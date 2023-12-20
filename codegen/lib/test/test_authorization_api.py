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
from cda_client.api.authorization_api import AuthorizationApi  # noqa: E501
from cda_client.rest import ApiException


class TestAuthorizationApi(unittest.TestCase):
    """AuthorizationApi unit test stubs"""

    def setUp(self):
        self.api = AuthorizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_cwms_data_auth_keys_with_key_name(self):
        """Test case for delete_cwms_data_auth_keys_with_key_name

        Delete cwmsData auth keys with keyName  # noqa: E501
        """
        pass

    def test_get_cwms_data_auth_keys(self):
        """Test case for get_cwms_data_auth_keys

        Get cwmsData auth keys  # noqa: E501
        """
        pass

    def test_get_cwms_data_auth_keys_with_key_name(self):
        """Test case for get_cwms_data_auth_keys_with_key_name

        Get cwmsData auth keys with keyName  # noqa: E501
        """
        pass

    def test_post_cwms_data_auth_keys(self):
        """Test case for post_cwms_data_auth_keys

        Post cwmsData auth keys  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
