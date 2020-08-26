# coding: utf-8

"""
    Wire4RestAPI

    Referencia de la API de Wire4  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from wire4_client.api_client import ApiClient


class PeticionesDePagoPorCoDiApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def consult_codi_request_by_order_id(self, authorization, order_id, sales_point_id, **kwargs):  # noqa: E501
        """Obtiene la información de una petición de pago CODI® por orderId para un punto de venta  # noqa: E501

        Obtiene la información de una petición de pago CODI® por orderId para un punto de venta  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.consult_codi_request_by_order_id(authorization, order_id, sales_point_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Header para token (required)
        :param str order_id: Identificador del pago CODI® (required)
        :param str sales_point_id: Identificador del punto de venta (required)
        :return: PaymentRequestCodiResponseDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.consult_codi_request_by_order_id_with_http_info(authorization, order_id, sales_point_id, **kwargs)  # noqa: E501
        else:
            (data) = self.consult_codi_request_by_order_id_with_http_info(authorization, order_id, sales_point_id, **kwargs)  # noqa: E501
            return data

    def consult_codi_request_by_order_id_with_http_info(self, authorization, order_id, sales_point_id, **kwargs):  # noqa: E501
        """Obtiene la información de una petición de pago CODI® por orderId para un punto de venta  # noqa: E501

        Obtiene la información de una petición de pago CODI® por orderId para un punto de venta  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.consult_codi_request_by_order_id_with_http_info(authorization, order_id, sales_point_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Header para token (required)
        :param str order_id: Identificador del pago CODI® (required)
        :param str sales_point_id: Identificador del punto de venta (required)
        :return: PaymentRequestCodiResponseDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'order_id', 'sales_point_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consult_codi_request_by_order_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `consult_codi_request_by_order_id`")  # noqa: E501
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `consult_codi_request_by_order_id`")  # noqa: E501
        # verify the required parameter 'sales_point_id' is set
        if ('sales_point_id' not in params or
                params['sales_point_id'] is None):
            raise ValueError("Missing the required parameter `sales_point_id` when calling `consult_codi_request_by_order_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in params:
            query_params.append(('orderId', params['order_id']))  # noqa: E501
        if 'sales_point_id' in params:
            query_params.append(('salesPointId', params['sales_point_id']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/codi/sales-point/charges', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentRequestCodiResponseDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def generate_codi_code_qr(self, body, authorization, sales_point_id, **kwargs):  # noqa: E501
        """Genera un código QR para un pago mediante CODI®  # noqa: E501

        Genera un código QR solicitado por un punto de venta para un pago mediante CODI®  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_codi_code_qr(body, authorization, sales_point_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CodiCodeRequestDTO body: Información del pago CODI® (required)
        :param str authorization: Header para token (required)
        :param str sales_point_id: Identificador del punto de venta (required)
        :return: CodiCodeQrResponseDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.generate_codi_code_qr_with_http_info(body, authorization, sales_point_id, **kwargs)  # noqa: E501
        else:
            (data) = self.generate_codi_code_qr_with_http_info(body, authorization, sales_point_id, **kwargs)  # noqa: E501
            return data

    def generate_codi_code_qr_with_http_info(self, body, authorization, sales_point_id, **kwargs):  # noqa: E501
        """Genera un código QR para un pago mediante CODI®  # noqa: E501

        Genera un código QR solicitado por un punto de venta para un pago mediante CODI®  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_codi_code_qr_with_http_info(body, authorization, sales_point_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CodiCodeRequestDTO body: Información del pago CODI® (required)
        :param str authorization: Header para token (required)
        :param str sales_point_id: Identificador del punto de venta (required)
        :return: CodiCodeQrResponseDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'sales_point_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_codi_code_qr" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `generate_codi_code_qr`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `generate_codi_code_qr`")  # noqa: E501
        # verify the required parameter 'sales_point_id' is set
        if ('sales_point_id' not in params or
                params['sales_point_id'] is None):
            raise ValueError("Missing the required parameter `sales_point_id` when calling `generate_codi_code_qr`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sales_point_id' in params:
            query_params.append(('salesPointId', params['sales_point_id']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/codi/sales-point/charges', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CodiCodeQrResponseDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)