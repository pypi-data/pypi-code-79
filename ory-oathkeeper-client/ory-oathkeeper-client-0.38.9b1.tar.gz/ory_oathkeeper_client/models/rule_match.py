# coding: utf-8

"""
    ORY Oathkeeper

    ORY Oathkeeper is a reverse proxy that checks the HTTP Authorization for validity against a set of rules. This service uses Hydra to validate access tokens and policies.  # noqa: E501

    The version of the OpenAPI document: v0.38.5-beta.1
    Contact: hi@ory.am
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_oathkeeper_client.configuration import Configuration


class RuleMatch(object):
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
        'methods': 'list[str]',
        'url': 'str'
    }

    attribute_map = {
        'methods': 'methods',
        'url': 'url'
    }

    def __init__(self, methods=None, url=None, local_vars_configuration=None):  # noqa: E501
        """RuleMatch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._methods = None
        self._url = None
        self.discriminator = None

        if methods is not None:
            self.methods = methods
        if url is not None:
            self.url = url

    @property
    def methods(self):
        """Gets the methods of this RuleMatch.  # noqa: E501

        An array of HTTP methods (e.g. GET, POST, PUT, DELETE, ...). When ORY Oathkeeper searches for rules to decide what to do with an incoming request to the proxy server, it compares the HTTP method of the incoming request with the HTTP methods of each rules. If a match is found, the rule is considered a partial match. If the matchesUrl field is satisfied as well, the rule is considered a full match.  # noqa: E501

        :return: The methods of this RuleMatch.  # noqa: E501
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this RuleMatch.

        An array of HTTP methods (e.g. GET, POST, PUT, DELETE, ...). When ORY Oathkeeper searches for rules to decide what to do with an incoming request to the proxy server, it compares the HTTP method of the incoming request with the HTTP methods of each rules. If a match is found, the rule is considered a partial match. If the matchesUrl field is satisfied as well, the rule is considered a full match.  # noqa: E501

        :param methods: The methods of this RuleMatch.  # noqa: E501
        :type: list[str]
        """

        self._methods = methods

    @property
    def url(self):
        """Gets the url of this RuleMatch.  # noqa: E501

        This field represents the URL pattern this rule matches. When ORY Oathkeeper searches for rules to decide what to do with an incoming request to the proxy server, it compares the full request URL (e.g. https://mydomain.com/api/resource) without query parameters of the incoming request with this field. If a match is found, the rule is considered a partial match. If the matchesMethods field is satisfied as well, the rule is considered a full match.  You can use regular expressions in this field to match more than one url. Regular expressions are encapsulated in brackets < and >. The following example matches all paths of the domain `mydomain.com`: `https://mydomain.com/<.*>`.  # noqa: E501

        :return: The url of this RuleMatch.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RuleMatch.

        This field represents the URL pattern this rule matches. When ORY Oathkeeper searches for rules to decide what to do with an incoming request to the proxy server, it compares the full request URL (e.g. https://mydomain.com/api/resource) without query parameters of the incoming request with this field. If a match is found, the rule is considered a partial match. If the matchesMethods field is satisfied as well, the rule is considered a full match.  You can use regular expressions in this field to match more than one url. Regular expressions are encapsulated in brackets < and >. The following example matches all paths of the domain `mydomain.com`: `https://mydomain.com/<.*>`.  # noqa: E501

        :param url: The url of this RuleMatch.  # noqa: E501
        :type: str
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, RuleMatch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuleMatch):
            return True

        return self.to_dict() != other.to_dict()
