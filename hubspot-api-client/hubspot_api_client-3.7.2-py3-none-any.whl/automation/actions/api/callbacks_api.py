# coding: utf-8

"""
    Custom Workflow Actions

    Create custom workflow actions  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.automation.actions.api_client import ApiClient
from hubspot.automation.actions.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError,
)


class CallbacksApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def complete(
        self, callback_id, callback_completion_request, **kwargs
    ):  # noqa: E501
        """Complete a callback  # noqa: E501

        Completes the given action callback.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complete(callback_id, callback_completion_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str callback_id: The ID of the target app. (required)
        :param CallbackCompletionRequest callback_completion_request: The result of the completed action. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.complete_with_http_info(
            callback_id, callback_completion_request, **kwargs
        )  # noqa: E501

    def complete_with_http_info(
        self, callback_id, callback_completion_request, **kwargs
    ):  # noqa: E501
        """Complete a callback  # noqa: E501

        Completes the given action callback.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complete_with_http_info(callback_id, callback_completion_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str callback_id: The ID of the target app. (required)
        :param CallbackCompletionRequest callback_completion_request: The result of the completed action. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["callback_id", "callback_completion_request"]
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
                    " to method complete" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'callback_id' is set
        if self.api_client.client_side_validation and (
            "callback_id" not in local_var_params
            or local_var_params["callback_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `callback_id` when calling `complete`"
            )  # noqa: E501
        # verify the required parameter 'callback_completion_request' is set
        if self.api_client.client_side_validation and (
            "callback_completion_request" not in local_var_params
            or local_var_params["callback_completion_request"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `callback_completion_request` when calling `complete`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "callback_id" in local_var_params:
            path_params["callbackId"] = local_var_params["callback_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "callback_completion_request" in local_var_params:
            body_params = local_var_params["callback_completion_request"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["*/*"]
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
            "/automation/v4/actions/callbacks/{callbackId}/complete",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def complete_batch(
        self, batch_input_callback_completion_batch_request, **kwargs
    ):  # noqa: E501
        """Complete a batch of callbacks  # noqa: E501

        Completes the given action callbacks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complete_batch(batch_input_callback_completion_batch_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchInputCallbackCompletionBatchRequest batch_input_callback_completion_batch_request: The result of the completed action. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.complete_batch_with_http_info(
            batch_input_callback_completion_batch_request, **kwargs
        )  # noqa: E501

    def complete_batch_with_http_info(
        self, batch_input_callback_completion_batch_request, **kwargs
    ):  # noqa: E501
        """Complete a batch of callbacks  # noqa: E501

        Completes the given action callbacks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complete_batch_with_http_info(batch_input_callback_completion_batch_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param BatchInputCallbackCompletionBatchRequest batch_input_callback_completion_batch_request: The result of the completed action. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["batch_input_callback_completion_batch_request"]
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
                    " to method complete_batch" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'batch_input_callback_completion_batch_request' is set
        if self.api_client.client_side_validation and (
            "batch_input_callback_completion_batch_request" not in local_var_params
            or local_var_params[  # noqa: E501
                "batch_input_callback_completion_batch_request"
            ]
            is None
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `batch_input_callback_completion_batch_request` when calling `complete_batch`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_callback_completion_batch_request" in local_var_params:
            body_params = local_var_params[
                "batch_input_callback_completion_batch_request"
            ]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["*/*"]
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
            "/automation/v4/actions/callbacks/complete",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
