# coding: utf-8

"""
    Files

    Upload and manage files.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.files.files.configuration import Configuration


class ErrorCategory(object):
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
    openapi_types = {"http_status": "str", "name": "str"}

    attribute_map = {"http_status": "httpStatus", "name": "name"}

    def __init__(self, http_status=None, name=None, local_vars_configuration=None):  # noqa: E501
        """ErrorCategory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._http_status = None
        self._name = None
        self.discriminator = None

        self.http_status = http_status
        self.name = name

    @property
    def http_status(self):
        """Gets the http_status of this ErrorCategory.  # noqa: E501


        :return: The http_status of this ErrorCategory.  # noqa: E501
        :rtype: str
        """
        return self._http_status

    @http_status.setter
    def http_status(self, http_status):
        """Sets the http_status of this ErrorCategory.


        :param http_status: The http_status of this ErrorCategory.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and http_status is None:  # noqa: E501
            raise ValueError("Invalid value for `http_status`, must not be `None`")  # noqa: E501
        allowed_values = [
            "CONTINUE",
            "SWITCHING_PROTOCOLS",
            "PROCESSING",
            "OK",
            "CREATED",
            "ACCEPTED",
            "NON_AUTHORITATIVE_INFORMATION",
            "NO_CONTENT",
            "RESET_CONTENT",
            "PARTIAL_CONTENT",
            "MULTI_STATUS",
            "ALREADY_REPORTED",
            "IM_USED",
            "MULTIPLE_CHOICES",
            "MOVED_PERMANENTLY",
            "FOUND",
            "SEE_OTHER",
            "NOT_MODIFIED",
            "USE_PROXY",
            "TEMPORARY_REDIRECT",
            "PERMANENT_REDIRECT",
            "BAD_REQUEST",
            "UNAUTHORIZED",
            "PAYMENT_REQUIRED",
            "FORBIDDEN",
            "NOT_FOUND",
            "METHOD_NOT_ALLOWED",
            "NOT_ACCEPTABLE",
            "PROXY_AUTHENTICATION_REQUIRED",
            "REQUEST_TIMEOUT",
            "CONFLICT",
            "GONE",
            "LENGTH_REQUIRED",
            "PRECONDITION_FAILED",
            "REQUEST_ENTITY_TOO_LARGE",
            "REQUEST_URI_TOO_LONG",
            "UNSUPPORTED_MEDIA_TYPE",
            "REQUESTED_RANGE_NOT_SATISFIABLE",
            "EXPECTATION_FAILED",
            "IM_A_TEAPOT",
            "MISDIRECTED_REQUEST",
            "UNPROCESSABLE_ENTITY",
            "LOCKED",
            "FAILED_DEPENDENCY",
            "UPGRADE_REQUIRED",
            "PRECONDITION_REQUIRED",
            "TOO_MANY_REQUESTS",
            "REQUEST_HEADERS_FIELDS_TOO_LARGE",
            "INTERNAL_STALE_SERVICE_DISCOVERY",
            "UNAVAILABLE_FOR_LEGAL_REASONS",
            "INTERNAL_SERVER_ERROR",
            "NOT_IMPLEMENTED",
            "BAD_GATEWAY",
            "SERVICE_UNAVAILABLE",
            "GATEWAY_TIMEOUT",
            "HTTP_VERSION_NOT_SUPPORTED",
            "VARIANT_ALSO_NEGOTIATES",
            "INSUFFICIENT_STORAGE",
            "LOOP_DETECTED",
            "NOT_EXTENDED",
            "NETWORK_AUTHENTICATION_REQUIRED",
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and http_status not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `http_status` ({0}), must be one of {1}".format(http_status, allowed_values))  # noqa: E501

        self._http_status = http_status

    @property
    def name(self):
        """Gets the name of this ErrorCategory.  # noqa: E501


        :return: The name of this ErrorCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ErrorCategory.


        :param name: The name of this ErrorCategory.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
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
        if not isinstance(other, ErrorCategory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorCategory):
            return True

        return self.to_dict() != other.to_dict()
