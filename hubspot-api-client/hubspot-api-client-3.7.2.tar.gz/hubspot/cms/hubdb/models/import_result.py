# coding: utf-8

"""
    HubDB endpoints

    HubDB is a relational data store that presents data as rows, columns, and cells in a table, much like a spreadsheet. HubDB tables can be added or modified [in the HubSpot CMS](https://knowledge.hubspot.com/cos-general/how-to-edit-hubdb-tables), but you can also use the API endpoints documented here. For more information on HubDB tables and using their data on a HubSpot site, see the [CMS developers site](https://designers.hubspot.com/docs/tools/hubdb). You can also see the [documentation for dynamic pages](https://designers.hubspot.com/docs/tutorials/how-to-build-dynamic-pages-with-hubdb) for more details about the `useForPages` field.  HubDB tables support `draft` and `live` versions and you can publish and unpublish the live version. This allows you to update data in the table, either for testing or to allow for a manual approval process, without affecting any live pages using the existing data. Draft data can be reviewed, pushed to live version, and published by a user working in HubSpot or published via the API. Draft data can also be discarded, allowing users to go back to the live version of the data without disrupting it. If a table is set to be `allowed for public access`, you can access the published version of the table and rows without any authentication.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.hubdb.configuration import Configuration


class ImportResult(object):
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
        "errors": "list[Error]",
        "rows_imported": "int",
        "duplicate_rows": "int",
        "row_limit_exceeded": "bool",
    }

    attribute_map = {
        "errors": "errors",
        "rows_imported": "rowsImported",
        "duplicate_rows": "duplicateRows",
        "row_limit_exceeded": "rowLimitExceeded",
    }

    def __init__(
        self,
        errors=None,
        rows_imported=None,
        duplicate_rows=None,
        row_limit_exceeded=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """ImportResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._errors = None
        self._rows_imported = None
        self._duplicate_rows = None
        self._row_limit_exceeded = None
        self.discriminator = None

        self.errors = errors
        self.rows_imported = rows_imported
        self.duplicate_rows = duplicate_rows
        self.row_limit_exceeded = row_limit_exceeded

    @property
    def errors(self):
        """Gets the errors of this ImportResult.  # noqa: E501

        List of errors during import  # noqa: E501

        :return: The errors of this ImportResult.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ImportResult.

        List of errors during import  # noqa: E501

        :param errors: The errors of this ImportResult.  # noqa: E501
        :type: list[Error]
        """
        if (
            self.local_vars_configuration.client_side_validation and errors is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `errors`, must not be `None`"
            )  # noqa: E501

        self._errors = errors

    @property
    def rows_imported(self):
        """Gets the rows_imported of this ImportResult.  # noqa: E501

        Specifies number of rows imported  # noqa: E501

        :return: The rows_imported of this ImportResult.  # noqa: E501
        :rtype: int
        """
        return self._rows_imported

    @rows_imported.setter
    def rows_imported(self, rows_imported):
        """Sets the rows_imported of this ImportResult.

        Specifies number of rows imported  # noqa: E501

        :param rows_imported: The rows_imported of this ImportResult.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and rows_imported is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `rows_imported`, must not be `None`"
            )  # noqa: E501

        self._rows_imported = rows_imported

    @property
    def duplicate_rows(self):
        """Gets the duplicate_rows of this ImportResult.  # noqa: E501

        Specifies number of duplicate rows  # noqa: E501

        :return: The duplicate_rows of this ImportResult.  # noqa: E501
        :rtype: int
        """
        return self._duplicate_rows

    @duplicate_rows.setter
    def duplicate_rows(self, duplicate_rows):
        """Sets the duplicate_rows of this ImportResult.

        Specifies number of duplicate rows  # noqa: E501

        :param duplicate_rows: The duplicate_rows of this ImportResult.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and duplicate_rows is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `duplicate_rows`, must not be `None`"
            )  # noqa: E501

        self._duplicate_rows = duplicate_rows

    @property
    def row_limit_exceeded(self):
        """Gets the row_limit_exceeded of this ImportResult.  # noqa: E501

        Specifies whether row limit exceeded during import  # noqa: E501

        :return: The row_limit_exceeded of this ImportResult.  # noqa: E501
        :rtype: bool
        """
        return self._row_limit_exceeded

    @row_limit_exceeded.setter
    def row_limit_exceeded(self, row_limit_exceeded):
        """Sets the row_limit_exceeded of this ImportResult.

        Specifies whether row limit exceeded during import  # noqa: E501

        :param row_limit_exceeded: The row_limit_exceeded of this ImportResult.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and row_limit_exceeded is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `row_limit_exceeded`, must not be `None`"
            )  # noqa: E501

        self._row_limit_exceeded = row_limit_exceeded

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
        if not isinstance(other, ImportResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportResult):
            return True

        return self.to_dict() != other.to_dict()
