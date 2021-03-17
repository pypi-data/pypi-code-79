# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gv_proto/proto/archivist.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gv_proto/proto/archivist.proto',
  package='gv_proto.proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1egv_proto/proto/archivist.proto\x12\x0egv_proto.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbb\x01\n\x11IndicatorsRequest\x12\x10\n\x08\x64\x61tatype\x18\x01 \x01(\t\x12,\n\x08\x66romdate\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x06todate\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04\x66req\x18\x04 \x01(\x05\x12\x0e\n\x06noeids\x18\x05 \x01(\x08\x12\x0c\n\x04\x61rea\x18\x06 \x01(\x0c\x12\x0e\n\x06window\x18\x07 \x01(\x05\"1\n\nIndicators\x12\x12\n\nindicators\x18\x01 \x01(\x0c\x12\x0f\n\x07\x61pplyto\x18\x02 \x01(\t\"\x80\x01\n\x12\x44\x61taQualityRequest\x12\x10\n\x08\x64\x61tatype\x18\x01 \x01(\t\x12,\n\x08\x66romdate\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x06todate\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\"\n\x0b\x44\x61taQuality\x12\x13\n\x0b\x64\x61taquality\x18\x01 \x01(\x0c\"\xa9\x01\n\x13LocationDataRequest\x12\x13\n\x0b\x64\x61tatypeeid\x18\x01 \x01(\t\x12\x13\n\x0blocationeid\x18\x02 \x01(\t\x12,\n\x08\x66romdate\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x06todate\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06period\x18\x05 \x01(\t\"$\n\x0cLocationData\x12\x14\n\x0clocationdata\x18\x01 \x01(\x0c\"\xa6\x01\n\x16ZonesTravelTimeRequest\x12\x11\n\tfromPoint\x18\x01 \x01(\t\x12\x0f\n\x07toPoint\x18\x02 \x01(\t\x12,\n\x08\x66romdate\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x06todate\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06period\x18\x05 \x01(\t\"&\n\x0fZonesTravelTime\x12\x13\n\x0btraveltimes\x18\x01 \x01(\x0c\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_INDICATORSREQUEST = _descriptor.Descriptor(
  name='IndicatorsRequest',
  full_name='gv_proto.proto.IndicatorsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='datatype', full_name='gv_proto.proto.IndicatorsRequest.datatype', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fromdate', full_name='gv_proto.proto.IndicatorsRequest.fromdate', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='todate', full_name='gv_proto.proto.IndicatorsRequest.todate', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='freq', full_name='gv_proto.proto.IndicatorsRequest.freq', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='noeids', full_name='gv_proto.proto.IndicatorsRequest.noeids', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='area', full_name='gv_proto.proto.IndicatorsRequest.area', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='window', full_name='gv_proto.proto.IndicatorsRequest.window', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=271,
)


_INDICATORS = _descriptor.Descriptor(
  name='Indicators',
  full_name='gv_proto.proto.Indicators',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='indicators', full_name='gv_proto.proto.Indicators.indicators', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='applyto', full_name='gv_proto.proto.Indicators.applyto', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=322,
)


_DATAQUALITYREQUEST = _descriptor.Descriptor(
  name='DataQualityRequest',
  full_name='gv_proto.proto.DataQualityRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='datatype', full_name='gv_proto.proto.DataQualityRequest.datatype', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fromdate', full_name='gv_proto.proto.DataQualityRequest.fromdate', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='todate', full_name='gv_proto.proto.DataQualityRequest.todate', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=453,
)


_DATAQUALITY = _descriptor.Descriptor(
  name='DataQuality',
  full_name='gv_proto.proto.DataQuality',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataquality', full_name='gv_proto.proto.DataQuality.dataquality', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=455,
  serialized_end=489,
)


_LOCATIONDATAREQUEST = _descriptor.Descriptor(
  name='LocationDataRequest',
  full_name='gv_proto.proto.LocationDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='datatypeeid', full_name='gv_proto.proto.LocationDataRequest.datatypeeid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='locationeid', full_name='gv_proto.proto.LocationDataRequest.locationeid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fromdate', full_name='gv_proto.proto.LocationDataRequest.fromdate', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='todate', full_name='gv_proto.proto.LocationDataRequest.todate', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period', full_name='gv_proto.proto.LocationDataRequest.period', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=661,
)


_LOCATIONDATA = _descriptor.Descriptor(
  name='LocationData',
  full_name='gv_proto.proto.LocationData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='locationdata', full_name='gv_proto.proto.LocationData.locationdata', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=663,
  serialized_end=699,
)


_ZONESTRAVELTIMEREQUEST = _descriptor.Descriptor(
  name='ZonesTravelTimeRequest',
  full_name='gv_proto.proto.ZonesTravelTimeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fromPoint', full_name='gv_proto.proto.ZonesTravelTimeRequest.fromPoint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='toPoint', full_name='gv_proto.proto.ZonesTravelTimeRequest.toPoint', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fromdate', full_name='gv_proto.proto.ZonesTravelTimeRequest.fromdate', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='todate', full_name='gv_proto.proto.ZonesTravelTimeRequest.todate', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='period', full_name='gv_proto.proto.ZonesTravelTimeRequest.period', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=702,
  serialized_end=868,
)


_ZONESTRAVELTIME = _descriptor.Descriptor(
  name='ZonesTravelTime',
  full_name='gv_proto.proto.ZonesTravelTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='traveltimes', full_name='gv_proto.proto.ZonesTravelTime.traveltimes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=870,
  serialized_end=908,
)

_INDICATORSREQUEST.fields_by_name['fromdate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_INDICATORSREQUEST.fields_by_name['todate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DATAQUALITYREQUEST.fields_by_name['fromdate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DATAQUALITYREQUEST.fields_by_name['todate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOCATIONDATAREQUEST.fields_by_name['fromdate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOCATIONDATAREQUEST.fields_by_name['todate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ZONESTRAVELTIMEREQUEST.fields_by_name['fromdate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ZONESTRAVELTIMEREQUEST.fields_by_name['todate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['IndicatorsRequest'] = _INDICATORSREQUEST
DESCRIPTOR.message_types_by_name['Indicators'] = _INDICATORS
DESCRIPTOR.message_types_by_name['DataQualityRequest'] = _DATAQUALITYREQUEST
DESCRIPTOR.message_types_by_name['DataQuality'] = _DATAQUALITY
DESCRIPTOR.message_types_by_name['LocationDataRequest'] = _LOCATIONDATAREQUEST
DESCRIPTOR.message_types_by_name['LocationData'] = _LOCATIONDATA
DESCRIPTOR.message_types_by_name['ZonesTravelTimeRequest'] = _ZONESTRAVELTIMEREQUEST
DESCRIPTOR.message_types_by_name['ZonesTravelTime'] = _ZONESTRAVELTIME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IndicatorsRequest = _reflection.GeneratedProtocolMessageType('IndicatorsRequest', (_message.Message,), {
  'DESCRIPTOR' : _INDICATORSREQUEST,
  '__module__' : 'gv_proto.proto.archivist_pb2'
  # @@protoc_insertion_point(class_scope:gv_proto.proto.IndicatorsRequest)
  })
_sym_db.RegisterMessage(IndicatorsRequest)

Indicators = _reflection.GeneratedProtocolMessageType('Indicators', (_message.Message,), {
  'DESCRIPTOR' : _INDICATORS,
  '__module__' : 'gv_proto.proto.archivist_pb2'
  # @@protoc_insertion_point(class_scope:gv_proto.proto.Indicators)
  })
_sym_db.RegisterMessage(Indicators)

DataQualityRequest = _reflection.GeneratedProtocolMessageType('DataQualityRequest', (_message.Message,), {
  'DESCRIPTOR' : _DATAQUALITYREQUEST,
  '__module__' : 'gv_proto.proto.archivist_pb2'
  # @@protoc_insertion_point(class_scope:gv_proto.proto.DataQualityRequest)
  })
_sym_db.RegisterMessage(DataQualityRequest)

DataQuality = _reflection.GeneratedProtocolMessageType('DataQuality', (_message.Message,), {
  'DESCRIPTOR' : _DATAQUALITY,
  '__module__' : 'gv_proto.proto.archivist_pb2'
  # @@protoc_insertion_point(class_scope:gv_proto.proto.DataQuality)
  })
_sym_db.RegisterMessage(DataQuality)

LocationDataRequest = _reflection.GeneratedProtocolMessageType('LocationDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONDATAREQUEST,
  '__module__' : 'gv_proto.proto.archivist_pb2'
  # @@protoc_insertion_point(class_scope:gv_proto.proto.LocationDataRequest)
  })
_sym_db.RegisterMessage(LocationDataRequest)

LocationData = _reflection.GeneratedProtocolMessageType('LocationData', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONDATA,
  '__module__' : 'gv_proto.proto.archivist_pb2'
  # @@protoc_insertion_point(class_scope:gv_proto.proto.LocationData)
  })
_sym_db.RegisterMessage(LocationData)

ZonesTravelTimeRequest = _reflection.GeneratedProtocolMessageType('ZonesTravelTimeRequest', (_message.Message,), {
  'DESCRIPTOR' : _ZONESTRAVELTIMEREQUEST,
  '__module__' : 'gv_proto.proto.archivist_pb2'
  # @@protoc_insertion_point(class_scope:gv_proto.proto.ZonesTravelTimeRequest)
  })
_sym_db.RegisterMessage(ZonesTravelTimeRequest)

ZonesTravelTime = _reflection.GeneratedProtocolMessageType('ZonesTravelTime', (_message.Message,), {
  'DESCRIPTOR' : _ZONESTRAVELTIME,
  '__module__' : 'gv_proto.proto.archivist_pb2'
  # @@protoc_insertion_point(class_scope:gv_proto.proto.ZonesTravelTime)
  })
_sym_db.RegisterMessage(ZonesTravelTime)


# @@protoc_insertion_point(module_scope)
