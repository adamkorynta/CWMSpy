# coding: utf-8

"""
    CWMS Data API

    CWMS REST API for Data Retrieval  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cda_client.api_client import ApiClient


class CatalogApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_cwms_data_catalog_with_dataset(self, dataset, **kwargs):  # noqa: E501
        """Get cwmsData catalog with dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cwms_data_catalog_with_dataset(dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CatalogableEndpoint dataset: A list of what data? E.g. Timeseries, Locations, Ratings, etc (required)
        :param str page: This end point can return a lot of data, this identifies where in the request you are.
        :param str cursor: Deprecated. Use 'page' instead.
        :param int page_size: How many entires per page returned. Default 500.
        :param int page_size: Deprecated. Use page-size.
        :param UnitSystem unit_system: Deprecated. Use unit-system.
        :param UnitSystem unit_system: Unit System desired in response. Can be SI (International Scientific) or EN (Imperial.) If unspecified, defaults to SI.
        :param str office: 3-4 letter office name representing the district you want to isolate data to.
        :param str like: Posix <a href=\"regexp.html\">regular expression</a> matching against the id
        :param str timeseries_category_like: Posix <a href=\"regexp.html\">regular expression</a> matching against the timeseries category id
        :param str timeseries_category_like: Deprecated. Use timeseries-category-like.
        :param str timeseries_group_like: Posix <a href=\"regexp.html\">regular expression</a> matching against the timeseries group id
        :param str timeseries_group_like: Deprecated. Use timeseries-group-like.
        :param str location_category_like: Posix <a href=\"regexp.html\">regular expression</a> matching against the location category id
        :param str location_category_like: Deprecated. Use location-category-like.
        :param str location_group_like: Posix <a href=\"regexp.html\">regular expression</a> matching against the location group id
        :param str location_group_like: Deprecated. Use location-group-like.
        :param str bounding_office_like: Posix <a href=\"regexp.html\">regular expression</a> matching against the location bounding office. When this field is used items with no bounding office set will not be present in results.
        :return: Catalog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cwms_data_catalog_with_dataset_with_http_info(dataset, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cwms_data_catalog_with_dataset_with_http_info(dataset, **kwargs)  # noqa: E501
            return data

    def get_cwms_data_catalog_with_dataset_with_http_info(self, dataset, **kwargs):  # noqa: E501
        """Get cwmsData catalog with dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cwms_data_catalog_with_dataset_with_http_info(dataset, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CatalogableEndpoint dataset: A list of what data? E.g. Timeseries, Locations, Ratings, etc (required)
        :param str page: This end point can return a lot of data, this identifies where in the request you are.
        :param str cursor: Deprecated. Use 'page' instead.
        :param int page_size: How many entires per page returned. Default 500.
        :param int page_size: Deprecated. Use page-size.
        :param UnitSystem unit_system: Deprecated. Use unit-system.
        :param UnitSystem unit_system: Unit System desired in response. Can be SI (International Scientific) or EN (Imperial.) If unspecified, defaults to SI.
        :param str office: 3-4 letter office name representing the district you want to isolate data to.
        :param str like: Posix <a href=\"regexp.html\">regular expression</a> matching against the id
        :param str timeseries_category_like: Posix <a href=\"regexp.html\">regular expression</a> matching against the timeseries category id
        :param str timeseries_category_like: Deprecated. Use timeseries-category-like.
        :param str timeseries_group_like: Posix <a href=\"regexp.html\">regular expression</a> matching against the timeseries group id
        :param str timeseries_group_like: Deprecated. Use timeseries-group-like.
        :param str location_category_like: Posix <a href=\"regexp.html\">regular expression</a> matching against the location category id
        :param str location_category_like: Deprecated. Use location-category-like.
        :param str location_group_like: Posix <a href=\"regexp.html\">regular expression</a> matching against the location group id
        :param str location_group_like: Deprecated. Use location-group-like.
        :param str bounding_office_like: Posix <a href=\"regexp.html\">regular expression</a> matching against the location bounding office. When this field is used items with no bounding office set will not be present in results.
        :return: Catalog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dataset', 'page', 'cursor', 'page_size', 'page_size', 'unit_system', 'unit_system', 'office', 'like', 'timeseries_category_like', 'timeseries_category_like', 'timeseries_group_like', 'timeseries_group_like', 'location_category_like', 'location_category_like', 'location_group_like', 'location_group_like', 'bounding_office_like']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cwms_data_catalog_with_dataset" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dataset' is set
        if ('dataset' not in params or
                params['dataset'] is None):
            raise ValueError("Missing the required parameter `dataset` when calling `get_cwms_data_catalog_with_dataset`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset' in params:
            path_params['dataset'] = params['dataset']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page-size', params['page_size']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'unit_system' in params:
            query_params.append(('unitSystem', params['unit_system']))  # noqa: E501
        if 'unit_system' in params:
            query_params.append(('unit-system', params['unit_system']))  # noqa: E501
        if 'office' in params:
            query_params.append(('office', params['office']))  # noqa: E501
        if 'like' in params:
            query_params.append(('like', params['like']))  # noqa: E501
        if 'timeseries_category_like' in params:
            query_params.append(('timeseries-category-like', params['timeseries_category_like']))  # noqa: E501
        if 'timeseries_category_like' in params:
            query_params.append(('timeseriesCategoryLike', params['timeseries_category_like']))  # noqa: E501
        if 'timeseries_group_like' in params:
            query_params.append(('timeseries-group-like', params['timeseries_group_like']))  # noqa: E501
        if 'timeseries_group_like' in params:
            query_params.append(('timeseriesGroupLike', params['timeseries_group_like']))  # noqa: E501
        if 'location_category_like' in params:
            query_params.append(('location-category-like', params['location_category_like']))  # noqa: E501
        if 'location_category_like' in params:
            query_params.append(('locationCategoryLike', params['location_category_like']))  # noqa: E501
        if 'location_group_like' in params:
            query_params.append(('location-group-like', params['location_group_like']))  # noqa: E501
        if 'location_group_like' in params:
            query_params.append(('locationGroupLike', params['location_group_like']))  # noqa: E501
        if 'bounding_office_like' in params:
            query_params.append(('bounding-office-like', params['bounding_office_like']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/json;version=2', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/cwms-data/catalog/{dataset}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Catalog',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)