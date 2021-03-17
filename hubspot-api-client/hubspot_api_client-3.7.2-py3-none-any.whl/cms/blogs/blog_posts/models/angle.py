# coding: utf-8

"""
    Blog Post endpoints

    \"Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags\"  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.blogs.blog_posts.configuration import Configuration


class Angle(object):
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
    openapi_types = {"value": "float", "units": "str"}

    attribute_map = {"value": "value", "units": "units"}

    def __init__(
        self, value=None, units=None, local_vars_configuration=None
    ):  # noqa: E501
        """Angle - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._units = None
        self.discriminator = None

        self.value = value
        self.units = units

    @property
    def value(self):
        """Gets the value of this Angle.  # noqa: E501


        :return: The value of this Angle.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Angle.


        :param value: The value of this Angle.  # noqa: E501
        :type: float
        """
        if (
            self.local_vars_configuration.client_side_validation and value is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `value`, must not be `None`"
            )  # noqa: E501

        self._value = value

    @property
    def units(self):
        """Gets the units of this Angle.  # noqa: E501


        :return: The units of this Angle.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this Angle.


        :param units: The units of this Angle.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and units is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `units`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["deg", "grad", "rad", "turn"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and units not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `units` ({0}), must be one of {1}".format(  # noqa: E501
                    units, allowed_values
                )
            )

        self._units = units

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
        if not isinstance(other, Angle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Angle):
            return True

        return self.to_dict() != other.to_dict()
