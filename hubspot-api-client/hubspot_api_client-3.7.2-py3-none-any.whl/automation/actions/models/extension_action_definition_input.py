# coding: utf-8

"""
    Custom Workflow Actions

    Create custom workflow actions  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.automation.actions.configuration import Configuration


class ExtensionActionDefinitionInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "functions": "list[ActionFunction]",
        "action_url": "str",
        "published": "bool",
        "archived_at": "int",
        "input_fields": "list[InputFieldDefinition]",
        "object_request_options": "ObjectRequestOptions",
        "input_field_dependencies": "list[OneOfSingleFieldDependencyConditionalSingleFieldDependency]",
        "labels": "dict(str, ActionLabels)",
        "object_types": "list[str]",
    }

    attribute_map = {
        "functions": "functions",
        "action_url": "actionUrl",
        "published": "published",
        "archived_at": "archivedAt",
        "input_fields": "inputFields",
        "object_request_options": "objectRequestOptions",
        "input_field_dependencies": "inputFieldDependencies",
        "labels": "labels",
        "object_types": "objectTypes",
    }

    def __init__(
        self,
        functions=None,
        action_url=None,
        published=None,
        archived_at=None,
        input_fields=None,
        object_request_options=None,
        input_field_dependencies=None,
        labels=None,
        object_types=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """ExtensionActionDefinitionInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._functions = None
        self._action_url = None
        self._published = None
        self._archived_at = None
        self._input_fields = None
        self._object_request_options = None
        self._input_field_dependencies = None
        self._labels = None
        self._object_types = None
        self.discriminator = None

        self.functions = functions
        self.action_url = action_url
        self.published = published
        if archived_at is not None:
            self.archived_at = archived_at
        self.input_fields = input_fields
        if object_request_options is not None:
            self.object_request_options = object_request_options
        if input_field_dependencies is not None:
            self.input_field_dependencies = input_field_dependencies
        self.labels = labels
        self.object_types = object_types

    @property
    def functions(self):
        """Gets the functions of this ExtensionActionDefinitionInput.  # noqa: E501

        A list of functions associated with the custom workflow action.  # noqa: E501

        :return: The functions of this ExtensionActionDefinitionInput.  # noqa: E501
        :rtype: list[ActionFunction]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        """Sets the functions of this ExtensionActionDefinitionInput.

        A list of functions associated with the custom workflow action.  # noqa: E501

        :param functions: The functions of this ExtensionActionDefinitionInput.  # noqa: E501
        :type: list[ActionFunction]
        """
        if (
            self.local_vars_configuration.client_side_validation and functions is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `functions`, must not be `None`"
            )  # noqa: E501

        self._functions = functions

    @property
    def action_url(self):
        """Gets the action_url of this ExtensionActionDefinitionInput.  # noqa: E501

        The URL that will accept an HTTPS request each time workflows executes the custom action.  # noqa: E501

        :return: The action_url of this ExtensionActionDefinitionInput.  # noqa: E501
        :rtype: str
        """
        return self._action_url

    @action_url.setter
    def action_url(self, action_url):
        """Sets the action_url of this ExtensionActionDefinitionInput.

        The URL that will accept an HTTPS request each time workflows executes the custom action.  # noqa: E501

        :param action_url: The action_url of this ExtensionActionDefinitionInput.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and action_url is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `action_url`, must not be `None`"
            )  # noqa: E501

        self._action_url = action_url

    @property
    def published(self):
        """Gets the published of this ExtensionActionDefinitionInput.  # noqa: E501

        Whether this custom action is published to customers.  # noqa: E501

        :return: The published of this ExtensionActionDefinitionInput.  # noqa: E501
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this ExtensionActionDefinitionInput.

        Whether this custom action is published to customers.  # noqa: E501

        :param published: The published of this ExtensionActionDefinitionInput.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation and published is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `published`, must not be `None`"
            )  # noqa: E501

        self._published = published

    @property
    def archived_at(self):
        """Gets the archived_at of this ExtensionActionDefinitionInput.  # noqa: E501

        The date that this custom action was archived, if the custom action is archived.  # noqa: E501

        :return: The archived_at of this ExtensionActionDefinitionInput.  # noqa: E501
        :rtype: int
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this ExtensionActionDefinitionInput.

        The date that this custom action was archived, if the custom action is archived.  # noqa: E501

        :param archived_at: The archived_at of this ExtensionActionDefinitionInput.  # noqa: E501
        :type: int
        """

        self._archived_at = archived_at

    @property
    def input_fields(self):
        """Gets the input_fields of this ExtensionActionDefinitionInput.  # noqa: E501

        The list of input fields to display in this custom action.  # noqa: E501

        :return: The input_fields of this ExtensionActionDefinitionInput.  # noqa: E501
        :rtype: list[InputFieldDefinition]
        """
        return self._input_fields

    @input_fields.setter
    def input_fields(self, input_fields):
        """Sets the input_fields of this ExtensionActionDefinitionInput.

        The list of input fields to display in this custom action.  # noqa: E501

        :param input_fields: The input_fields of this ExtensionActionDefinitionInput.  # noqa: E501
        :type: list[InputFieldDefinition]
        """
        if (
            self.local_vars_configuration.client_side_validation
            and input_fields is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `input_fields`, must not be `None`"
            )  # noqa: E501

        self._input_fields = input_fields

    @property
    def object_request_options(self):
        """Gets the object_request_options of this ExtensionActionDefinitionInput.  # noqa: E501


        :return: The object_request_options of this ExtensionActionDefinitionInput.  # noqa: E501
        :rtype: ObjectRequestOptions
        """
        return self._object_request_options

    @object_request_options.setter
    def object_request_options(self, object_request_options):
        """Sets the object_request_options of this ExtensionActionDefinitionInput.


        :param object_request_options: The object_request_options of this ExtensionActionDefinitionInput.  # noqa: E501
        :type: ObjectRequestOptions
        """

        self._object_request_options = object_request_options

    @property
    def input_field_dependencies(self):
        """Gets the input_field_dependencies of this ExtensionActionDefinitionInput.  # noqa: E501

        A list of dependencies between the input fields. These configure when the input fields should be visible.  # noqa: E501

        :return: The input_field_dependencies of this ExtensionActionDefinitionInput.  # noqa: E501
        :rtype: list[OneOfSingleFieldDependencyConditionalSingleFieldDependency]
        """
        return self._input_field_dependencies

    @input_field_dependencies.setter
    def input_field_dependencies(self, input_field_dependencies):
        """Sets the input_field_dependencies of this ExtensionActionDefinitionInput.

        A list of dependencies between the input fields. These configure when the input fields should be visible.  # noqa: E501

        :param input_field_dependencies: The input_field_dependencies of this ExtensionActionDefinitionInput.  # noqa: E501
        :type: list[OneOfSingleFieldDependencyConditionalSingleFieldDependency]
        """

        self._input_field_dependencies = input_field_dependencies

    @property
    def labels(self):
        """Gets the labels of this ExtensionActionDefinitionInput.  # noqa: E501

        The user-facing labels for the custom action.  # noqa: E501

        :return: The labels of this ExtensionActionDefinitionInput.  # noqa: E501
        :rtype: dict(str, ActionLabels)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ExtensionActionDefinitionInput.

        The user-facing labels for the custom action.  # noqa: E501

        :param labels: The labels of this ExtensionActionDefinitionInput.  # noqa: E501
        :type: dict(str, ActionLabels)
        """
        if (
            self.local_vars_configuration.client_side_validation and labels is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `labels`, must not be `None`"
            )  # noqa: E501

        self._labels = labels

    @property
    def object_types(self):
        """Gets the object_types of this ExtensionActionDefinitionInput.  # noqa: E501

        The object types that this custom action supports.  # noqa: E501

        :return: The object_types of this ExtensionActionDefinitionInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._object_types

    @object_types.setter
    def object_types(self, object_types):
        """Sets the object_types of this ExtensionActionDefinitionInput.

        The object types that this custom action supports.  # noqa: E501

        :param object_types: The object_types of this ExtensionActionDefinitionInput.  # noqa: E501
        :type: list[str]
        """
        if (
            self.local_vars_configuration.client_side_validation
            and object_types is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `object_types`, must not be `None`"
            )  # noqa: E501

        self._object_types = object_types

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExtensionActionDefinitionInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExtensionActionDefinitionInput):
            return True

        return self.to_dict() != other.to_dict()
