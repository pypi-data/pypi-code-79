# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/cost_saving/v1/statistic.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spaceone/api/cost_saving/v1/statistic.proto',
  package='spaceone.api.cost_saving.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+spaceone/api/cost_saving/v1/statistic.proto\x12\x1bspaceone.api.cost_saving.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\x9e\x01\n\x0eStatisticQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\x12\n\nstart_hour\x18\x04 \x01(\t\x12\x10\n\x08\x65nd_hour\x18\x05 \x01(\t\x12\x13\n\x0b\x61ggregation\x18\x06 \x01(\x05\"]\n\x12StatisticStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"\xd1\x02\n\rStatisticInfo\x12\x1b\n\x13\x63ost_saving_stat_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\x11\n\tsaving_by\x18\x04 \x01(\t\x12\x13\n\x0b\x65nvironment\x18\x05 \x01(\t\x12\x10\n\x08provider\x18\x06 \x01(\t\x12\x0e\n\x06region\x18\x07 \x01(\t\x12\x15\n\rresource_type\x18\x08 \x01(\t\x12\x0c\n\x04\x63ost\x18\x0b \x01(\x02\x12.\n\ncreated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tupdate_at\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nexpired_at\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"b\n\x0eStatisticsInfo\x12;\n\x07results\x18\x01 \x03(\x0b\x32*.spaceone.api.cost_saving.v1.StatisticInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x32\xb2\x02\n\tStatistic\x12\xa9\x01\n\x04list\x12+.spaceone.api.cost_saving.v1.StatisticQuery\x1a+.spaceone.api.cost_saving.v1.StatisticsInfo\"G\x82\xd3\xe4\x93\x02\x41\x12\x1a/cost-saving/v1/statisticsZ#\"!/cost-saving/v1/statistics/search\x12y\n\x04stat\x12/.spaceone.api.cost_saving.v1.StatisticStatQuery\x1a\x17.google.protobuf.Struct\"\'\x82\xd3\xe4\x93\x02!\"\x1f/cost-saving/v1/statistics/statb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.DESCRIPTOR,])




_STATISTICQUERY = _descriptor.Descriptor(
  name='StatisticQuery',
  full_name='spaceone.api.cost_saving.v1.StatisticQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.cost_saving.v1.StatisticQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.cost_saving.v1.StatisticQuery.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='spaceone.api.cost_saving.v1.StatisticQuery.project_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_hour', full_name='spaceone.api.cost_saving.v1.StatisticQuery.start_hour', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_hour', full_name='spaceone.api.cost_saving.v1.StatisticQuery.end_hour', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aggregation', full_name='spaceone.api.cost_saving.v1.StatisticQuery.aggregation', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=204,
  serialized_end=362,
)


_STATISTICSTATQUERY = _descriptor.Descriptor(
  name='StatisticStatQuery',
  full_name='spaceone.api.cost_saving.v1.StatisticStatQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.cost_saving.v1.StatisticStatQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.cost_saving.v1.StatisticStatQuery.domain_id', index=1,
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
  serialized_start=364,
  serialized_end=457,
)


_STATISTICINFO = _descriptor.Descriptor(
  name='StatisticInfo',
  full_name='spaceone.api.cost_saving.v1.StatisticInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cost_saving_stat_id', full_name='spaceone.api.cost_saving.v1.StatisticInfo.cost_saving_stat_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.cost_saving.v1.StatisticInfo.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='spaceone.api.cost_saving.v1.StatisticInfo.project_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='saving_by', full_name='spaceone.api.cost_saving.v1.StatisticInfo.saving_by', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environment', full_name='spaceone.api.cost_saving.v1.StatisticInfo.environment', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider', full_name='spaceone.api.cost_saving.v1.StatisticInfo.provider', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region', full_name='spaceone.api.cost_saving.v1.StatisticInfo.region', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='spaceone.api.cost_saving.v1.StatisticInfo.resource_type', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost', full_name='spaceone.api.cost_saving.v1.StatisticInfo.cost', index=8,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='spaceone.api.cost_saving.v1.StatisticInfo.created_at', index=9,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_at', full_name='spaceone.api.cost_saving.v1.StatisticInfo.update_at', index=10,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expired_at', full_name='spaceone.api.cost_saving.v1.StatisticInfo.expired_at', index=11,
      number=23, type=11, cpp_type=10, label=1,
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
  serialized_start=460,
  serialized_end=797,
)


_STATISTICSINFO = _descriptor.Descriptor(
  name='StatisticsInfo',
  full_name='spaceone.api.cost_saving.v1.StatisticsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='spaceone.api.cost_saving.v1.StatisticsInfo.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='spaceone.api.cost_saving.v1.StatisticsInfo.total_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=799,
  serialized_end=897,
)

_STATISTICQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._QUERY
_STATISTICSTATQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._STATISTICSQUERY
_STATISTICINFO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STATISTICINFO.fields_by_name['update_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STATISTICINFO.fields_by_name['expired_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STATISTICSINFO.fields_by_name['results'].message_type = _STATISTICINFO
DESCRIPTOR.message_types_by_name['StatisticQuery'] = _STATISTICQUERY
DESCRIPTOR.message_types_by_name['StatisticStatQuery'] = _STATISTICSTATQUERY
DESCRIPTOR.message_types_by_name['StatisticInfo'] = _STATISTICINFO
DESCRIPTOR.message_types_by_name['StatisticsInfo'] = _STATISTICSINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatisticQuery = _reflection.GeneratedProtocolMessageType('StatisticQuery', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICQUERY,
  '__module__' : 'spaceone.api.cost_saving.v1.statistic_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.StatisticQuery)
  })
_sym_db.RegisterMessage(StatisticQuery)

StatisticStatQuery = _reflection.GeneratedProtocolMessageType('StatisticStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICSTATQUERY,
  '__module__' : 'spaceone.api.cost_saving.v1.statistic_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.StatisticStatQuery)
  })
_sym_db.RegisterMessage(StatisticStatQuery)

StatisticInfo = _reflection.GeneratedProtocolMessageType('StatisticInfo', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICINFO,
  '__module__' : 'spaceone.api.cost_saving.v1.statistic_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.StatisticInfo)
  })
_sym_db.RegisterMessage(StatisticInfo)

StatisticsInfo = _reflection.GeneratedProtocolMessageType('StatisticsInfo', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICSINFO,
  '__module__' : 'spaceone.api.cost_saving.v1.statistic_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.cost_saving.v1.StatisticsInfo)
  })
_sym_db.RegisterMessage(StatisticsInfo)



_STATISTIC = _descriptor.ServiceDescriptor(
  name='Statistic',
  full_name='spaceone.api.cost_saving.v1.Statistic',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=900,
  serialized_end=1206,
  methods=[
  _descriptor.MethodDescriptor(
    name='list',
    full_name='spaceone.api.cost_saving.v1.Statistic.list',
    index=0,
    containing_service=None,
    input_type=_STATISTICQUERY,
    output_type=_STATISTICSINFO,
    serialized_options=b'\202\323\344\223\002A\022\032/cost-saving/v1/statisticsZ#\"!/cost-saving/v1/statistics/search',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stat',
    full_name='spaceone.api.cost_saving.v1.Statistic.stat',
    index=1,
    containing_service=None,
    input_type=_STATISTICSTATQUERY,
    output_type=google_dot_protobuf_dot_struct__pb2._STRUCT,
    serialized_options=b'\202\323\344\223\002!\"\037/cost-saving/v1/statistics/stat',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STATISTIC)

DESCRIPTOR.services_by_name['Statistic'] = _STATISTIC

# @@protoc_insertion_point(module_scope)
