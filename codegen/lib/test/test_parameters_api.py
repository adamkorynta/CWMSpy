# coding: utf-8

"""
    CWMS Data API

    CWMS REST API for Data Retrieval  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import cda_client
from cda_client.api.parameters_api import ParametersApi  # noqa: E501
from cda_client.rest import ApiException


class TestParametersApi(unittest.TestCase):
    """ParametersApi unit test stubs"""

    def setUp(self):
        self.api = ParametersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_cwms_data_parameters(self):
        """Test case for get_cwms_data_parameters

        Get cwmsData parameters  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
