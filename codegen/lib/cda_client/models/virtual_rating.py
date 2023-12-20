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
from cda_client.models.abstract_rating_metadata import AbstractRatingMetadata  # noqa: F401,E501

class VirtualRating(AbstractRatingMetadata):
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
        'source_ratings': 'list[SourceRating]',
        'connections': 'str'
    }
    if hasattr(AbstractRatingMetadata, "swagger_types"):
        swagger_types.update(AbstractRatingMetadata.swagger_types)

    attribute_map = {
        'source_ratings': 'source-ratings',
        'connections': 'connections'
    }
    if hasattr(AbstractRatingMetadata, "attribute_map"):
        attribute_map.update(AbstractRatingMetadata.attribute_map)

    def __init__(self, source_ratings=None, connections=None, *args, **kwargs):  # noqa: E501
        """VirtualRating - a model defined in Swagger"""  # noqa: E501
        self._source_ratings = None
        self._connections = None
        self.discriminator = None
        if source_ratings is not None:
            self.source_ratings = source_ratings
        if connections is not None:
            self.connections = connections
        AbstractRatingMetadata.__init__(self, *args, **kwargs)

    @property
    def source_ratings(self):
        """Gets the source_ratings of this VirtualRating.  # noqa: E501


        :return: The source_ratings of this VirtualRating.  # noqa: E501
        :rtype: list[SourceRating]
        """
        return self._source_ratings

    @source_ratings.setter
    def source_ratings(self, source_ratings):
        """Sets the source_ratings of this VirtualRating.


        :param source_ratings: The source_ratings of this VirtualRating.  # noqa: E501
        :type: list[SourceRating]
        """

        self._source_ratings = source_ratings

    @property
    def connections(self):
        """Gets the connections of this VirtualRating.  # noqa: E501


        :return: The connections of this VirtualRating.  # noqa: E501
        :rtype: str
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this VirtualRating.


        :param connections: The connections of this VirtualRating.  # noqa: E501
        :type: str
        """

        self._connections = connections

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
        if issubclass(VirtualRating, dict):
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
        if not isinstance(other, VirtualRating):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other