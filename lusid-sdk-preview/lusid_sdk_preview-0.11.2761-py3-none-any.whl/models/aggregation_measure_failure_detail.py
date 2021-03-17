# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2761
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class AggregationMeasureFailureDetail(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'id': 'str',
        'effective_at': 'datetime',
        'measure': 'str',
        'reason': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'id': 'id',
        'effective_at': 'effectiveAt',
        'measure': 'measure',
        'reason': 'reason',
        'detail': 'detail'
    }

    required_map = {
        'id': 'optional',
        'effective_at': 'optional',
        'measure': 'optional',
        'reason': 'optional',
        'detail': 'optional'
    }

    def __init__(self, id=None, effective_at=None, measure=None, reason=None, detail=None):  # noqa: E501
        """
        AggregationMeasureFailureDetail - a model defined in OpenAPI

        :param id: 
        :type id: str
        :param effective_at: 
        :type effective_at: datetime
        :param measure: 
        :type measure: str
        :param reason: 
        :type reason: str
        :param detail: 
        :type detail: str

        """  # noqa: E501

        self._id = None
        self._effective_at = None
        self._measure = None
        self._reason = None
        self._detail = None
        self.discriminator = None

        self.id = id
        if effective_at is not None:
            self.effective_at = effective_at
        self.measure = measure
        self.reason = reason
        self.detail = detail

    @property
    def id(self):
        """Gets the id of this AggregationMeasureFailureDetail.  # noqa: E501


        :return: The id of this AggregationMeasureFailureDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AggregationMeasureFailureDetail.


        :param id: The id of this AggregationMeasureFailureDetail.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def effective_at(self):
        """Gets the effective_at of this AggregationMeasureFailureDetail.  # noqa: E501


        :return: The effective_at of this AggregationMeasureFailureDetail.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this AggregationMeasureFailureDetail.


        :param effective_at: The effective_at of this AggregationMeasureFailureDetail.  # noqa: E501
        :type: datetime
        """

        self._effective_at = effective_at

    @property
    def measure(self):
        """Gets the measure of this AggregationMeasureFailureDetail.  # noqa: E501


        :return: The measure of this AggregationMeasureFailureDetail.  # noqa: E501
        :rtype: str
        """
        return self._measure

    @measure.setter
    def measure(self, measure):
        """Sets the measure of this AggregationMeasureFailureDetail.


        :param measure: The measure of this AggregationMeasureFailureDetail.  # noqa: E501
        :type: str
        """

        self._measure = measure

    @property
    def reason(self):
        """Gets the reason of this AggregationMeasureFailureDetail.  # noqa: E501


        :return: The reason of this AggregationMeasureFailureDetail.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this AggregationMeasureFailureDetail.


        :param reason: The reason of this AggregationMeasureFailureDetail.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def detail(self):
        """Gets the detail of this AggregationMeasureFailureDetail.  # noqa: E501


        :return: The detail of this AggregationMeasureFailureDetail.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this AggregationMeasureFailureDetail.


        :param detail: The detail of this AggregationMeasureFailureDetail.  # noqa: E501
        :type: str
        """

        self._detail = detail

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
        if not isinstance(other, AggregationMeasureFailureDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
