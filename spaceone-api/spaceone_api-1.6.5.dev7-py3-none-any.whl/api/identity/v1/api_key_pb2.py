# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/v1/api_key.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spaceone/api/identity/v1/api_key.proto',
  package='spaceone.api.identity.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&spaceone/api/identity/v1/api_key.proto\x12\x18spaceone.api.identity.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"9\n\x13\x43reateAPIKeyRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"6\n\rAPIKeyRequest\x12\x12\n\napi_key_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"G\n\x10GetAPIKeyRequest\x12\x12\n\napi_key_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\xaa\x02\n\nAPIKeyInfo\x12\x12\n\napi_key_id\x18\x01 \x01(\t\x12\x0f\n\x07\x61pi_key\x18\x02 \x01(\t\x12\x39\n\x05state\x18\x03 \x01(\x0e\x32*.spaceone.api.identity.v1.APIKeyInfo.State\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x11\n\tdomain_id\x18\x05 \x01(\t\x12\x34\n\x10last_accessed_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ncreated_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"2\n\x05State\x12\x0e\n\nNONE_STATE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"\xe1\x01\n\x0b\x41PIKeyQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x12\n\napi_key_id\x18\x02 \x01(\t\x12:\n\x05state\x18\x03 \x01(\x0e\x32+.spaceone.api.identity.v1.APIKeyQuery.State\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x11\n\tdomain_id\x18\x05 \x01(\t\"2\n\x05State\x12\x0e\n\nNONE_STATE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"Y\n\x0b\x41PIKeysInfo\x12\x35\n\x07results\x18\x01 \x03(\x0b\x32$.spaceone.api.identity.v1.APIKeyInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"Z\n\x0f\x41PIKeyStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\xa1\x07\n\x06\x41PIKey\x12|\n\x06\x63reate\x12-.spaceone.api.identity.v1.CreateAPIKeyRequest\x1a$.spaceone.api.identity.v1.APIKeyInfo\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x15/identity/v1/api-keys\x12\x89\x01\n\x06\x65nable\x12\'.spaceone.api.identity.v1.APIKeyRequest\x1a$.spaceone.api.identity.v1.APIKeyInfo\"0\x82\xd3\xe4\x93\x02*\x1a(/identity/v1/api-key/{api_key_id}/enable\x12\x8b\x01\n\x07\x64isable\x12\'.spaceone.api.identity.v1.APIKeyRequest\x1a$.spaceone.api.identity.v1.APIKeyInfo\"1\x82\xd3\xe4\x93\x02+\x1a)/identity/v1/api-key/{api_key_id}/disable\x12t\n\x06\x64\x65lete\x12\'.spaceone.api.identity.v1.APIKeyRequest\x1a\x16.google.protobuf.Empty\")\x82\xd3\xe4\x93\x02#*!/identity/v1/api-key/{api_key_id}\x12\x82\x01\n\x03get\x12*.spaceone.api.identity.v1.GetAPIKeyRequest\x1a$.spaceone.api.identity.v1.APIKeyInfo\")\x82\xd3\xe4\x93\x02#\x12!/identity/v1/api-key/{api_key_id}\x12\x93\x01\n\x04list\x12%.spaceone.api.identity.v1.APIKeyQuery\x1a%.spaceone.api.identity.v1.APIKeysInfo\"=\x82\xd3\xe4\x93\x02\x37\x12\x15/identity/v1/api-keysZ\x1e\"\x1c/identity/v1/api-keys/search\x12n\n\x04stat\x12).spaceone.api.identity.v1.APIKeyStatQuery\x1a\x17.google.protobuf.Struct\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/identity/v1/api-keys/statb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.DESCRIPTOR,])



_APIKEYINFO_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='spaceone.api.identity.v1.APIKeyInfo.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_STATE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=661,
  serialized_end=711,
)
_sym_db.RegisterEnumDescriptor(_APIKEYINFO_STATE)

_APIKEYQUERY_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='spaceone.api.identity.v1.APIKeyQuery.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE_STATE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=661,
  serialized_end=711,
)
_sym_db.RegisterEnumDescriptor(_APIKEYQUERY_STATE)


_CREATEAPIKEYREQUEST = _descriptor.Descriptor(
  name='CreateAPIKeyRequest',
  full_name='spaceone.api.identity.v1.CreateAPIKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='spaceone.api.identity.v1.CreateAPIKeyRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.CreateAPIKeyRequest.domain_id', index=1,
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
  serialized_start=224,
  serialized_end=281,
)


_APIKEYREQUEST = _descriptor.Descriptor(
  name='APIKeyRequest',
  full_name='spaceone.api.identity.v1.APIKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_key_id', full_name='spaceone.api.identity.v1.APIKeyRequest.api_key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.APIKeyRequest.domain_id', index=1,
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
  serialized_start=283,
  serialized_end=337,
)


_GETAPIKEYREQUEST = _descriptor.Descriptor(
  name='GetAPIKeyRequest',
  full_name='spaceone.api.identity.v1.GetAPIKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_key_id', full_name='spaceone.api.identity.v1.GetAPIKeyRequest.api_key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.GetAPIKeyRequest.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='only', full_name='spaceone.api.identity.v1.GetAPIKeyRequest.only', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=339,
  serialized_end=410,
)


_APIKEYINFO = _descriptor.Descriptor(
  name='APIKeyInfo',
  full_name='spaceone.api.identity.v1.APIKeyInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_key_id', full_name='spaceone.api.identity.v1.APIKeyInfo.api_key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='api_key', full_name='spaceone.api.identity.v1.APIKeyInfo.api_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='spaceone.api.identity.v1.APIKeyInfo.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='spaceone.api.identity.v1.APIKeyInfo.user_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.APIKeyInfo.domain_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_accessed_at', full_name='spaceone.api.identity.v1.APIKeyInfo.last_accessed_at', index=5,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='spaceone.api.identity.v1.APIKeyInfo.created_at', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _APIKEYINFO_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=711,
)


_APIKEYQUERY = _descriptor.Descriptor(
  name='APIKeyQuery',
  full_name='spaceone.api.identity.v1.APIKeyQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.identity.v1.APIKeyQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='api_key_id', full_name='spaceone.api.identity.v1.APIKeyQuery.api_key_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='spaceone.api.identity.v1.APIKeyQuery.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='spaceone.api.identity.v1.APIKeyQuery.user_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.APIKeyQuery.domain_id', index=4,
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
    _APIKEYQUERY_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=714,
  serialized_end=939,
)


_APIKEYSINFO = _descriptor.Descriptor(
  name='APIKeysInfo',
  full_name='spaceone.api.identity.v1.APIKeysInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='spaceone.api.identity.v1.APIKeysInfo.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='spaceone.api.identity.v1.APIKeysInfo.total_count', index=1,
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
  serialized_start=941,
  serialized_end=1030,
)


_APIKEYSTATQUERY = _descriptor.Descriptor(
  name='APIKeyStatQuery',
  full_name='spaceone.api.identity.v1.APIKeyStatQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.identity.v1.APIKeyStatQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.APIKeyStatQuery.domain_id', index=1,
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
  serialized_start=1032,
  serialized_end=1122,
)

_APIKEYINFO.fields_by_name['state'].enum_type = _APIKEYINFO_STATE
_APIKEYINFO.fields_by_name['last_accessed_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_APIKEYINFO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_APIKEYINFO_STATE.containing_type = _APIKEYINFO
_APIKEYQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._QUERY
_APIKEYQUERY.fields_by_name['state'].enum_type = _APIKEYQUERY_STATE
_APIKEYQUERY_STATE.containing_type = _APIKEYQUERY
_APIKEYSINFO.fields_by_name['results'].message_type = _APIKEYINFO
_APIKEYSTATQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._STATISTICSQUERY
DESCRIPTOR.message_types_by_name['CreateAPIKeyRequest'] = _CREATEAPIKEYREQUEST
DESCRIPTOR.message_types_by_name['APIKeyRequest'] = _APIKEYREQUEST
DESCRIPTOR.message_types_by_name['GetAPIKeyRequest'] = _GETAPIKEYREQUEST
DESCRIPTOR.message_types_by_name['APIKeyInfo'] = _APIKEYINFO
DESCRIPTOR.message_types_by_name['APIKeyQuery'] = _APIKEYQUERY
DESCRIPTOR.message_types_by_name['APIKeysInfo'] = _APIKEYSINFO
DESCRIPTOR.message_types_by_name['APIKeyStatQuery'] = _APIKEYSTATQUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateAPIKeyRequest = _reflection.GeneratedProtocolMessageType('CreateAPIKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAPIKEYREQUEST,
  '__module__' : 'spaceone.api.identity.v1.api_key_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.CreateAPIKeyRequest)
  })
_sym_db.RegisterMessage(CreateAPIKeyRequest)

APIKeyRequest = _reflection.GeneratedProtocolMessageType('APIKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _APIKEYREQUEST,
  '__module__' : 'spaceone.api.identity.v1.api_key_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.APIKeyRequest)
  })
_sym_db.RegisterMessage(APIKeyRequest)

GetAPIKeyRequest = _reflection.GeneratedProtocolMessageType('GetAPIKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAPIKEYREQUEST,
  '__module__' : 'spaceone.api.identity.v1.api_key_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.GetAPIKeyRequest)
  })
_sym_db.RegisterMessage(GetAPIKeyRequest)

APIKeyInfo = _reflection.GeneratedProtocolMessageType('APIKeyInfo', (_message.Message,), {
  'DESCRIPTOR' : _APIKEYINFO,
  '__module__' : 'spaceone.api.identity.v1.api_key_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.APIKeyInfo)
  })
_sym_db.RegisterMessage(APIKeyInfo)

APIKeyQuery = _reflection.GeneratedProtocolMessageType('APIKeyQuery', (_message.Message,), {
  'DESCRIPTOR' : _APIKEYQUERY,
  '__module__' : 'spaceone.api.identity.v1.api_key_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.APIKeyQuery)
  })
_sym_db.RegisterMessage(APIKeyQuery)

APIKeysInfo = _reflection.GeneratedProtocolMessageType('APIKeysInfo', (_message.Message,), {
  'DESCRIPTOR' : _APIKEYSINFO,
  '__module__' : 'spaceone.api.identity.v1.api_key_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.APIKeysInfo)
  })
_sym_db.RegisterMessage(APIKeysInfo)

APIKeyStatQuery = _reflection.GeneratedProtocolMessageType('APIKeyStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _APIKEYSTATQUERY,
  '__module__' : 'spaceone.api.identity.v1.api_key_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.APIKeyStatQuery)
  })
_sym_db.RegisterMessage(APIKeyStatQuery)



_APIKEY = _descriptor.ServiceDescriptor(
  name='APIKey',
  full_name='spaceone.api.identity.v1.APIKey',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1125,
  serialized_end=2054,
  methods=[
  _descriptor.MethodDescriptor(
    name='create',
    full_name='spaceone.api.identity.v1.APIKey.create',
    index=0,
    containing_service=None,
    input_type=_CREATEAPIKEYREQUEST,
    output_type=_APIKEYINFO,
    serialized_options=b'\202\323\344\223\002\027\"\025/identity/v1/api-keys',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='enable',
    full_name='spaceone.api.identity.v1.APIKey.enable',
    index=1,
    containing_service=None,
    input_type=_APIKEYREQUEST,
    output_type=_APIKEYINFO,
    serialized_options=b'\202\323\344\223\002*\032(/identity/v1/api-key/{api_key_id}/enable',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='disable',
    full_name='spaceone.api.identity.v1.APIKey.disable',
    index=2,
    containing_service=None,
    input_type=_APIKEYREQUEST,
    output_type=_APIKEYINFO,
    serialized_options=b'\202\323\344\223\002+\032)/identity/v1/api-key/{api_key_id}/disable',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='spaceone.api.identity.v1.APIKey.delete',
    index=3,
    containing_service=None,
    input_type=_APIKEYREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002#*!/identity/v1/api-key/{api_key_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='spaceone.api.identity.v1.APIKey.get',
    index=4,
    containing_service=None,
    input_type=_GETAPIKEYREQUEST,
    output_type=_APIKEYINFO,
    serialized_options=b'\202\323\344\223\002#\022!/identity/v1/api-key/{api_key_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='list',
    full_name='spaceone.api.identity.v1.APIKey.list',
    index=5,
    containing_service=None,
    input_type=_APIKEYQUERY,
    output_type=_APIKEYSINFO,
    serialized_options=b'\202\323\344\223\0027\022\025/identity/v1/api-keysZ\036\"\034/identity/v1/api-keys/search',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stat',
    full_name='spaceone.api.identity.v1.APIKey.stat',
    index=6,
    containing_service=None,
    input_type=_APIKEYSTATQUERY,
    output_type=google_dot_protobuf_dot_struct__pb2._STRUCT,
    serialized_options=b'\202\323\344\223\002\034\"\032/identity/v1/api-keys/stat',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_APIKEY)

DESCRIPTOR.services_by_name['APIKey'] = _APIKEY

# @@protoc_insertion_point(module_scope)
