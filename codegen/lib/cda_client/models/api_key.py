# coding: utf-8

"""
    CWMS Data API

    CWMS REST API for Data Retrieval  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ApiKey(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user_id': 'str',
        'key_name': 'str',
        'api_key': 'str',
        'created': 'datetime',
        'expires': 'datetime'
    }

    attribute_map = {
        'user_id': 'user-id',
        'key_name': 'key-name',
        'api_key': 'api-key',
        'created': 'created',
        'expires': 'expires'
    }

    def __init__(self, user_id=None, key_name=None, api_key=None, created=None, expires=None):  # noqa: E501
        """ApiKey - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._key_name = None
        self._api_key = None
        self._created = None
        self._expires = None
        self.discriminator = None
        self.user_id = user_id
        self.key_name = key_name
        if api_key is not None:
            self.api_key = api_key
        if created is not None:
            self.created = created
        if expires is not None:
            self.expires = expires

    @property
    def user_id(self):
        """Gets the user_id of this ApiKey.  # noqa: E501


        :return: The user_id of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ApiKey.


        :param user_id: The user_id of this ApiKey.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def key_name(self):
        """Gets the key_name of this ApiKey.  # noqa: E501


        :return: The key_name of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this ApiKey.


        :param key_name: The key_name of this ApiKey.  # noqa: E501
        :type: str
        """
        if key_name is None:
            raise ValueError("Invalid value for `key_name`, must not be `None`")  # noqa: E501

        self._key_name = key_name

    @property
    def api_key(self):
        """Gets the api_key of this ApiKey.  # noqa: E501


        :return: The api_key of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this ApiKey.


        :param api_key: The api_key of this ApiKey.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def created(self):
        """Gets the created of this ApiKey.  # noqa: E501

        The instant this Key was created, in ISO-8601 format with offset and timezone ('yyyy-MM-dd'T'HH:mm:ssZ'['VV']'')  # noqa: E501

        :return: The created of this ApiKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ApiKey.

        The instant this Key was created, in ISO-8601 format with offset and timezone ('yyyy-MM-dd'T'HH:mm:ssZ'['VV']'')  # noqa: E501

        :param created: The created of this ApiKey.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def expires(self):
        """Gets the expires of this ApiKey.  # noqa: E501

        When this key expires, in ISO-8601 format with offset and timezone ('yyyy-MM-dd'T'HH:mm:ssZ'['VV']'')  # noqa: E501

        :return: The expires of this ApiKey.  # noqa: E501
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this ApiKey.

        When this key expires, in ISO-8601 format with offset and timezone ('yyyy-MM-dd'T'HH:mm:ssZ'['VV']'')  # noqa: E501

        :param expires: The expires of this ApiKey.  # noqa: E501
        :type: datetime
        """

        self._expires = expires

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ApiKey, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
