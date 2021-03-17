# coding: utf-8

"""
    CRM Imports

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.imports.configuration import Configuration


class PublicObjectListRecord(object):
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
    openapi_types = {"list_id": "str", "object_type": "str"}

    attribute_map = {"list_id": "listId", "object_type": "objectType"}

    def __init__(
        self, list_id=None, object_type=None, local_vars_configuration=None
    ):  # noqa: E501
        """PublicObjectListRecord - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._list_id = None
        self._object_type = None
        self.discriminator = None

        self.list_id = list_id
        self.object_type = object_type

    @property
    def list_id(self):
        """Gets the list_id of this PublicObjectListRecord.  # noqa: E501

        The ID of the list containing the imported objects.  # noqa: E501

        :return: The list_id of this PublicObjectListRecord.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this PublicObjectListRecord.

        The ID of the list containing the imported objects.  # noqa: E501

        :param list_id: The list_id of this PublicObjectListRecord.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and list_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `list_id`, must not be `None`"
            )  # noqa: E501

        self._list_id = list_id

    @property
    def object_type(self):
        """Gets the object_type of this PublicObjectListRecord.  # noqa: E501

        The type of object contained in the list.  # noqa: E501

        :return: The object_type of this PublicObjectListRecord.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this PublicObjectListRecord.

        The type of object contained in the list.  # noqa: E501

        :param object_type: The object_type of this PublicObjectListRecord.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and object_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `object_type`, must not be `None`"
            )  # noqa: E501

        self._object_type = object_type

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
        if not isinstance(other, PublicObjectListRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicObjectListRecord):
            return True

        return self.to_dict() != other.to_dict()
