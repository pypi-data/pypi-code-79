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


class ModelKernelImagePullSecret(object):
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
        'created_dt': 'datetime',
        'edges': 'ModelKernelImagePullSecretEdges',
        'id': 'int',
        'immutable_slug': 'str',
        'name': 'str',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'edges': 'edges',
        'id': 'id',
        'immutable_slug': 'immutable_slug',
        'name': 'name',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, created_dt=None, edges=None, id=None, immutable_slug=None, name=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """ModelKernelImagePullSecret - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._edges = None
        self._id = None
        self._immutable_slug = None
        self._name = None
        self._updated_dt = None
        self.discriminator = None

        self.created_dt = created_dt
        if edges is not None:
            self.edges = edges
        if id is not None:
            self.id = id
        if immutable_slug is not None:
            self.immutable_slug = immutable_slug
        if name is not None:
            self.name = name
        self.updated_dt = updated_dt

    @property
    def created_dt(self):
        """Gets the created_dt of this ModelKernelImagePullSecret.  # noqa: E501


        :return: The created_dt of this ModelKernelImagePullSecret.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ModelKernelImagePullSecret.


        :param created_dt: The created_dt of this ModelKernelImagePullSecret.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def edges(self):
        """Gets the edges of this ModelKernelImagePullSecret.  # noqa: E501


        :return: The edges of this ModelKernelImagePullSecret.  # noqa: E501
        :rtype: ModelKernelImagePullSecretEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this ModelKernelImagePullSecret.


        :param edges: The edges of this ModelKernelImagePullSecret.  # noqa: E501
        :type edges: ModelKernelImagePullSecretEdges
        """

        self._edges = edges

    @property
    def id(self):
        """Gets the id of this ModelKernelImagePullSecret.  # noqa: E501


        :return: The id of this ModelKernelImagePullSecret.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelKernelImagePullSecret.


        :param id: The id of this ModelKernelImagePullSecret.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this ModelKernelImagePullSecret.  # noqa: E501


        :return: The immutable_slug of this ModelKernelImagePullSecret.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this ModelKernelImagePullSecret.


        :param immutable_slug: The immutable_slug of this ModelKernelImagePullSecret.  # noqa: E501
        :type immutable_slug: str
        """

        self._immutable_slug = immutable_slug

    @property
    def name(self):
        """Gets the name of this ModelKernelImagePullSecret.  # noqa: E501


        :return: The name of this ModelKernelImagePullSecret.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelKernelImagePullSecret.


        :param name: The name of this ModelKernelImagePullSecret.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ModelKernelImagePullSecret.  # noqa: E501


        :return: The updated_dt of this ModelKernelImagePullSecret.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ModelKernelImagePullSecret.


        :param updated_dt: The updated_dt of this ModelKernelImagePullSecret.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

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
        if not isinstance(other, ModelKernelImagePullSecret):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelKernelImagePullSecret):
            return True

        return self.to_dict() != other.to_dict()
