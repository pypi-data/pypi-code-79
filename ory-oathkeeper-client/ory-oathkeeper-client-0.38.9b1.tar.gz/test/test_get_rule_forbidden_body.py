# coding: utf-8

"""
    ORY Oathkeeper

    ORY Oathkeeper is a reverse proxy that checks the HTTP Authorization for validity against a set of rules. This service uses Hydra to validate access tokens and policies.  # noqa: E501

    The version of the OpenAPI document: v0.0.0-alpha.1
    Contact: hi@ory.am
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ory_oathkeeper_client
from ory_oathkeeper_client.models.get_rule_forbidden_body import GetRuleForbiddenBody  # noqa: E501
from ory_oathkeeper_client.rest import ApiException


class TestGetRuleForbiddenBody(unittest.TestCase):
    """GetRuleForbiddenBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetRuleForbiddenBody(self):
        """Test GetRuleForbiddenBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ory_oathkeeper_client.models.get_rule_forbidden_body.GetRuleForbiddenBody()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
