import json
from typing import List, Union

import pytest
from ruamel.yaml import YAML

from great_expectations.core.batch import Batch, BatchRequest, PartitionRequest
from great_expectations.exceptions.exceptions import DataContextError
from great_expectations.execution_engine.sqlalchemy_batch_data import (
    SqlAlchemyBatchData,
)
from great_expectations.marshmallow__shade.exceptions import ValidationError

yaml = YAML()


def test_get_batch(data_context_with_sql_datasource_for_testing_get_batch):
    context = data_context_with_sql_datasource_for_testing_get_batch

    print(
        json.dumps(
            context.datasources["my_sqlite_db"].get_available_data_asset_names(),
            indent=4,
        )
    )

    # Successful specification using a typed BatchRequest
    context.get_batch(
        batch_request=BatchRequest(
            datasource_name="my_sqlite_db",
            data_connector_name="daily",
            data_asset_name="table_partitioned_by_date_column__A",
            partition_request=PartitionRequest(
                batch_identifiers={"date": "2020-01-15"}
            ),
        )
    )

    # Failed specification using an untyped BatchRequest
    with pytest.raises(TypeError):
        context.get_batch(
            batch_request={
                "datasource_name": "my_sqlite_db",
                "data_connector_name": "daily",
                "data_asset_name": "table_partitioned_by_date_column__A",
                "partition_request": {"batch_identifiers": {"date": "2020-01-15"}},
            }
        )

    # Failed specification using an incomplete BatchRequest
    with pytest.raises(ValueError):
        context.get_batch(
            batch_request=BatchRequest(
                datasource_name="my_sqlite_db",
                data_connector_name="daily",
                data_asset_name="table_partitioned_by_date_column__A",
                partition_request=PartitionRequest(batch_identifiers={}),
            )
        )

    # Failed specification using an incomplete BatchRequest
    with pytest.raises(ValueError):
        context.get_batch(
            batch_request=BatchRequest(
                datasource_name="my_sqlite_db",
                data_connector_name="daily",
                data_asset_name="table_partitioned_by_date_column__A",
            )
        )

    # Failed specification using an incomplete BatchRequest
    with pytest.raises(TypeError):
        context.get_batch(
            batch_request=BatchRequest(
                datasource_name="my_sqlite_db",
                data_connector_name="daily",
            )
        )

    # Failed specification using an incomplete BatchRequest
    # with pytest.raises(ValueError):
    with pytest.raises(TypeError):
        context.get_batch(
            batch_request=BatchRequest(
                # datasource_name=MISSING
                data_connector_name="daily",
                data_asset_name="table_partitioned_by_date_column__A",
                partition_request=PartitionRequest(batch_identifiers={}),
            )
        )

    # Successful specification using parameters
    context.get_batch(
        datasource_name="my_sqlite_db",
        data_connector_name="daily",
        data_asset_name="table_partitioned_by_date_column__A",
        date="2020-01-15",
    )

    # Successful specification using parameters without parameter names for the identifying triple
    # This is the thinnest this can plausibly get.
    context.get_batch(
        "my_sqlite_db",
        "daily",
        "table_partitioned_by_date_column__A",
        date="2020-01-15",
    )

    # Successful specification using parameters without parameter names for the identifying triple
    # In the case of a data_asset containing a single Batch, we don't even need parameters
    context.get_batch(
        "my_sqlite_db",
        "whole_table",
        "table_partitioned_by_date_column__A",
    )

    # Successful specification using parameters and partition_request
    context.get_batch(
        "my_sqlite_db",
        "daily",
        "table_partitioned_by_date_column__A",
        partition_request=PartitionRequest(
            {"batch_identifiers": {"date": "2020-01-15"}}
        ),
    )

    # Successful specification using parameters and batch_identifiers
    context.get_batch(
        "my_sqlite_db",
        "daily",
        "table_partitioned_by_date_column__A",
        batch_identifiers={"date": "2020-01-15"},
    )


def test_get_validator(data_context_with_sql_datasource_for_testing_get_batch):
    context = data_context_with_sql_datasource_for_testing_get_batch
    context.create_expectation_suite("my_expectations")

    print(
        json.dumps(
            context.datasources["my_sqlite_db"].get_available_data_asset_names(),
            indent=4,
        )
    )

    # Successful specification using a typed BatchRequest
    context.get_validator(
        batch_request=BatchRequest(
            datasource_name="my_sqlite_db",
            data_connector_name="daily",
            data_asset_name="table_partitioned_by_date_column__A",
            partition_request=PartitionRequest(
                batch_identifiers={"date": "2020-01-15"}
            ),
        ),
        expectation_suite_name="my_expectations",
    )

    # Failed specification using an untyped BatchRequest
    with pytest.raises(TypeError):
        context.get_validator(
            batch_request={
                "datasource_name": "my_sqlite_db",
                "data_connector_name": "daily",
                "data_asset_name": "table_partitioned_by_date_column__A",
                "partition_request": {"batch_identifiers": {"date": "2020-01-15"}},
            },
            expectation_suite_name="my_expectations",
        )

    # Failed specification using an incomplete BatchRequest
    with pytest.raises(ValueError):
        context.get_validator(
            batch_request=BatchRequest(
                datasource_name="my_sqlite_db",
                data_connector_name="daily",
                data_asset_name="table_partitioned_by_date_column__A",
                partition_request=PartitionRequest(batch_identifiers={}),
            ),
            expectation_suite_name="my_expectations",
        )

    # Failed specification using an incomplete BatchRequest
    with pytest.raises(ValueError):
        context.get_validator(
            batch_request=BatchRequest(
                datasource_name="my_sqlite_db",
                data_connector_name="daily",
                data_asset_name="table_partitioned_by_date_column__A",
            ),
            expectation_suite_name="my_expectations",
        )

    # Failed specification using an incomplete BatchRequest
    with pytest.raises(TypeError):
        context.get_validator(
            batch_request=BatchRequest(
                datasource_name="my_sqlite_db",
                data_connector_name="daily",
            ),
            expectation_suite_name="my_expectations",
        )

    # Failed specification using an incomplete BatchRequest
    # with pytest.raises(ValueError):
    with pytest.raises(TypeError):
        context.get_validator(
            batch_request=BatchRequest(
                # datasource_name=MISSING
                data_connector_name="daily",
                data_asset_name="table_partitioned_by_date_column__A",
                partition_request=PartitionRequest(batch_identifiers={}),
            ),
            expectation_suite_name="my_expectations",
        )

    # Successful specification using parameters
    context.get_validator(
        datasource_name="my_sqlite_db",
        data_connector_name="daily",
        data_asset_name="table_partitioned_by_date_column__A",
        date="2020-01-15",
        expectation_suite_name="my_expectations",
    )

    # Successful specification using parameters without parameter names for the identifying triple
    # This is the thinnest this can plausibly get.
    context.get_validator(
        "my_sqlite_db",
        "daily",
        "table_partitioned_by_date_column__A",
        date="2020-01-15",
        expectation_suite_name="my_expectations",
    )

    # Successful specification using parameters without parameter names for the identifying triple
    # In the case of a data_asset containing a single Batch, we don't even need parameters
    context.get_validator(
        "my_sqlite_db",
        "whole_table",
        "table_partitioned_by_date_column__A",
        expectation_suite_name="my_expectations",
    )

    # Successful specification using parameters and partition_request
    context.get_validator(
        "my_sqlite_db",
        "daily",
        "table_partitioned_by_date_column__A",
        partition_request=PartitionRequest(
            {"batch_identifiers": {"date": "2020-01-15"}}
        ),
        expectation_suite_name="my_expectations",
    )

    # Successful specification using parameters and batch_identifiers
    context.get_validator(
        "my_sqlite_db",
        "daily",
        "table_partitioned_by_date_column__A",
        batch_identifiers={"date": "2020-01-15"},
        expectation_suite_name="my_expectations",
    )


def test_get_validator_expectation_suite_options(
    data_context_with_sql_datasource_for_testing_get_batch,
):
    context = data_context_with_sql_datasource_for_testing_get_batch
    context.create_expectation_suite("some_expectations")

    # Successful specification with an existing expectation_suite_name
    context.get_validator(
        datasource_name="my_sqlite_db",
        data_connector_name="daily",
        data_asset_name="table_partitioned_by_date_column__A",
        date="2020-01-15",
        expectation_suite_name="some_expectations",
    )

    # Successful specification with a fetched ExpectationSuite object
    some_expectations = context.get_expectation_suite("some_expectations")
    context.get_validator(
        datasource_name="my_sqlite_db",
        data_connector_name="daily",
        data_asset_name="table_partitioned_by_date_column__A",
        date="2020-01-15",
        expectation_suite=some_expectations,
    )

    # Successful specification with a fresh ExpectationSuite object
    some_more_expectations = context.create_expectation_suite(
        expectation_suite_name="some_more_expectations"
    )
    context.get_validator(
        datasource_name="my_sqlite_db",
        data_connector_name="daily",
        data_asset_name="table_partitioned_by_date_column__A",
        date="2020-01-15",
        expectation_suite=some_more_expectations,
    )

    # Successful specification using overwrite_existing_expectation_suite
    context.get_validator(
        batch_request=BatchRequest(
            datasource_name="my_sqlite_db",
            data_connector_name="daily",
            data_asset_name="table_partitioned_by_date_column__A",
            partition_request=PartitionRequest(
                batch_identifiers={"date": "2020-01-15"}
            ),
        ),
        create_expectation_suite_with_name="yet_more_expectations",
        # TODO: readd
        # overwrite_existing_expectation_suite=True,
    )

    # Failed specification: incorrectly typed expectation suite
    with pytest.raises(TypeError):
        context.get_validator(
            datasource_name="my_sqlite_db",
            data_connector_name="daily",
            data_asset_name="table_partitioned_by_date_column__A",
            date="2020-01-15",
            expectation_suite={
                "im": "a",
                "dictionary": "not a",
                "ExepctationSuite": False,
            },
        )


def test_get_batch_list_from_new_style_datasource_with_sql_datasource(
    sa, data_context_with_sql_datasource_for_testing_get_batch
):
    context = data_context_with_sql_datasource_for_testing_get_batch

    batch_request: Union[dict, BatchRequest] = {
        "datasource_name": "my_sqlite_db",
        "data_connector_name": "daily",
        "data_asset_name": "table_partitioned_by_date_column__A",
        "partition_request": {"batch_identifiers": {"date": "2020-01-15"}},
    }
    batch_list: List[Batch] = context.get_batch_list(**batch_request)

    assert len(batch_list) == 1

    batch: Batch = batch_list[0]
    assert batch.batch_spec is not None
    assert (
        batch.batch_definition["data_asset_name"]
        == "table_partitioned_by_date_column__A"
    )
    assert batch.batch_definition["partition_definition"] == {"date": "2020-01-15"}
    assert isinstance(batch.data, SqlAlchemyBatchData)
