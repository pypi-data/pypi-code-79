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


class ResponseKernelCluster(object):
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
        'id': 'int',
        'immutable_slug': 'str',
        'is_savvihub_managed': 'bool',
        'name': 'str',
        'provider': 'str',
        'region': 'str',
        'updated_dt': 'datetime',
        'workspace_id': 'int'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'id': 'id',
        'immutable_slug': 'immutable_slug',
        'is_savvihub_managed': 'is_savvihub_managed',
        'name': 'name',
        'provider': 'provider',
        'region': 'region',
        'updated_dt': 'updated_dt',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, created_dt=None, id=None, immutable_slug=None, is_savvihub_managed=None, name=None, provider=None, region=None, updated_dt=None, workspace_id=None, local_vars_configuration=None):  # noqa: E501
        """ResponseKernelCluster - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._id = None
        self._immutable_slug = None
        self._is_savvihub_managed = None
        self._name = None
        self._provider = None
        self._region = None
        self._updated_dt = None
        self._workspace_id = None
        self.discriminator = None

        self.created_dt = created_dt
        self.id = id
        self.immutable_slug = immutable_slug
        self.is_savvihub_managed = is_savvihub_managed
        self.name = name
        self.provider = provider
        self.region = region
        self.updated_dt = updated_dt
        self.workspace_id = workspace_id

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseKernelCluster.  # noqa: E501


        :return: The created_dt of this ResponseKernelCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseKernelCluster.


        :param created_dt: The created_dt of this ResponseKernelCluster.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def id(self):
        """Gets the id of this ResponseKernelCluster.  # noqa: E501


        :return: The id of this ResponseKernelCluster.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseKernelCluster.


        :param id: The id of this ResponseKernelCluster.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this ResponseKernelCluster.  # noqa: E501


        :return: The immutable_slug of this ResponseKernelCluster.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this ResponseKernelCluster.


        :param immutable_slug: The immutable_slug of this ResponseKernelCluster.  # noqa: E501
        :type immutable_slug: str
        """
        if self.local_vars_configuration.client_side_validation and immutable_slug is None:  # noqa: E501
            raise ValueError("Invalid value for `immutable_slug`, must not be `None`")  # noqa: E501

        self._immutable_slug = immutable_slug

    @property
    def is_savvihub_managed(self):
        """Gets the is_savvihub_managed of this ResponseKernelCluster.  # noqa: E501


        :return: The is_savvihub_managed of this ResponseKernelCluster.  # noqa: E501
        :rtype: bool
        """
        return self._is_savvihub_managed

    @is_savvihub_managed.setter
    def is_savvihub_managed(self, is_savvihub_managed):
        """Sets the is_savvihub_managed of this ResponseKernelCluster.


        :param is_savvihub_managed: The is_savvihub_managed of this ResponseKernelCluster.  # noqa: E501
        :type is_savvihub_managed: bool
        """
        if self.local_vars_configuration.client_side_validation and is_savvihub_managed is None:  # noqa: E501
            raise ValueError("Invalid value for `is_savvihub_managed`, must not be `None`")  # noqa: E501

        self._is_savvihub_managed = is_savvihub_managed

    @property
    def name(self):
        """Gets the name of this ResponseKernelCluster.  # noqa: E501


        :return: The name of this ResponseKernelCluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseKernelCluster.


        :param name: The name of this ResponseKernelCluster.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this ResponseKernelCluster.  # noqa: E501


        :return: The provider of this ResponseKernelCluster.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ResponseKernelCluster.


        :param provider: The provider of this ResponseKernelCluster.  # noqa: E501
        :type provider: str
        """
        if self.local_vars_configuration.client_side_validation and provider is None:  # noqa: E501
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider

    @property
    def region(self):
        """Gets the region of this ResponseKernelCluster.  # noqa: E501


        :return: The region of this ResponseKernelCluster.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ResponseKernelCluster.


        :param region: The region of this ResponseKernelCluster.  # noqa: E501
        :type region: str
        """

        self._region = region

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseKernelCluster.  # noqa: E501


        :return: The updated_dt of this ResponseKernelCluster.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseKernelCluster.


        :param updated_dt: The updated_dt of this ResponseKernelCluster.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ResponseKernelCluster.  # noqa: E501


        :return: The workspace_id of this ResponseKernelCluster.  # noqa: E501
        :rtype: int
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ResponseKernelCluster.


        :param workspace_id: The workspace_id of this ResponseKernelCluster.  # noqa: E501
        :type workspace_id: int
        """
        if self.local_vars_configuration.client_side_validation and workspace_id is None:  # noqa: E501
            raise ValueError("Invalid value for `workspace_id`, must not be `None`")  # noqa: E501

        self._workspace_id = workspace_id

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
        if not isinstance(other, ResponseKernelCluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseKernelCluster):
            return True

        return self.to_dict() != other.to_dict()
