# coding: utf-8

"""
    Wire4RestAPI

    Referencia de la API de Wire4  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import wire4_client
from api.cargos_recurrentes_api import CargosRecurrentesApi  # noqa: E501
from wire4_client.rest import ApiException


class TestCargosRecurrentesApi(unittest.TestCase):
    """CargosRecurrentesApi unit test stubs"""

    def setUp(self):
        self.api = api.cargos_recurrentes_api.CargosRecurrentesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_register_recurring_charge_using_post(self):
        """Test case for register_recurring_charge_using_post

        Registro de cargos recurrentes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()