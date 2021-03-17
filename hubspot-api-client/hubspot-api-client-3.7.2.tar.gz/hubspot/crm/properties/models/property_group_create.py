# coding: utf-8

"""
    Properties

    All HubSpot objects store data in default and custom properties. These endpoints provide access to read and modify object properties in HubSpot.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.properties.configuration import Configuration


class PropertyGroupCreate(object):
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
    openapi_types = {"name": "str", "label": "str", "display_order": "int"}

    attribute_map = {"name": "name", "label": "label", "display_order": "displayOrder"}

    def __init__(
        self, name=None, label=None, display_order=None, local_vars_configuration=None
    ):  # noqa: E501
        """PropertyGroupCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._label = None
        self._display_order = None
        self.discriminator = None

        self.name = name
        self.label = label
        if display_order is not None:
            self.display_order = display_order

    @property
    def name(self):
        """Gets the name of this PropertyGroupCreate.  # noqa: E501

        The internal property group name, which must be used when referencing the property group via the API.  # noqa: E501

        :return: The name of this PropertyGroupCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PropertyGroupCreate.

        The internal property group name, which must be used when referencing the property group via the API.  # noqa: E501

        :param name: The name of this PropertyGroupCreate.  # noqa: E501
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
        """Gets the label of this PropertyGroupCreate.  # noqa: E501

        A human-readable label that will be shown in HubSpot.  # noqa: E501

        :return: The label of this PropertyGroupCreate.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PropertyGroupCreate.

        A human-readable label that will be shown in HubSpot.  # noqa: E501

        :param label: The label of this PropertyGroupCreate.  # noqa: E501
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
    def display_order(self):
        """Gets the display_order of this PropertyGroupCreate.  # noqa: E501

        Property groups are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property group to be displayed after any positive values.  # noqa: E501

        :return: The display_order of this PropertyGroupCreate.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this PropertyGroupCreate.

        Property groups are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property group to be displayed after any positive values.  # noqa: E501

        :param display_order: The display_order of this PropertyGroupCreate.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

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
        if not isinstance(other, PropertyGroupCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PropertyGroupCreate):
            return True

        return self.to_dict() != other.to_dict()
