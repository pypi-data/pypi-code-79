# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cs3.app.registry.v1beta1 import registry_api_pb2 as cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2


class RegistryAPIStub(object):
    """App Registry API

    The App Registry API is meant to as registry that
    contains mappings between mime types and app providers.

    The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
    NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
    "OPTIONAL" in this document are to be interpreted as described in
    RFC 2119.

    The following are global requirements that apply to all methods:
    Any method MUST return CODE_OK on a succesful operation.
    Any method MAY return NOT_IMPLEMENTED.
    Any method MAY return INTERNAL.
    Any method MAY return UNKNOWN.
    Any method MAY return UNAUTHENTICATED.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAppProviders = channel.unary_unary(
                '/cs3.app.registry.v1beta1.RegistryAPI/GetAppProviders',
                request_serializer=cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetAppProvidersRequest.SerializeToString,
                response_deserializer=cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetAppProvidersResponse.FromString,
                )
        self.ListAppProviders = channel.unary_unary(
                '/cs3.app.registry.v1beta1.RegistryAPI/ListAppProviders',
                request_serializer=cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListAppProvidersRequest.SerializeToString,
                response_deserializer=cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListAppProvidersResponse.FromString,
                )


class RegistryAPIServicer(object):
    """App Registry API

    The App Registry API is meant to as registry that
    contains mappings between mime types and app providers.

    The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
    NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
    "OPTIONAL" in this document are to be interpreted as described in
    RFC 2119.

    The following are global requirements that apply to all methods:
    Any method MUST return CODE_OK on a succesful operation.
    Any method MAY return NOT_IMPLEMENTED.
    Any method MAY return INTERNAL.
    Any method MAY return UNKNOWN.
    Any method MAY return UNAUTHENTICATED.
    """

    def GetAppProviders(self, request, context):
        """Returns the app providers that are capable of handling this resource info.
        MUST return CODE_NOT_FOUND if no providers are available.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAppProviders(self, request, context):
        """Returns a list of the available app providers known by this registry.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RegistryAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAppProviders': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAppProviders,
                    request_deserializer=cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetAppProvidersRequest.FromString,
                    response_serializer=cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetAppProvidersResponse.SerializeToString,
            ),
            'ListAppProviders': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAppProviders,
                    request_deserializer=cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListAppProvidersRequest.FromString,
                    response_serializer=cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListAppProvidersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cs3.app.registry.v1beta1.RegistryAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RegistryAPI(object):
    """App Registry API

    The App Registry API is meant to as registry that
    contains mappings between mime types and app providers.

    The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
    NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
    "OPTIONAL" in this document are to be interpreted as described in
    RFC 2119.

    The following are global requirements that apply to all methods:
    Any method MUST return CODE_OK on a succesful operation.
    Any method MAY return NOT_IMPLEMENTED.
    Any method MAY return INTERNAL.
    Any method MAY return UNKNOWN.
    Any method MAY return UNAUTHENTICATED.
    """

    @staticmethod
    def GetAppProviders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.app.registry.v1beta1.RegistryAPI/GetAppProviders',
            cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetAppProvidersRequest.SerializeToString,
            cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetAppProvidersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAppProviders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.app.registry.v1beta1.RegistryAPI/ListAppProviders',
            cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListAppProvidersRequest.SerializeToString,
            cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListAppProvidersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
