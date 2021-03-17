# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.inventory.v1 import cloud_service_type_pb2 as spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2


class CloudServiceTypeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.inventory.v1.CloudServiceType/create',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CreateCloudServiceTypeRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeInfo.FromString,
                )
        self.update = channel.unary_unary(
                '/spaceone.api.inventory.v1.CloudServiceType/update',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.UpdateCloudServiceTypeRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeInfo.FromString,
                )
        self.pin_data = channel.unary_unary(
                '/spaceone.api.inventory.v1.CloudServiceType/pin_data',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.PinCloudServiceTypeDataRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeInfo.FromString,
                )
        self.delete = channel.unary_unary(
                '/spaceone.api.inventory.v1.CloudServiceType/delete',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.get = channel.unary_unary(
                '/spaceone.api.inventory.v1.CloudServiceType/get',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.GetCloudServiceTypeRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeInfo.FromString,
                )
        self.list = channel.unary_unary(
                '/spaceone.api.inventory.v1.CloudServiceType/list',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypesInfo.FromString,
                )
        self.stat = channel.unary_unary(
                '/spaceone.api.inventory.v1.CloudServiceType/stat',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )


class CloudServiceTypeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def pin_data(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CloudServiceTypeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CreateCloudServiceTypeRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.UpdateCloudServiceTypeRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeInfo.SerializeToString,
            ),
            'pin_data': grpc.unary_unary_rpc_method_handler(
                    servicer.pin_data,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.PinCloudServiceTypeDataRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.GetCloudServiceTypeRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypesInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.inventory.v1.CloudServiceType', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CloudServiceType(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.CloudServiceType/create',
            spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CreateCloudServiceTypeRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.CloudServiceType/update',
            spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.UpdateCloudServiceTypeRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def pin_data(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.CloudServiceType/pin_data',
            spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.PinCloudServiceTypeDataRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.CloudServiceType/delete',
            spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.CloudServiceType/get',
            spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.GetCloudServiceTypeRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.CloudServiceType/list',
            spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeQuery.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypesInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.CloudServiceType/stat',
            spaceone_dot_api_dot_inventory_dot_v1_dot_cloud__service__type__pb2.CloudServiceTypeStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
