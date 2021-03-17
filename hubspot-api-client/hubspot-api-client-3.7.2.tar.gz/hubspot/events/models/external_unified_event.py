# coding: utf-8

"""
    HubSpot Events API

    API for accessing CRM object events.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.events.configuration import Configuration


class ExternalUnifiedEvent(object):
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
        "object_type": "str",
        "object_id": "str",
        "event_type": "str",
        "occurred_at": "datetime",
        "id": "str",
        "properties": "dict(str, str)",
    }

    attribute_map = {
        "object_type": "objectType",
        "object_id": "objectId",
        "event_type": "eventType",
        "occurred_at": "occurredAt",
        "id": "id",
        "properties": "properties",
    }

    def __init__(
        self,
        object_type=None,
        object_id=None,
        event_type=None,
        occurred_at=None,
        id=None,
        properties=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """ExternalUnifiedEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._object_type = None
        self._object_id = None
        self._event_type = None
        self._occurred_at = None
        self._id = None
        self._properties = None
        self.discriminator = None

        self.object_type = object_type
        self.object_id = object_id
        self.event_type = event_type
        self.occurred_at = occurred_at
        self.id = id
        self.properties = properties

    @property
    def object_type(self):
        """Gets the object_type of this ExternalUnifiedEvent.  # noqa: E501

        The objectType for the object which did the event.  # noqa: E501

        :return: The object_type of this ExternalUnifiedEvent.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ExternalUnifiedEvent.

        The objectType for the object which did the event.  # noqa: E501

        :param object_type: The object_type of this ExternalUnifiedEvent.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and object_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `object_type`, must not be `None`"
            )  # noqa: E501

        self._object_type = object_type

    @property
    def object_id(self):
        """Gets the object_id of this ExternalUnifiedEvent.  # noqa: E501

        The objectId of the object which did the event.  # noqa: E501

        :return: The object_id of this ExternalUnifiedEvent.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this ExternalUnifiedEvent.

        The objectId of the object which did the event.  # noqa: E501

        :param object_id: The object_id of this ExternalUnifiedEvent.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and object_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `object_id`, must not be `None`"
            )  # noqa: E501

        self._object_id = object_id

    @property
    def event_type(self):
        """Gets the event_type of this ExternalUnifiedEvent.  # noqa: E501

        The format of the `eventType` string is `ae{appId}_{eventTypeLabel}`, `pe{portalId}_{eventTypeLabel}`, or just `e_{eventTypeLabel}` for HubSpot events.  # noqa: E501

        :return: The event_type of this ExternalUnifiedEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ExternalUnifiedEvent.

        The format of the `eventType` string is `ae{appId}_{eventTypeLabel}`, `pe{portalId}_{eventTypeLabel}`, or just `e_{eventTypeLabel}` for HubSpot events.  # noqa: E501

        :param event_type: The event_type of this ExternalUnifiedEvent.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and event_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `event_type`, must not be `None`"
            )  # noqa: E501

        self._event_type = event_type

    @property
    def occurred_at(self):
        """Gets the occurred_at of this ExternalUnifiedEvent.  # noqa: E501

        An ISO 8601 timestamp when the event occurred.  # noqa: E501

        :return: The occurred_at of this ExternalUnifiedEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._occurred_at

    @occurred_at.setter
    def occurred_at(self, occurred_at):
        """Sets the occurred_at of this ExternalUnifiedEvent.

        An ISO 8601 timestamp when the event occurred.  # noqa: E501

        :param occurred_at: The occurred_at of this ExternalUnifiedEvent.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation and occurred_at is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `occurred_at`, must not be `None`"
            )  # noqa: E501

        self._occurred_at = occurred_at

    @property
    def id(self):
        """Gets the id of this ExternalUnifiedEvent.  # noqa: E501

        A unique identifier for the event.  # noqa: E501

        :return: The id of this ExternalUnifiedEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalUnifiedEvent.

        A unique identifier for the event.  # noqa: E501

        :param id: The id of this ExternalUnifiedEvent.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def properties(self):
        """Gets the properties of this ExternalUnifiedEvent.  # noqa: E501


        :return: The properties of this ExternalUnifiedEvent.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ExternalUnifiedEvent.


        :param properties: The properties of this ExternalUnifiedEvent.  # noqa: E501
        :type: dict(str, str)
        """
        if (
            self.local_vars_configuration.client_side_validation and properties is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `properties`, must not be `None`"
            )  # noqa: E501

        self._properties = properties

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
        if not isinstance(other, ExternalUnifiedEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalUnifiedEvent):
            return True

        return self.to_dict() != other.to_dict()
