# coding: utf-8

"""
    Investor8.Core

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import investor8_sdk
from investor8_sdk.api.screener_api import ScreenerApi  # noqa: E501
from investor8_sdk.rest import ApiException


class TestScreenerApi(unittest.TestCase):
    """ScreenerApi unit test stubs"""

    def setUp(self):
        self.api = ScreenerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_sectors_returns(self):
        """Test case for get_all_sectors_returns

        """
        pass

    def test_get_all_sectors_returns_today_sa(self):
        """Test case for get_all_sectors_returns_today_sa

        """
        pass

    def test_get_dow_tickers(self):
        """Test case for get_dow_tickers

        """
        pass

    def test_get_list_ip_os(self):
        """Test case for get_list_ip_os

        """
        pass

    def test_get_top_stocks(self):
        """Test case for get_top_stocks

        """
        pass

    def test_get_upcoming_ipos(self):
        """Test case for get_upcoming_ipos

        """
        pass


if __name__ == '__main__':
    unittest.main()
