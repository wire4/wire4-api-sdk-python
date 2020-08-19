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
from api.transferencias_spei_api import TransferenciasSPEIApi  # noqa: E501
from wire4_client.rest import ApiException


class TestTransferenciasSPEIApi(unittest.TestCase):
    """TransferenciasSPEIApi unit test stubs"""

    def setUp(self):
        self.api = api.transferencias_spei_api.TransferenciasSPEIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_authorization_transactions_group(self):
        """Test case for create_authorization_transactions_group

        Agrupa un conjunto de transacciones bajo un mismo request_id para autorizar  # noqa: E501
        """
        pass

    def test_drop_transactions_pending_using_delete(self):
        """Test case for drop_transactions_pending_using_delete

        Eliminación de transferencias SPEI® pendientes  # noqa: E501
        """
        pass

    def test_incoming_spei_transactions_report_using_get(self):
        """Test case for incoming_spei_transactions_report_using_get

        Consulta de transferencias recibidas  # noqa: E501
        """
        pass

    def test_out_comming_spei_request_id_transactions_report_using_get(self):
        """Test case for out_comming_spei_request_id_transactions_report_using_get

        Consulta de transferencias de salida por identificador de petición  # noqa: E501
        """
        pass

    def test_outgoing_spei_transactions_report_using_get(self):
        """Test case for outgoing_spei_transactions_report_using_get

        Consulta de transferencias realizadas  # noqa: E501
        """
        pass

    def test_register_outgoing_spei_transaction_using_post(self):
        """Test case for register_outgoing_spei_transaction_using_post

        Registro de transferencias  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
