# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from bosdyn.api import network_compute_bridge_pb2 as bosdyn_dot_api_dot_network__compute__bridge__pb2


class NetworkComputeBridgeStub(object):
  """RPCs for sending images or other data to networked server for computation.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.NetworkCompute = channel.unary_unary(
        '/bosdyn.api.NetworkComputeBridge/NetworkCompute',
        request_serializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.NetworkComputeRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.NetworkComputeResponse.FromString,
        )
    self.ListAvailableModels = channel.unary_unary(
        '/bosdyn.api.NetworkComputeBridge/ListAvailableModels',
        request_serializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.ListAvailableModelsRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.ListAvailableModelsResponse.FromString,
        )


class NetworkComputeBridgeServicer(object):
  """RPCs for sending images or other data to networked server for computation.
  """

  def NetworkCompute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListAvailableModels(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NetworkComputeBridgeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'NetworkCompute': grpc.unary_unary_rpc_method_handler(
          servicer.NetworkCompute,
          request_deserializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.NetworkComputeRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.NetworkComputeResponse.SerializeToString,
      ),
      'ListAvailableModels': grpc.unary_unary_rpc_method_handler(
          servicer.ListAvailableModels,
          request_deserializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.ListAvailableModelsRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.ListAvailableModelsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'bosdyn.api.NetworkComputeBridge', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class NetworkComputeBridgeWorkerStub(object):
  """Set of RPCs for workers of the network compute bridge.  This is seperate from the RPCs for the
  on-robot network compute bridge so that if they need to diverge in the future it is possible
  to do so.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.NetworkCompute = channel.unary_unary(
        '/bosdyn.api.NetworkComputeBridgeWorker/NetworkCompute',
        request_serializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.NetworkComputeRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.NetworkComputeResponse.FromString,
        )
    self.ListAvailableModels = channel.unary_unary(
        '/bosdyn.api.NetworkComputeBridgeWorker/ListAvailableModels',
        request_serializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.ListAvailableModelsRequest.SerializeToString,
        response_deserializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.ListAvailableModelsResponse.FromString,
        )


class NetworkComputeBridgeWorkerServicer(object):
  """Set of RPCs for workers of the network compute bridge.  This is seperate from the RPCs for the
  on-robot network compute bridge so that if they need to diverge in the future it is possible
  to do so.
  """

  def NetworkCompute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListAvailableModels(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NetworkComputeBridgeWorkerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'NetworkCompute': grpc.unary_unary_rpc_method_handler(
          servicer.NetworkCompute,
          request_deserializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.NetworkComputeRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.NetworkComputeResponse.SerializeToString,
      ),
      'ListAvailableModels': grpc.unary_unary_rpc_method_handler(
          servicer.ListAvailableModels,
          request_deserializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.ListAvailableModelsRequest.FromString,
          response_serializer=bosdyn_dot_api_dot_network__compute__bridge__pb2.ListAvailableModelsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'bosdyn.api.NetworkComputeBridgeWorker', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
