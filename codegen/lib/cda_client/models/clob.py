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

class Clob(object):
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
        'office_id': 'str',
        'id': 'str',
        'description': 'str',
        'value': 'str'
    }

    attribute_map = {
        'office_id': 'office-id',
        'id': 'id',
        'description': 'description',
        'value': 'value'
    }

    def __init__(self, office_id=None, id=None, description=None, value=None):  # noqa: E501
        """Clob - a model defined in Swagger"""  # noqa: E501
        self._office_id = None
        self._id = None
        self._description = None
        self._value = None
        self.discriminator = None
        self.office_id = office_id
        self.id = id
        if description is not None:
            self.description = description
        if value is not None:
            self.value = value

    @property
    def office_id(self):
        """Gets the office_id of this Clob.  # noqa: E501

        Owning office of object.  # noqa: E501

        :return: The office_id of this Clob.  # noqa: E501
        :rtype: str
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this Clob.

        Owning office of object.  # noqa: E501

        :param office_id: The office_id of this Clob.  # noqa: E501
        :type: str
        """
        if office_id is None:
            raise ValueError("Invalid value for `office_id`, must not be `None`")  # noqa: E501

        self._office_id = office_id

    @property
    def id(self):
        """Gets the id of this Clob.  # noqa: E501


        :return: The id of this Clob.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Clob.


        :param id: The id of this Clob.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def description(self):
        """Gets the description of this Clob.  # noqa: E501


        :return: The description of this Clob.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Clob.


        :param description: The description of this Clob.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def value(self):
        """Gets the value of this Clob.  # noqa: E501


        :return: The value of this Clob.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Clob.


        :param value: The value of this Clob.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(Clob, dict):
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
        if not isinstance(other, Clob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other