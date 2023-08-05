# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.tick_analytics.v1 import tick_sma_pb2 as systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__sma__pb2


class TickSmaServiceStub(object):
    """Called to request tick by tick simple moving average data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TickSma = channel.unary_stream(
                '/systemathics.apis.services.tick_analytics.v1.TickSmaService/TickSma',
                request_serializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__sma__pb2.TickSmaRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__sma__pb2.TickSmaResponse.FromString,
                )


class TickSmaServiceServicer(object):
    """Called to request tick by tick simple moving average data.
    """

    def TickSma(self, request, context):
        """Gets tick by tick simple moving average data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TickSmaServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TickSma': grpc.unary_stream_rpc_method_handler(
                    servicer.TickSma,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__sma__pb2.TickSmaRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__sma__pb2.TickSmaResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.tick_analytics.v1.TickSmaService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TickSmaService(object):
    """Called to request tick by tick simple moving average data.
    """

    @staticmethod
    def TickSma(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/systemathics.apis.services.tick_analytics.v1.TickSmaService/TickSma',
            systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__sma__pb2.TickSmaRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__sma__pb2.TickSmaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
