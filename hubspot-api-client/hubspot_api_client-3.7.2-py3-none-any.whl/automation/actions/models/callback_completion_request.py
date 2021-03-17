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


class CallbackCompletionRequest(object):
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
    openapi_types = {"output_fields": "dict(str, str)"}

    attribute_map = {"output_fields": "outputFields"}

    def __init__(self, output_fields=None, local_vars_configuration=None):  # noqa: E501
        """CallbackCompletionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._output_fields = None
        self.discriminator = None

        self.output_fields = output_fields

    @property
    def output_fields(self):
        """Gets the output_fields of this CallbackCompletionRequest.  # noqa: E501

        A map of action output names and values.  # noqa: E501

        :return: The output_fields of this CallbackCompletionRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._output_fields

    @output_fields.setter
    def output_fields(self, output_fields):
        """Sets the output_fields of this CallbackCompletionRequest.

        A map of action output names and values.  # noqa: E501

        :param output_fields: The output_fields of this CallbackCompletionRequest.  # noqa: E501
        :type: dict(str, str)
        """
        if (
            self.local_vars_configuration.client_side_validation
            and output_fields is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `output_fields`, must not be `None`"
            )  # noqa: E501

        self._output_fields = output_fields

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
        if not isinstance(other, CallbackCompletionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CallbackCompletionRequest):
            return True

        return self.to_dict() != other.to_dict()
