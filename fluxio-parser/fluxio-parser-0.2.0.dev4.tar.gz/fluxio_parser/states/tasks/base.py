"""Contains base classes used to represent AWS Step Functions Task States"""
import ast
import logging
import re
from typing import Any, Dict, Optional, Set

import astor

from ...constants import INVALID_RESULT_PATH_PATTERN, RESERVED_INPUT_DATA_KEYS
from ...exceptions import assert_supported_operation
from ...transformers import DataDictTransformer
from ...util import (
    CallableOption,
    convert_input_data_ref,
    GET_VALUE_MAP,
    hash_node,
    parse_options,
    serialize_error_name,
)
from ..base import State, StateMachineFragment
from .retry import Retry, RETRY_OPTION_MAP


def convert_data_dict(node: Any, visitor: ast.NodeVisitor) -> str:
    """Convert dict with ``data[...]`` references to ``"$[...]"``"""
    return GET_VALUE_MAP[dict](DataDictTransformer().visit(node), visitor)


# Map of task option name to an option schema
OPTION_MAP = {
    "key": CallableOption(
        value_type=ast.Str,
        value_type_label="string",
        get_value=GET_VALUE_MAP[str],
        default_value=lambda node, visitor: f"{node.func.id}-{hash_node(node)}",
    ),
    "timeout": CallableOption(
        value_type=ast.Num,
        value_type_label="integer",
        get_value=GET_VALUE_MAP[int],
        default_value=300,
    ),
    # Options for CodeBuild
    "env": CallableOption(
        value_type=ast.Dict,
        value_type_label="string",
        get_value=convert_data_dict,
        default_value={},
    ),
    "build_arg_vars": CallableOption(
        value_type=ast.Dict,
        value_type_label="dict",
        get_value=GET_VALUE_MAP[dict],
        default_value={},
    ),
}


class Catch(StateMachineFragment):
    """Catch state machine fragment.

    A catch is the state machine equivalent of an exception handler. It is used to
    handle failed tasks and determine which state to transition to next.

    See: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html#error-handling-fallback-states

    For example::

        try:
            FirstTask(key="first")
        except CustomError:
            ErrorHandlerTask(key="handle-error")

        SecondTask(key="second")

    resolves to::

        {
            "Type": "Task",
            "Resource": "arn:aws:states:::lambda:invoke",
            "Parameters": {
                "FunctionName": "...first"
            },
            Catch": [
                {
                   "ErrorEquals": ["CustomError"],
                   "ResultPath": "$['error']",
                   "Next": "handle-error"
                },
            ],
            "Next": "second"
        }
    """

    def to_dict(self) -> Dict:
        """Return a serialized representation of the Catch fragment."""
        data = {"ResultPath": "$.error"}
        self._set_end_or_next(data)
        if isinstance(self.ast_node.type, ast.Tuple):
            data["ErrorEquals"] = [
                serialize_error_name(el) for el in self.ast_node.type.elts
            ]
        else:
            data["ErrorEquals"] = [serialize_error_name(self.ast_node.type)]

        return data


class TaskState(State):
    """Task state

    A Task state performs an action using an AWS service integration. We currently
    support a select few integrations, with Lambda as the default. Task states
    are generated by defining a class that inherits from ``Task`` then instantiating
    that class in an .sfn file. Nested state machine tasks are defined as module-level
    functions.

    When instantiating a task state, you can pass part of input data object as the
    first positional argument. To explicitly set the state key in the state machine
    definition, provide ``key`` keyword argument. The default task timeout is 300
    seconds. Override this by passing a ``timeout`` keyword argument.

    Child classes should extend ``TaskState`` and override, at minimum:
    * ``resource``
    * ``parameters``

    See:
    * https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-task-state.html
    * https://docs.aws.amazon.com/step-functions/latest/dg/concepts-service-integrations.html

    For example::

        class MyTask(Task):
            async def run(event, context):
                return

        data["output"] = MyTask(data["input"], key="hello")

    resolves to::

        {
            "Type": "Task",
            "Resource": "arn:aws:states:::lambda:invoke",
            "Parameters": {
                "FunctionName": "..."
            },
            "InputPath": "$['data']",
            "ResultPath": "$['output']"
        }
    """

    # Subclasses can add default retry configuration
    DEFAULT_RETRIES = []

    def __init__(
        self,
        state_graph: "nx.DiGraph",  # noqa: F821
        key: str,
        ast_node: Any,
        state_machine_visitor: "StateMachineVisitor",  # noqa: F821
        options: Dict[str, Any],
    ) -> None:
        """Initialize a TaskState

        Args:
            state_graph: DAG of state machine fragments with edges between them
            key: Key of the fragment in the state machine's States value. This only
                really applies to States, not generic fragments.
            ast_node: AST node for this fragment in the .sfn file
            state_machine_visitor: State machine visitor that is the parent of this
                state. This can be used to understand the context of the state.
            options: Options from the task class attributes combined with overrides
                passed in for the specific task.

        """
        super().__init__(state_graph, key, ast_node)
        self.state_machine_visitor = state_machine_visitor
        self.options = options
        self.catches = []
        self.current_catch = None
        self.retries = self.DEFAULT_RETRIES.copy()

    @property
    def task_definition_name(self) -> str:
        """Returns the name of the task definition.

        This could be the class or function name depending on the type of task.
        """
        return self.ast_node.value.func.id

    @property
    def resource(self) -> str:
        """Returns the task state Resource key.

        Child classes must override this method.
        """
        raise NotImplementedError()

    @property
    def parameters(self) -> Dict:
        """Returns the task state Parameters key.

        Child classes must override this method.

        This value will be embedded in the state machine definition resource in a
        CloudFormation template so it can contain substitution (!Sub) variables.
        """
        raise NotImplementedError()

    @property
    def variable_names(self) -> Set[str]:
        """Returns set of variable names corresponding to task builder outputs.

        These strings include all the CloudFormation Sub variables (e.g. ``${Foo}``)
        present in the ``parameters`` dict.
        """
        raise NotImplementedError()

    def add_catch(self, node: Any) -> Catch:
        """Create a new Catch instance, add it to list of catches, set the current catch

        Args:
            node: AST node representing the exception handler

        Returns:
            new Catch fragment

        """
        catch = Catch(self.state_graph, f"Catch-{hash_node(node)}", node)
        logging.debug(f"Adding catch {catch} to {self}")
        self.catches.append(catch)
        self.current_catch = catch
        return catch

    def add_retries(self, context_manager: Any) -> None:
        """Add retry configuration to this TaskState

        Args:
            context_manager: the Call representing the context manager

        """
        retry_options = parse_options(RETRY_OPTION_MAP, context_manager)
        self.retries.append(Retry(**retry_options))

    def shape(self) -> None:
        """Shape the graph for this Task state."""
        if len(self.edges) > 0:
            # For each catch, if it ends with a non-terminal state then add an
            # edge to the next state *after* the task.
            for catch in self.catches:
                descendants = catch.descendants
                if len(descendants) > 0 and not descendants[-1].TERMINAL:
                    self.state_graph.add_edge(descendants[-1], self.edges[0])

    def _get_input_path(self) -> str:
        """Get the InputPath value for the task state

        Returns:
            input path string

        """
        if len(self.ast_node.value.args) > 0:
            return re.sub(
                "^data", "$", astor.to_source(self.ast_node.value.args[0]).strip()
            )

        return "$"

    def _get_result_path(self) -> Optional[str]:
        """Get the ResultPath value for the task state

        If the result path was not explicitly provided, return None to indicate that
        the the result should be discarded.

        Returns:
            result path string or None

        """
        if isinstance(self.ast_node, ast.Assign) and len(self.ast_node.targets) > 0:
            result_path = convert_input_data_ref(self.ast_node.targets[0])
            assert_supported_operation(
                re.search(INVALID_RESULT_PATH_PATTERN, result_path) is None,
                "Task result path is invalid. Check that it does not contain reserved"
                f" keys: {', '.join(RESERVED_INPUT_DATA_KEYS)}",
                self.ast_node,
            )
            return result_path

        return None

    def to_dict(self) -> Dict:
        """Return a serialized representation of the task state"""
        data = {
            "Type": "Task",
            "Resource": self.resource,
            "Parameters": self.parameters,
            "InputPath": "$",
            "ResultPath": self._get_result_path(),
        }

        if "timeout" in self.options:
            data["TimeoutSeconds"] = self.options["timeout"]

        if len(self.catches) > 0:
            data["Catch"] = [c.to_dict() for c in self.catches]

        if len(self.retries) > 0:
            data["Retry"] = [r.to_dict() for r in self.retries]

        self._set_end_or_next(data)
        return data
