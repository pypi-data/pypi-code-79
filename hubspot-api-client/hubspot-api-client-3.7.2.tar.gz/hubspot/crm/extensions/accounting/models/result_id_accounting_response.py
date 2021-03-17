# coding: utf-8

"""
    Accounting Extension

    These APIs allow you to interact with HubSpot's Accounting Extension. It allows you to: * Specify the URLs that HubSpot will use when making webhook requests to your external accounting system. * Respond to webhook calls made to your external accounting system by HubSpot   # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.accounting.configuration import Configuration


class ResultIdAccountingResponse(object):
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
    openapi_types = {"result": "str", "id": "str"}

    attribute_map = {"result": "@result", "id": "id"}

    def __init__(
        self, result=None, id=None, local_vars_configuration=None
    ):  # noqa: E501
        """ResultIdAccountingResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._id = None
        self.discriminator = None

        self.result = result
        self.id = id

    @property
    def result(self):
        """Gets the result of this ResultIdAccountingResponse.  # noqa: E501

        Designates if the response is a success ('OK') or failure ('ERR').  # noqa: E501

        :return: The result of this ResultIdAccountingResponse.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ResultIdAccountingResponse.

        Designates if the response is a success ('OK') or failure ('ERR').  # noqa: E501

        :param result: The result of this ResultIdAccountingResponse.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and result is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `result`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["OK", "ERR"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and result not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}".format(  # noqa: E501
                    result, allowed_values
                )
            )

        self._result = result

    @property
    def id(self):
        """Gets the id of this ResultIdAccountingResponse.  # noqa: E501

        The ID of created entity.  # noqa: E501

        :return: The id of this ResultIdAccountingResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResultIdAccountingResponse.

        The ID of created entity.  # noqa: E501

        :param id: The id of this ResultIdAccountingResponse.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, ResultIdAccountingResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResultIdAccountingResponse):
            return True

        return self.to_dict() != other.to_dict()
