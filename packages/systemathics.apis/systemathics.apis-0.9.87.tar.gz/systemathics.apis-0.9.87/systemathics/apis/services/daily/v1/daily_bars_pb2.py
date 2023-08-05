# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily/v1/daily_bars.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.type import date_pb2 as google_dot_type_dot_date__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4systemathics/apis/services/daily/v1/daily_bars.proto\x12#systemathics.apis.services.daily.v1\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\"\xac\x01\n\x10\x44\x61ilyBarsRequest\x12@\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.Identifier\x12\x42\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.Constraints\x12\x12\n\nadjustment\x18\x03 \x01(\x08\"P\n\x11\x44\x61ilyBarsResponse\x12;\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32-.systemathics.apis.services.daily.v1.DailyBar\"\x82\x01\n\x08\x44\x61ilyBar\x12\x1f\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.Date\x12\x0c\n\x04open\x18\x02 \x01(\x01\x12\x0c\n\x04high\x18\x03 \x01(\x01\x12\x0b\n\x03low\x18\x04 \x01(\x01\x12\r\n\x05\x63lose\x18\x05 \x01(\x01\x12\x0e\n\x06volume\x18\x06 \x01(\x03\x12\r\n\x05score\x18\x07 \x01(\x01\x32\x8e\x01\n\x10\x44\x61ilyBarsService\x12z\n\tDailyBars\x12\x35.systemathics.apis.services.daily.v1.DailyBarsRequest\x1a\x36.systemathics.apis.services.daily.v1.DailyBarsResponseb\x06proto3')



_DAILYBARSREQUEST = DESCRIPTOR.message_types_by_name['DailyBarsRequest']
_DAILYBARSRESPONSE = DESCRIPTOR.message_types_by_name['DailyBarsResponse']
_DAILYBAR = DESCRIPTOR.message_types_by_name['DailyBar']
DailyBarsRequest = _reflection.GeneratedProtocolMessageType('DailyBarsRequest', (_message.Message,), {
  'DESCRIPTOR' : _DAILYBARSREQUEST,
  '__module__' : 'systemathics.apis.services.daily.v1.daily_bars_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily.v1.DailyBarsRequest)
  })
_sym_db.RegisterMessage(DailyBarsRequest)

DailyBarsResponse = _reflection.GeneratedProtocolMessageType('DailyBarsResponse', (_message.Message,), {
  'DESCRIPTOR' : _DAILYBARSRESPONSE,
  '__module__' : 'systemathics.apis.services.daily.v1.daily_bars_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily.v1.DailyBarsResponse)
  })
_sym_db.RegisterMessage(DailyBarsResponse)

DailyBar = _reflection.GeneratedProtocolMessageType('DailyBar', (_message.Message,), {
  'DESCRIPTOR' : _DAILYBAR,
  '__module__' : 'systemathics.apis.services.daily.v1.daily_bars_pb2'
  # @@protoc_insertion_point(class_scope:systemathics.apis.services.daily.v1.DailyBar)
  })
_sym_db.RegisterMessage(DailyBar)

_DAILYBARSSERVICE = DESCRIPTOR.services_by_name['DailyBarsService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DAILYBARSREQUEST._serialized_start=221
  _DAILYBARSREQUEST._serialized_end=393
  _DAILYBARSRESPONSE._serialized_start=395
  _DAILYBARSRESPONSE._serialized_end=475
  _DAILYBAR._serialized_start=478
  _DAILYBAR._serialized_end=608
  _DAILYBARSSERVICE._serialized_start=611
  _DAILYBARSSERVICE._serialized_end=753
# @@protoc_insertion_point(module_scope)
