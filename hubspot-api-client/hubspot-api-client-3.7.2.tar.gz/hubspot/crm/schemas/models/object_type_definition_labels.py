# coding: utf-8

"""
    Schemas

    The CRM uses schemas to define how custom objects should store and represent information in the HubSpot CRM. Schemas define details about an object's type, properties, and associations. The schema can be uniquely identified by its **object type ID**.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.schemas.configuration import Configuration


class ObjectTypeDefinitionLabels(object):
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
    openapi_types = {"singular": "str", "plural": "str"}

    attribute_map = {"singular": "singular", "plural": "plural"}

    def __init__(
        self, singular=None, plural=None, local_vars_configuration=None
    ):  # noqa: E501
        """ObjectTypeDefinitionLabels - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._singular = None
        self._plural = None
        self.discriminator = None

        if singular is not None:
            self.singular = singular
        if plural is not None:
            self.plural = plural

    @property
    def singular(self):
        """Gets the singular of this ObjectTypeDefinitionLabels.  # noqa: E501

        The word for one object. (There’s no way to change this later.)  # noqa: E501

        :return: The singular of this ObjectTypeDefinitionLabels.  # noqa: E501
        :rtype: str
        """
        return self._singular

    @singular.setter
    def singular(self, singular):
        """Sets the singular of this ObjectTypeDefinitionLabels.

        The word for one object. (There’s no way to change this later.)  # noqa: E501

        :param singular: The singular of this ObjectTypeDefinitionLabels.  # noqa: E501
        :type: str
        """

        self._singular = singular

    @property
    def plural(self):
        """Gets the plural of this ObjectTypeDefinitionLabels.  # noqa: E501

        The word for multiple objects. (There’s no way to change this later.)  # noqa: E501

        :return: The plural of this ObjectTypeDefinitionLabels.  # noqa: E501
        :rtype: str
        """
        return self._plural

    @plural.setter
    def plural(self, plural):
        """Sets the plural of this ObjectTypeDefinitionLabels.

        The word for multiple objects. (There’s no way to change this later.)  # noqa: E501

        :param plural: The plural of this ObjectTypeDefinitionLabels.  # noqa: E501
        :type: str
        """

        self._plural = plural

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
        if not isinstance(other, ObjectTypeDefinitionLabels):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectTypeDefinitionLabels):
            return True

        return self.to_dict() != other.to_dict()
