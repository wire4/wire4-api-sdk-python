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


class EmpresasCoDiApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def obtain_companies(self, authorization, **kwargs):  # noqa: E501
        """Consulta de empresas CODI®  # noqa: E501

        Consulta de empresas CODI® registradas para la aplicación.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.obtain_companies(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Header para token (required)
        :return: list[CompanyRegistered]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.obtain_companies_with_http_info(authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.obtain_companies_with_http_info(authorization, **kwargs)  # noqa: E501
            return data

    def obtain_companies_with_http_info(self, authorization, **kwargs):  # noqa: E501
        """Consulta de empresas CODI®  # noqa: E501

        Consulta de empresas CODI® registradas para la aplicación.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.obtain_companies_with_http_info(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Header para token (required)
        :return: list[CompanyRegistered]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method obtain_companies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `obtain_companies`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/codi/companies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CompanyRegistered]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def register_company_using_post(self, body, authorization, **kwargs):  # noqa: E501
        """Registro de empresas CODI®  # noqa: E501

        Registra una empresa para hacer uso de operaciones CODI®.<br><br> <b>Nota:<b> Es requerido tener el certificado emitido por BANXICO® asi como el Nombre de la empresa, Nombre comercial y el Registro Federal de Contribuyentes (RFC) de la empresa.<br/>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_company_using_post(body, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CompanyRequested body: Información de la cuenta del beneficiario (required)
        :param str authorization: Header para token (required)
        :return: CompanyRegistered
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.register_company_using_post_with_http_info(body, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.register_company_using_post_with_http_info(body, authorization, **kwargs)  # noqa: E501
            return data

    def register_company_using_post_with_http_info(self, body, authorization, **kwargs):  # noqa: E501
        """Registro de empresas CODI®  # noqa: E501

        Registra una empresa para hacer uso de operaciones CODI®.<br><br> <b>Nota:<b> Es requerido tener el certificado emitido por BANXICO® asi como el Nombre de la empresa, Nombre comercial y el Registro Federal de Contribuyentes (RFC) de la empresa.<br/>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.register_company_using_post_with_http_info(body, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CompanyRequested body: Información de la cuenta del beneficiario (required)
        :param str authorization: Header para token (required)
        :return: CompanyRegistered
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register_company_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `register_company_using_post`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `register_company_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/codi/companies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CompanyRegistered',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
