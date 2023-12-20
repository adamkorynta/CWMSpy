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

class LocationLevels(object):
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
        'page': 'str',
        'total': 'int',
        'levels': 'list[LocationLevel]',
        'next_page': 'str',
        'page_size': 'int'
    }

    attribute_map = {
        'page': 'page',
        'total': 'total',
        'levels': 'levels',
        'next_page': 'next-page',
        'page_size': 'page-size'
    }

    def __init__(self, page=None, total=None, levels=None, next_page=None, page_size=None):  # noqa: E501
        """LocationLevels - a model defined in Swagger"""  # noqa: E501
        self._page = None
        self._total = None
        self._levels = None
        self._next_page = None
        self._page_size = None
        self.discriminator = None
        if page is not None:
            self.page = page
        if total is not None:
            self.total = total
        if levels is not None:
            self.levels = levels
        if next_page is not None:
            self.next_page = next_page
        if page_size is not None:
            self.page_size = page_size

    @property
    def page(self):
        """Gets the page of this LocationLevels.  # noqa: E501

        The cursor to the current page of data  # noqa: E501

        :return: The page of this LocationLevels.  # noqa: E501
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this LocationLevels.

        The cursor to the current page of data  # noqa: E501

        :param page: The page of this LocationLevels.  # noqa: E501
        :type: str
        """

        self._page = page

    @property
    def total(self):
        """Gets the total of this LocationLevels.  # noqa: E501

        The total number of records retrieved; null or not present if not supported or unknown  # noqa: E501

        :return: The total of this LocationLevels.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this LocationLevels.

        The total number of records retrieved; null or not present if not supported or unknown  # noqa: E501

        :param total: The total of this LocationLevels.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def levels(self):
        """Gets the levels of this LocationLevels.  # noqa: E501

        List of retrieved location levels  # noqa: E501

        :return: The levels of this LocationLevels.  # noqa: E501
        :rtype: list[LocationLevel]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        """Sets the levels of this LocationLevels.

        List of retrieved location levels  # noqa: E501

        :param levels: The levels of this LocationLevels.  # noqa: E501
        :type: list[LocationLevel]
        """

        self._levels = levels

    @property
    def next_page(self):
        """Gets the next_page of this LocationLevels.  # noqa: E501

        The cursor to the next page of data; null if there is no more data  # noqa: E501

        :return: The next_page of this LocationLevels.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this LocationLevels.

        The cursor to the next page of data; null if there is no more data  # noqa: E501

        :param next_page: The next_page of this LocationLevels.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def page_size(self):
        """Gets the page_size of this LocationLevels.  # noqa: E501

        The number of records fetched per-page; this may be larger than the number of records actually retrieved  # noqa: E501

        :return: The page_size of this LocationLevels.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this LocationLevels.

        The number of records fetched per-page; this may be larger than the number of records actually retrieved  # noqa: E501

        :param page_size: The page_size of this LocationLevels.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if issubclass(LocationLevels, dict):
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
        if not isinstance(other, LocationLevels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
