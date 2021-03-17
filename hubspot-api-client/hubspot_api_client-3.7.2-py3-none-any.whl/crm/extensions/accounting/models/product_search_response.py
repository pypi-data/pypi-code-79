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


class ProductSearchResponse(object):
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
    openapi_types = {"result": "str", "products": "list[Product]"}

    attribute_map = {"result": "@result", "products": "products"}

    def __init__(
        self, result=None, products=None, local_vars_configuration=None
    ):  # noqa: E501
        """ProductSearchResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._products = None
        self.discriminator = None

        if result is not None:
            self.result = result
        self.products = products

    @property
    def result(self):
        """Gets the result of this ProductSearchResponse.  # noqa: E501

        Designates if the response is a success ('OK') or failure ('ERR').  # noqa: E501

        :return: The result of this ProductSearchResponse.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ProductSearchResponse.

        Designates if the response is a success ('OK') or failure ('ERR').  # noqa: E501

        :param result: The result of this ProductSearchResponse.  # noqa: E501
        :type: str
        """
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
    def products(self):
        """Gets the products of this ProductSearchResponse.  # noqa: E501

        The list of products that matched the search criteria.  # noqa: E501

        :return: The products of this ProductSearchResponse.  # noqa: E501
        :rtype: list[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this ProductSearchResponse.

        The list of products that matched the search criteria.  # noqa: E501

        :param products: The products of this ProductSearchResponse.  # noqa: E501
        :type: list[Product]
        """
        if (
            self.local_vars_configuration.client_side_validation and products is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `products`, must not be `None`"
            )  # noqa: E501

        self._products = products

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
        if not isinstance(other, ProductSearchResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductSearchResponse):
            return True

        return self.to_dict() != other.to_dict()
