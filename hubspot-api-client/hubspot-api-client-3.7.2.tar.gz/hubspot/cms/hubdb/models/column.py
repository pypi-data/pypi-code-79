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


class Column(object):
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
        "name": "str",
        "label": "str",
        "id": "str",
        "width": "int",
        "foreign_table_id": "int",
        "foreign_column_id": "int",
        "foreign_ids": "list[ForeignId]",
        "foreign_ids_by_name": "dict(str, ForeignId)",
        "foreign_ids_by_id": "dict(str, ForeignId)",
        "type": "str",
        "option_count": "int",
        "archived": "bool",
        "options": "list[Option]",
    }

    attribute_map = {
        "name": "name",
        "label": "label",
        "id": "id",
        "width": "width",
        "foreign_table_id": "foreignTableId",
        "foreign_column_id": "foreignColumnId",
        "foreign_ids": "foreignIds",
        "foreign_ids_by_name": "foreignIdsByName",
        "foreign_ids_by_id": "foreignIdsById",
        "type": "type",
        "option_count": "optionCount",
        "archived": "archived",
        "options": "options",
    }

    def __init__(
        self,
        name=None,
        label=None,
        id=None,
        width=None,
        foreign_table_id=None,
        foreign_column_id=None,
        foreign_ids=None,
        foreign_ids_by_name=None,
        foreign_ids_by_id=None,
        type=None,
        option_count=None,
        archived=None,
        options=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Column - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._label = None
        self._id = None
        self._width = None
        self._foreign_table_id = None
        self._foreign_column_id = None
        self._foreign_ids = None
        self._foreign_ids_by_name = None
        self._foreign_ids_by_id = None
        self._type = None
        self._option_count = None
        self._archived = None
        self._options = None
        self.discriminator = None

        self.name = name
        self.label = label
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if foreign_table_id is not None:
            self.foreign_table_id = foreign_table_id
        if foreign_column_id is not None:
            self.foreign_column_id = foreign_column_id
        if foreign_ids is not None:
            self.foreign_ids = foreign_ids
        if foreign_ids_by_name is not None:
            self.foreign_ids_by_name = foreign_ids_by_name
        if foreign_ids_by_id is not None:
            self.foreign_ids_by_id = foreign_ids_by_id
        self.type = type
        if option_count is not None:
            self.option_count = option_count
        if archived is not None:
            self.archived = archived
        if options is not None:
            self.options = options

    @property
    def name(self):
        """Gets the name of this Column.  # noqa: E501

        Name of the column  # noqa: E501

        :return: The name of this Column.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Column.

        Name of the column  # noqa: E501

        :param name: The name of this Column.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def label(self):
        """Gets the label of this Column.  # noqa: E501

        Label of the column  # noqa: E501

        :return: The label of this Column.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Column.

        Label of the column  # noqa: E501

        :param label: The label of this Column.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and label is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `label`, must not be `None`"
            )  # noqa: E501

        self._label = label

    @property
    def id(self):
        """Gets the id of this Column.  # noqa: E501

        Column Id  # noqa: E501

        :return: The id of this Column.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Column.

        Column Id  # noqa: E501

        :param id: The id of this Column.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def width(self):
        """Gets the width of this Column.  # noqa: E501

        Column width for HubDB UI  # noqa: E501

        :return: The width of this Column.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Column.

        Column width for HubDB UI  # noqa: E501

        :param width: The width of this Column.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def foreign_table_id(self):
        """Gets the foreign_table_id of this Column.  # noqa: E501

        Foreign table id referenced  # noqa: E501

        :return: The foreign_table_id of this Column.  # noqa: E501
        :rtype: int
        """
        return self._foreign_table_id

    @foreign_table_id.setter
    def foreign_table_id(self, foreign_table_id):
        """Sets the foreign_table_id of this Column.

        Foreign table id referenced  # noqa: E501

        :param foreign_table_id: The foreign_table_id of this Column.  # noqa: E501
        :type: int
        """

        self._foreign_table_id = foreign_table_id

    @property
    def foreign_column_id(self):
        """Gets the foreign_column_id of this Column.  # noqa: E501

        Foreign Column id  # noqa: E501

        :return: The foreign_column_id of this Column.  # noqa: E501
        :rtype: int
        """
        return self._foreign_column_id

    @foreign_column_id.setter
    def foreign_column_id(self, foreign_column_id):
        """Sets the foreign_column_id of this Column.

        Foreign Column id  # noqa: E501

        :param foreign_column_id: The foreign_column_id of this Column.  # noqa: E501
        :type: int
        """

        self._foreign_column_id = foreign_column_id

    @property
    def foreign_ids(self):
        """Gets the foreign_ids of this Column.  # noqa: E501

        Foreign Ids  # noqa: E501

        :return: The foreign_ids of this Column.  # noqa: E501
        :rtype: list[ForeignId]
        """
        return self._foreign_ids

    @foreign_ids.setter
    def foreign_ids(self, foreign_ids):
        """Sets the foreign_ids of this Column.

        Foreign Ids  # noqa: E501

        :param foreign_ids: The foreign_ids of this Column.  # noqa: E501
        :type: list[ForeignId]
        """

        self._foreign_ids = foreign_ids

    @property
    def foreign_ids_by_name(self):
        """Gets the foreign_ids_by_name of this Column.  # noqa: E501

        Foreign ids by name  # noqa: E501

        :return: The foreign_ids_by_name of this Column.  # noqa: E501
        :rtype: dict(str, ForeignId)
        """
        return self._foreign_ids_by_name

    @foreign_ids_by_name.setter
    def foreign_ids_by_name(self, foreign_ids_by_name):
        """Sets the foreign_ids_by_name of this Column.

        Foreign ids by name  # noqa: E501

        :param foreign_ids_by_name: The foreign_ids_by_name of this Column.  # noqa: E501
        :type: dict(str, ForeignId)
        """

        self._foreign_ids_by_name = foreign_ids_by_name

    @property
    def foreign_ids_by_id(self):
        """Gets the foreign_ids_by_id of this Column.  # noqa: E501

        Foreign ids  # noqa: E501

        :return: The foreign_ids_by_id of this Column.  # noqa: E501
        :rtype: dict(str, ForeignId)
        """
        return self._foreign_ids_by_id

    @foreign_ids_by_id.setter
    def foreign_ids_by_id(self, foreign_ids_by_id):
        """Sets the foreign_ids_by_id of this Column.

        Foreign ids  # noqa: E501

        :param foreign_ids_by_id: The foreign_ids_by_id of this Column.  # noqa: E501
        :type: dict(str, ForeignId)
        """

        self._foreign_ids_by_id = foreign_ids_by_id

    @property
    def type(self):
        """Gets the type of this Column.  # noqa: E501

        Type of the column  # noqa: E501

        :return: The type of this Column.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Column.

        Type of the column  # noqa: E501

        :param type: The type of this Column.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "NULL",
            "TEXT",
            "NUMBER",
            "URL",
            "IMAGE",
            "SELECT",
            "MULTISELECT",
            "BOOLEAN",
            "LOCATION",
            "DATE",
            "DATETIME",
            "CURRENCY",
            "RICHTEXT",
            "FOREIGN_ID",
            "VIDEO",
            "CTA",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def option_count(self):
        """Gets the option_count of this Column.  # noqa: E501

        Number of options available  # noqa: E501

        :return: The option_count of this Column.  # noqa: E501
        :rtype: int
        """
        return self._option_count

    @option_count.setter
    def option_count(self, option_count):
        """Sets the option_count of this Column.

        Number of options available  # noqa: E501

        :param option_count: The option_count of this Column.  # noqa: E501
        :type: int
        """

        self._option_count = option_count

    @property
    def archived(self):
        """Gets the archived of this Column.  # noqa: E501

        Specifies whether the column is archived  # noqa: E501

        :return: The archived of this Column.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this Column.

        Specifies whether the column is archived  # noqa: E501

        :param archived: The archived of this Column.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def options(self):
        """Gets the options of this Column.  # noqa: E501

        Options to choose for select and multi-select columns  # noqa: E501

        :return: The options of this Column.  # noqa: E501
        :rtype: list[Option]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Column.

        Options to choose for select and multi-select columns  # noqa: E501

        :param options: The options of this Column.  # noqa: E501
        :type: list[Option]
        """

        self._options = options

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
        if not isinstance(other, Column):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Column):
            return True

        return self.to_dict() != other.to_dict()
