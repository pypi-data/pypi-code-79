# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class ExperimentExperimentListByProjectResponse(object):
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
        'page_info': 'ModelPageInfoWithCount',
        'results': 'list[ResponseExperimentInfo]'
    }

    attribute_map = {
        'page_info': 'page_info',
        'results': 'results'
    }

    def __init__(self, page_info=None, results=None, local_vars_configuration=None):  # noqa: E501
        """ExperimentExperimentListByProjectResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._page_info = None
        self._results = None
        self.discriminator = None

        self.page_info = page_info
        self.results = results

    @property
    def page_info(self):
        """Gets the page_info of this ExperimentExperimentListByProjectResponse.  # noqa: E501


        :return: The page_info of this ExperimentExperimentListByProjectResponse.  # noqa: E501
        :rtype: ModelPageInfoWithCount
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ExperimentExperimentListByProjectResponse.


        :param page_info: The page_info of this ExperimentExperimentListByProjectResponse.  # noqa: E501
        :type page_info: ModelPageInfoWithCount
        """
        if self.local_vars_configuration.client_side_validation and page_info is None:  # noqa: E501
            raise ValueError("Invalid value for `page_info`, must not be `None`")  # noqa: E501

        self._page_info = page_info

    @property
    def results(self):
        """Gets the results of this ExperimentExperimentListByProjectResponse.  # noqa: E501


        :return: The results of this ExperimentExperimentListByProjectResponse.  # noqa: E501
        :rtype: list[ResponseExperimentInfo]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ExperimentExperimentListByProjectResponse.


        :param results: The results of this ExperimentExperimentListByProjectResponse.  # noqa: E501
        :type results: list[ResponseExperimentInfo]
        """
        if self.local_vars_configuration.client_side_validation and results is None:  # noqa: E501
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExperimentExperimentListByProjectResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExperimentExperimentListByProjectResponse):
            return True

        return self.to_dict() != other.to_dict()
