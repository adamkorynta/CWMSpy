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

class TimeSeries(object):
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
        'begin': 'datetime',
        'end': 'datetime',
        'interval': 'TimeSeriesInterval',
        'interval_offset': 'int',
        'name': 'str',
        'next_page': 'str',
        'office_id': 'str',
        'page': 'str',
        'page_size': 'int',
        'time_zone': 'str',
        'total': 'int',
        'units': 'str',
        'value_columns': 'list[TimeSeriesColumn]',
        'values': 'list[list[object]]',
        'vertical_datum_info': 'VerticalDatumInfo'
    }

    attribute_map = {
        'begin': 'begin',
        'end': 'end',
        'interval': 'interval',
        'interval_offset': 'interval-offset',
        'name': 'name',
        'next_page': 'next-page',
        'office_id': 'office-id',
        'page': 'page',
        'page_size': 'page-size',
        'time_zone': 'time-zone',
        'total': 'total',
        'units': 'units',
        'value_columns': 'value-columns',
        'values': 'values',
        'vertical_datum_info': 'vertical-datum-info'
    }

    def __init__(self, begin=None, end=None, interval=None, interval_offset=None, name=None, next_page=None, office_id=None, page=None, page_size=None, time_zone=None, total=None, units=None, value_columns=None, values=None, vertical_datum_info=None):  # noqa: E501
        """TimeSeries - a model defined in Swagger"""  # noqa: E501
        self._begin = None
        self._end = None
        self._interval = None
        self._interval_offset = None
        self._name = None
        self._next_page = None
        self._office_id = None
        self._page = None
        self._page_size = None
        self._time_zone = None
        self._total = None
        self._units = None
        self._value_columns = None
        self._values = None
        self._vertical_datum_info = None
        self.discriminator = None
        if begin is not None:
            self.begin = begin
        if end is not None:
            self.end = end
        if interval is not None:
            self.interval = interval
        if interval_offset is not None:
            self.interval_offset = interval_offset
        if name is not None:
            self.name = name
        if next_page is not None:
            self.next_page = next_page
        if office_id is not None:
            self.office_id = office_id
        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if time_zone is not None:
            self.time_zone = time_zone
        if total is not None:
            self.total = total
        self.units = units
        if value_columns is not None:
            self.value_columns = value_columns
        if values is not None:
            self.values = values
        if vertical_datum_info is not None:
            self.vertical_datum_info = vertical_datum_info

    @property
    def begin(self):
        """Gets the begin of this TimeSeries.  # noqa: E501

        The requested start time of the data, in ISO-8601 format with offset and timezone ('yyyy-MM-dd'T'HH:mm:ssZ'['VV']'')  # noqa: E501

        :return: The begin of this TimeSeries.  # noqa: E501
        :rtype: datetime
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this TimeSeries.

        The requested start time of the data, in ISO-8601 format with offset and timezone ('yyyy-MM-dd'T'HH:mm:ssZ'['VV']'')  # noqa: E501

        :param begin: The begin of this TimeSeries.  # noqa: E501
        :type: datetime
        """

        self._begin = begin

    @property
    def end(self):
        """Gets the end of this TimeSeries.  # noqa: E501

        The requested end time of the data, in ISO-8601 format with offset and timezone ('yyyy-MM-dd'T'HH:mm:ssZ'['VV']'')  # noqa: E501

        :return: The end of this TimeSeries.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this TimeSeries.

        The requested end time of the data, in ISO-8601 format with offset and timezone ('yyyy-MM-dd'T'HH:mm:ssZ'['VV']'')  # noqa: E501

        :param end: The end of this TimeSeries.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def interval(self):
        """Gets the interval of this TimeSeries.  # noqa: E501


        :return: The interval of this TimeSeries.  # noqa: E501
        :rtype: TimeSeriesInterval
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this TimeSeries.


        :param interval: The interval of this TimeSeries.  # noqa: E501
        :type: TimeSeriesInterval
        """

        self._interval = interval

    @property
    def interval_offset(self):
        """Gets the interval_offset of this TimeSeries.  # noqa: E501

        Offset from top of interval  # noqa: E501

        :return: The interval_offset of this TimeSeries.  # noqa: E501
        :rtype: int
        """
        return self._interval_offset

    @interval_offset.setter
    def interval_offset(self, interval_offset):
        """Sets the interval_offset of this TimeSeries.

        Offset from top of interval  # noqa: E501

        :param interval_offset: The interval_offset of this TimeSeries.  # noqa: E501
        :type: int
        """

        self._interval_offset = interval_offset

    @property
    def name(self):
        """Gets the name of this TimeSeries.  # noqa: E501

        Time-series name  # noqa: E501

        :return: The name of this TimeSeries.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TimeSeries.

        Time-series name  # noqa: E501

        :param name: The name of this TimeSeries.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def next_page(self):
        """Gets the next_page of this TimeSeries.  # noqa: E501

        The cursor to the next page of data; null if there is no more data  # noqa: E501

        :return: The next_page of this TimeSeries.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this TimeSeries.

        The cursor to the next page of data; null if there is no more data  # noqa: E501

        :param next_page: The next_page of this TimeSeries.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def office_id(self):
        """Gets the office_id of this TimeSeries.  # noqa: E501

        Office ID that owns the time-series  # noqa: E501

        :return: The office_id of this TimeSeries.  # noqa: E501
        :rtype: str
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this TimeSeries.

        Office ID that owns the time-series  # noqa: E501

        :param office_id: The office_id of this TimeSeries.  # noqa: E501
        :type: str
        """

        self._office_id = office_id

    @property
    def page(self):
        """Gets the page of this TimeSeries.  # noqa: E501

        The cursor to the current page of data  # noqa: E501

        :return: The page of this TimeSeries.  # noqa: E501
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this TimeSeries.

        The cursor to the current page of data  # noqa: E501

        :param page: The page of this TimeSeries.  # noqa: E501
        :type: str
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this TimeSeries.  # noqa: E501

        The number of records fetched per-page; this may be larger than the number of records actually retrieved  # noqa: E501

        :return: The page_size of this TimeSeries.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this TimeSeries.

        The number of records fetched per-page; this may be larger than the number of records actually retrieved  # noqa: E501

        :param page_size: The page_size of this TimeSeries.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def time_zone(self):
        """Gets the time_zone of this TimeSeries.  # noqa: E501

        Only on 21.1.1 Database. The timezone the Interval Offset is from.  # noqa: E501

        :return: The time_zone of this TimeSeries.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this TimeSeries.

        Only on 21.1.1 Database. The timezone the Interval Offset is from.  # noqa: E501

        :param time_zone: The time_zone of this TimeSeries.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def total(self):
        """Gets the total of this TimeSeries.  # noqa: E501

        The total number of records retrieved; null or not present if not supported or unknown  # noqa: E501

        :return: The total of this TimeSeries.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TimeSeries.

        The total number of records retrieved; null or not present if not supported or unknown  # noqa: E501

        :param total: The total of this TimeSeries.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def units(self):
        """Gets the units of this TimeSeries.  # noqa: E501

        The units of the time series data  # noqa: E501

        :return: The units of this TimeSeries.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this TimeSeries.

        The units of the time series data  # noqa: E501

        :param units: The units of this TimeSeries.  # noqa: E501
        :type: str
        """
        if units is None:
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501

        self._units = units

    @property
    def value_columns(self):
        """Gets the value_columns of this TimeSeries.  # noqa: E501


        :return: The value_columns of this TimeSeries.  # noqa: E501
        :rtype: list[TimeSeriesColumn]
        """
        return self._value_columns

    @value_columns.setter
    def value_columns(self, value_columns):
        """Sets the value_columns of this TimeSeries.


        :param value_columns: The value_columns of this TimeSeries.  # noqa: E501
        :type: list[TimeSeriesColumn]
        """

        self._value_columns = value_columns

    @property
    def values(self):
        """Gets the values of this TimeSeries.  # noqa: E501


        :return: The values of this TimeSeries.  # noqa: E501
        :rtype: list[list[object]]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this TimeSeries.


        :param values: The values of this TimeSeries.  # noqa: E501
        :type: list[list[object]]
        """

        self._values = values

    @property
    def vertical_datum_info(self):
        """Gets the vertical_datum_info of this TimeSeries.  # noqa: E501


        :return: The vertical_datum_info of this TimeSeries.  # noqa: E501
        :rtype: VerticalDatumInfo
        """
        return self._vertical_datum_info

    @vertical_datum_info.setter
    def vertical_datum_info(self, vertical_datum_info):
        """Sets the vertical_datum_info of this TimeSeries.


        :param vertical_datum_info: The vertical_datum_info of this TimeSeries.  # noqa: E501
        :type: VerticalDatumInfo
        """

        self._vertical_datum_info = vertical_datum_info

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
        if issubclass(TimeSeries, dict):
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
        if not isinstance(other, TimeSeries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other