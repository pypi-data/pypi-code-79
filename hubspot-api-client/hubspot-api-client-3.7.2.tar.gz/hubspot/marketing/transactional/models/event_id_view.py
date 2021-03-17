# coding: utf-8

"""
    Transactional Email

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.marketing.transactional.configuration import Configuration


class EventIdView(object):
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
    openapi_types = {"created": "datetime", "id": "str"}

    attribute_map = {"created": "created", "id": "id"}

    def __init__(
        self, created=None, id=None, local_vars_configuration=None
    ):  # noqa: E501
        """EventIdView - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created = None
        self._id = None
        self.discriminator = None

        self.created = created
        self.id = id

    @property
    def created(self):
        """Gets the created of this EventIdView.  # noqa: E501

        Time of event creation.  # noqa: E501

        :return: The created of this EventIdView.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EventIdView.

        Time of event creation.  # noqa: E501

        :param created: The created of this EventIdView.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation and created is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `created`, must not be `None`"
            )  # noqa: E501

        self._created = created

    @property
    def id(self):
        """Gets the id of this EventIdView.  # noqa: E501

        Identifier of event.  # noqa: E501

        :return: The id of this EventIdView.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EventIdView.

        Identifier of event.  # noqa: E501

        :param id: The id of this EventIdView.  # noqa: E501
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
        if not isinstance(other, EventIdView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventIdView):
            return True

        return self.to_dict() != other.to_dict()
