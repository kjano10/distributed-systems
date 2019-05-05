# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import currencyExchange_pb2 as currencyExchange__pb2


class currencyServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.addBank = channel.unary_stream(
        '/currencyEx.currencyService/addBank',
        request_serializer=currencyExchange__pb2.Subscribe.SerializeToString,
        response_deserializer=currencyExchange__pb2.AckCur.FromString,
        )


class currencyServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def addBank(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_currencyServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'addBank': grpc.unary_stream_rpc_method_handler(
          servicer.addBank,
          request_deserializer=currencyExchange__pb2.Subscribe.FromString,
          response_serializer=currencyExchange__pb2.AckCur.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'currencyEx.currencyService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
