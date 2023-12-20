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

class VerticalDatumInfo(object):
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
        'office': 'str',
        'unit': 'str',
        'location': 'str',
        'native_datum': 'str',
        'elevation': 'float',
        'offsets': 'list[Offset]'
    }

    attribute_map = {
        'office': 'office',
        'unit': 'unit',
        'location': 'location',
        'native_datum': 'native-datum',
        'elevation': 'elevation',
        'offsets': 'offsets'
    }

    def __init__(self, office=None, unit=None, location=None, native_datum=None, elevation=None, offsets=None):  # noqa: E501
        """VerticalDatumInfo - a model defined in Swagger"""  # noqa: E501
        self._office = None
        self._unit = None
        self._location = None
        self._native_datum = None
        self._elevation = None
        self._offsets = None
        self.discriminator = None
        if office is not None:
            self.office = office
        if unit is not None:
            self.unit = unit
        if location is not None:
            self.location = location
        if native_datum is not None:
            self.native_datum = native_datum
        if elevation is not None:
            self.elevation = elevation
        if offsets is not None:
            self.offsets = offsets

    @property
    def office(self):
        """Gets the office of this VerticalDatumInfo.  # noqa: E501


        :return: The office of this VerticalDatumInfo.  # noqa: E501
        :rtype: str
        """
        return self._office

    @office.setter
    def office(self, office):
        """Sets the office of this VerticalDatumInfo.


        :param office: The office of this VerticalDatumInfo.  # noqa: E501
        :type: str
        """

        self._office = office

    @property
    def unit(self):
        """Gets the unit of this VerticalDatumInfo.  # noqa: E501


        :return: The unit of this VerticalDatumInfo.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this VerticalDatumInfo.


        :param unit: The unit of this VerticalDatumInfo.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def location(self):
        """Gets the location of this VerticalDatumInfo.  # noqa: E501


        :return: The location of this VerticalDatumInfo.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this VerticalDatumInfo.


        :param location: The location of this VerticalDatumInfo.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def native_datum(self):
        """Gets the native_datum of this VerticalDatumInfo.  # noqa: E501


        :return: The native_datum of this VerticalDatumInfo.  # noqa: E501
        :rtype: str
        """
        return self._native_datum

    @native_datum.setter
    def native_datum(self, native_datum):
        """Sets the native_datum of this VerticalDatumInfo.


        :param native_datum: The native_datum of this VerticalDatumInfo.  # noqa: E501
        :type: str
        """

        self._native_datum = native_datum

    @property
    def elevation(self):
        """Gets the elevation of this VerticalDatumInfo.  # noqa: E501


        :return: The elevation of this VerticalDatumInfo.  # noqa: E501
        :rtype: float
        """
        return self._elevation

    @elevation.setter
    def elevation(self, elevation):
        """Sets the elevation of this VerticalDatumInfo.


        :param elevation: The elevation of this VerticalDatumInfo.  # noqa: E501
        :type: float
        """

        self._elevation = elevation

    @property
    def offsets(self):
        """Gets the offsets of this VerticalDatumInfo.  # noqa: E501


        :return: The offsets of this VerticalDatumInfo.  # noqa: E501
        :rtype: list[Offset]
        """
        return self._offsets

    @offsets.setter
    def offsets(self, offsets):
        """Sets the offsets of this VerticalDatumInfo.


        :param offsets: The offsets of this VerticalDatumInfo.  # noqa: E501
        :type: list[Offset]
        """

        self._offsets = offsets

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
        if issubclass(VerticalDatumInfo, dict):
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
        if not isinstance(other, VerticalDatumInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other