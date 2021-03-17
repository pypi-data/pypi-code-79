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


class ResponseMyUser(object):
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
        'display_name': 'str',
        'edges': 'ModelUserEdges',
        'email': 'str',
        'github_authorized': 'bool',
        'has_password': 'bool',
        'id': 'int',
        'immutable_slug': 'str',
        'is_email_verified': 'bool',
        'last_login': 'datetime',
        'updated_dt': 'datetime',
        'username': 'str',
        'workspaces': 'list[ResponseWorkspace]'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'display_name': 'display_name',
        'edges': 'edges',
        'email': 'email',
        'github_authorized': 'github_authorized',
        'has_password': 'has_password',
        'id': 'id',
        'immutable_slug': 'immutable_slug',
        'is_email_verified': 'is_email_verified',
        'last_login': 'last_login',
        'updated_dt': 'updated_dt',
        'username': 'username',
        'workspaces': 'workspaces'
    }

    def __init__(self, created_dt=None, display_name=None, edges=None, email=None, github_authorized=None, has_password=None, id=None, immutable_slug=None, is_email_verified=None, last_login=None, updated_dt=None, username=None, workspaces=None, local_vars_configuration=None):  # noqa: E501
        """ResponseMyUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._display_name = None
        self._edges = None
        self._email = None
        self._github_authorized = None
        self._has_password = None
        self._id = None
        self._immutable_slug = None
        self._is_email_verified = None
        self._last_login = None
        self._updated_dt = None
        self._username = None
        self._workspaces = None
        self.discriminator = None

        self.created_dt = created_dt
        if display_name is not None:
            self.display_name = display_name
        if edges is not None:
            self.edges = edges
        if email is not None:
            self.email = email
        self.github_authorized = github_authorized
        self.has_password = has_password
        if id is not None:
            self.id = id
        if immutable_slug is not None:
            self.immutable_slug = immutable_slug
        if is_email_verified is not None:
            self.is_email_verified = is_email_verified
        self.last_login = last_login
        self.updated_dt = updated_dt
        if username is not None:
            self.username = username
        self.workspaces = workspaces

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseMyUser.  # noqa: E501


        :return: The created_dt of this ResponseMyUser.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseMyUser.


        :param created_dt: The created_dt of this ResponseMyUser.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def display_name(self):
        """Gets the display_name of this ResponseMyUser.  # noqa: E501


        :return: The display_name of this ResponseMyUser.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ResponseMyUser.


        :param display_name: The display_name of this ResponseMyUser.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def edges(self):
        """Gets the edges of this ResponseMyUser.  # noqa: E501


        :return: The edges of this ResponseMyUser.  # noqa: E501
        :rtype: ModelUserEdges
        """
        return self._edges

    @edges.setter
    def edges(self, edges):
        """Sets the edges of this ResponseMyUser.


        :param edges: The edges of this ResponseMyUser.  # noqa: E501
        :type edges: ModelUserEdges
        """

        self._edges = edges

    @property
    def email(self):
        """Gets the email of this ResponseMyUser.  # noqa: E501


        :return: The email of this ResponseMyUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ResponseMyUser.


        :param email: The email of this ResponseMyUser.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def github_authorized(self):
        """Gets the github_authorized of this ResponseMyUser.  # noqa: E501


        :return: The github_authorized of this ResponseMyUser.  # noqa: E501
        :rtype: bool
        """
        return self._github_authorized

    @github_authorized.setter
    def github_authorized(self, github_authorized):
        """Sets the github_authorized of this ResponseMyUser.


        :param github_authorized: The github_authorized of this ResponseMyUser.  # noqa: E501
        :type github_authorized: bool
        """
        if self.local_vars_configuration.client_side_validation and github_authorized is None:  # noqa: E501
            raise ValueError("Invalid value for `github_authorized`, must not be `None`")  # noqa: E501

        self._github_authorized = github_authorized

    @property
    def has_password(self):
        """Gets the has_password of this ResponseMyUser.  # noqa: E501


        :return: The has_password of this ResponseMyUser.  # noqa: E501
        :rtype: bool
        """
        return self._has_password

    @has_password.setter
    def has_password(self, has_password):
        """Sets the has_password of this ResponseMyUser.


        :param has_password: The has_password of this ResponseMyUser.  # noqa: E501
        :type has_password: bool
        """
        if self.local_vars_configuration.client_side_validation and has_password is None:  # noqa: E501
            raise ValueError("Invalid value for `has_password`, must not be `None`")  # noqa: E501

        self._has_password = has_password

    @property
    def id(self):
        """Gets the id of this ResponseMyUser.  # noqa: E501


        :return: The id of this ResponseMyUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseMyUser.


        :param id: The id of this ResponseMyUser.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def immutable_slug(self):
        """Gets the immutable_slug of this ResponseMyUser.  # noqa: E501


        :return: The immutable_slug of this ResponseMyUser.  # noqa: E501
        :rtype: str
        """
        return self._immutable_slug

    @immutable_slug.setter
    def immutable_slug(self, immutable_slug):
        """Sets the immutable_slug of this ResponseMyUser.


        :param immutable_slug: The immutable_slug of this ResponseMyUser.  # noqa: E501
        :type immutable_slug: str
        """

        self._immutable_slug = immutable_slug

    @property
    def is_email_verified(self):
        """Gets the is_email_verified of this ResponseMyUser.  # noqa: E501


        :return: The is_email_verified of this ResponseMyUser.  # noqa: E501
        :rtype: bool
        """
        return self._is_email_verified

    @is_email_verified.setter
    def is_email_verified(self, is_email_verified):
        """Sets the is_email_verified of this ResponseMyUser.


        :param is_email_verified: The is_email_verified of this ResponseMyUser.  # noqa: E501
        :type is_email_verified: bool
        """

        self._is_email_verified = is_email_verified

    @property
    def last_login(self):
        """Gets the last_login of this ResponseMyUser.  # noqa: E501


        :return: The last_login of this ResponseMyUser.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this ResponseMyUser.


        :param last_login: The last_login of this ResponseMyUser.  # noqa: E501
        :type last_login: datetime
        """

        self._last_login = last_login

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseMyUser.  # noqa: E501


        :return: The updated_dt of this ResponseMyUser.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseMyUser.


        :param updated_dt: The updated_dt of this ResponseMyUser.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def username(self):
        """Gets the username of this ResponseMyUser.  # noqa: E501


        :return: The username of this ResponseMyUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ResponseMyUser.


        :param username: The username of this ResponseMyUser.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def workspaces(self):
        """Gets the workspaces of this ResponseMyUser.  # noqa: E501


        :return: The workspaces of this ResponseMyUser.  # noqa: E501
        :rtype: list[ResponseWorkspace]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        """Sets the workspaces of this ResponseMyUser.


        :param workspaces: The workspaces of this ResponseMyUser.  # noqa: E501
        :type workspaces: list[ResponseWorkspace]
        """
        if self.local_vars_configuration.client_side_validation and workspaces is None:  # noqa: E501
            raise ValueError("Invalid value for `workspaces`, must not be `None`")  # noqa: E501

        self._workspaces = workspaces

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
        if not isinstance(other, ResponseMyUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseMyUser):
            return True

        return self.to_dict() != other.to_dict()
