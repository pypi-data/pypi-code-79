# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from bosdyn.api import time_sync_pb2 as bosdyn_dot_api_dot_time__sync__pb2


class TimeSyncServiceStub(object):
  """The time-sync service estimates the difference between server and client clocks.
  Time synchronization is a tool which allows applications to work in a unified timebase with
  precision. It is useful in cases where a precise time must be set, independently of network
  communication lag. In distributed systems and robotics, hardware, system-level, and per-process
  approaches can be used to obtain synchronization.
  This service implements a stand alone time synchronization service. It enables clients to
  establish a per-process offset between two processes which may be on separate systems.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.TimeSyncUpdate = channel.unary_unary(
        '/bosdyn.api.TimeSyncService/TimeSyncUpdate',
        request_serializer=bosdyn_dot_api_dot_time__sync__pb2.TimeSyncUpdateRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_time__sync__pb2.TimeSyncUpdateResponse.FromString,
        )


class TimeSyncServiceServicer(object):
  """The time-sync service estimates the difference between server and client clocks.
  Time synchronization is a tool which allows applications to work in a unified timebase with
  precision. It is useful in cases where a precise time must be set, independently of network
  communication lag. In distributed systems and robotics, hardware, system-level, and per-process
  approaches can be used to obtain synchronization.
  This service implements a stand alone time synchronization service. It enables clients to
  establish a per-process offset between two processes which may be on separate systems.
  """

  def TimeSyncUpdate(self, request, context):
    """See the exchange documentation in time_sync.proto. This call makes one client/server
    round trip toward clock synchronization.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TimeSyncServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'TimeSyncUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.TimeSyncUpdate,
          request_deserializer=bosdyn_dot_api_dot_time__sync__pb2.TimeSyncUpdateRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_time__sync__pb2.TimeSyncUpdateResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'bosdyn.api.TimeSyncService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
