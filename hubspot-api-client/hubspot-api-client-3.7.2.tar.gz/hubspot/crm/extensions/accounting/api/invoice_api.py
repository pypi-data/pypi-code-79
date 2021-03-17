# coding: utf-8

"""
    Accounting Extension

    These APIs allow you to interact with HubSpot's Accounting Extension. It allows you to: * Specify the URLs that HubSpot will use when making webhook requests to your external accounting system. * Respond to webhook calls made to your external accounting system by HubSpot   # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.extensions.accounting.api_client import ApiClient
from hubspot.crm.extensions.accounting.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError,
)


class InvoiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_payment(
        self, invoice_id, invoice_create_payment_request, **kwargs
    ):  # noqa: E501
        """Records an invoice payment  # noqa: E501

        Records an payment against an invoice.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_payment(invoice_id, invoice_create_payment_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str invoice_id: The ID of the invoice. This is the invoice ID from the external accounting system. (required)
        :param InvoiceCreatePaymentRequest invoice_create_payment_request: The payment information (required)
        :param str account_id: The ID of the account that the invoice belongs to. This is the account ID from the external accounting system.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InvoiceUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_payment_with_http_info(
            invoice_id, invoice_create_payment_request, **kwargs
        )  # noqa: E501

    def create_payment_with_http_info(
        self, invoice_id, invoice_create_payment_request, **kwargs
    ):  # noqa: E501
        """Records an invoice payment  # noqa: E501

        Records an payment against an invoice.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_payment_with_http_info(invoice_id, invoice_create_payment_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str invoice_id: The ID of the invoice. This is the invoice ID from the external accounting system. (required)
        :param InvoiceCreatePaymentRequest invoice_create_payment_request: The payment information (required)
        :param str account_id: The ID of the account that the invoice belongs to. This is the account ID from the external accounting system.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InvoiceUpdateResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["invoice_id", "invoice_create_payment_request", "account_id"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_payment" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'invoice_id' is set
        if self.api_client.client_side_validation and (
            "invoice_id" not in local_var_params
            or local_var_params["invoice_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `invoice_id` when calling `create_payment`"
            )  # noqa: E501
        # verify the required parameter 'invoice_create_payment_request' is set
        if self.api_client.client_side_validation and (
            "invoice_create_payment_request" not in local_var_params
            or local_var_params["invoice_create_payment_request"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `invoice_create_payment_request` when calling `create_payment`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "invoice_id" in local_var_params:
            path_params["invoiceId"] = local_var_params["invoice_id"]  # noqa: E501

        query_params = []
        if (
            "account_id" in local_var_params
            and local_var_params["account_id"] is not None
        ):  # noqa: E501
            query_params.append(
                ("accountId", local_var_params["account_id"])
            )  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "invoice_create_payment_request" in local_var_params:
            body_params = local_var_params["invoice_create_payment_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/extensions/accounting/invoice/{invoiceId}/payment",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InvoiceUpdateResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_by_id(self, invoice_id, account_id, **kwargs):  # noqa: E501
        """Get invoice data  # noqa: E501

        Returns invoice data for an Accounting account from the specified ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id(invoice_id, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str invoice_id: The ID of the invoice. This is the invoice ID from the external accounting system. (required)
        :param str account_id: The ID of the account that the invoice belongs to. This is the account ID from the external accounting system. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InvoiceReadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_by_id_with_http_info(
            invoice_id, account_id, **kwargs
        )  # noqa: E501

    def get_by_id_with_http_info(self, invoice_id, account_id, **kwargs):  # noqa: E501
        """Get invoice data  # noqa: E501

        Returns invoice data for an Accounting account from the specified ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_with_http_info(invoice_id, account_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str invoice_id: The ID of the invoice. This is the invoice ID from the external accounting system. (required)
        :param str account_id: The ID of the account that the invoice belongs to. This is the account ID from the external accounting system. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InvoiceReadResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["invoice_id", "account_id"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'invoice_id' is set
        if self.api_client.client_side_validation and (
            "invoice_id" not in local_var_params
            or local_var_params["invoice_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `invoice_id` when calling `get_by_id`"
            )  # noqa: E501
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and (
            "account_id" not in local_var_params
            or local_var_params["account_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `account_id` when calling `get_by_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "invoice_id" in local_var_params:
            path_params["invoiceId"] = local_var_params["invoice_id"]  # noqa: E501

        query_params = []
        if (
            "account_id" in local_var_params
            and local_var_params["account_id"] is not None
        ):  # noqa: E501
            query_params.append(
                ("accountId", local_var_params["account_id"])
            )  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/extensions/accounting/invoice/{invoiceId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InvoiceReadResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update(
        self, invoice_id, account_id, invoice_update_request, **kwargs
    ):  # noqa: E501
        """Update an invoice  # noqa: E501

        Updates an Invoice by the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(invoice_id, account_id, invoice_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str invoice_id: The ID of the invoice. This is the invoice ID from the external accounting system. (required)
        :param str account_id: The ID of the account that the invoice belongs to. This is the account ID from the external accounting system. (required)
        :param InvoiceUpdateRequest invoice_update_request: The invoice data to update (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InvoiceUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.update_with_http_info(
            invoice_id, account_id, invoice_update_request, **kwargs
        )  # noqa: E501

    def update_with_http_info(
        self, invoice_id, account_id, invoice_update_request, **kwargs
    ):  # noqa: E501
        """Update an invoice  # noqa: E501

        Updates an Invoice by the given ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(invoice_id, account_id, invoice_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str invoice_id: The ID of the invoice. This is the invoice ID from the external accounting system. (required)
        :param str account_id: The ID of the account that the invoice belongs to. This is the account ID from the external accounting system. (required)
        :param InvoiceUpdateRequest invoice_update_request: The invoice data to update (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InvoiceUpdateResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["invoice_id", "account_id", "invoice_update_request"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method update" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'invoice_id' is set
        if self.api_client.client_side_validation and (
            "invoice_id" not in local_var_params
            or local_var_params["invoice_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `invoice_id` when calling `update`"
            )  # noqa: E501
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and (
            "account_id" not in local_var_params
            or local_var_params["account_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `account_id` when calling `update`"
            )  # noqa: E501
        # verify the required parameter 'invoice_update_request' is set
        if self.api_client.client_side_validation and (
            "invoice_update_request" not in local_var_params
            or local_var_params["invoice_update_request"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `invoice_update_request` when calling `update`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "invoice_id" in local_var_params:
            path_params["invoiceId"] = local_var_params["invoice_id"]  # noqa: E501

        query_params = []
        if (
            "account_id" in local_var_params
            and local_var_params["account_id"] is not None
        ):  # noqa: E501
            query_params.append(
                ("accountId", local_var_params["account_id"])
            )  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "invoice_update_request" in local_var_params:
            body_params = local_var_params["invoice_update_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/extensions/accounting/invoice/{invoiceId}",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InvoiceUpdateResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
