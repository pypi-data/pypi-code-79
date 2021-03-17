# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/v1/domain.proto
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
from spaceone.api.core.v1 import handler_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_handler__pb2
from spaceone.api.core.v1 import tag_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_tag__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spaceone/api/identity/v1/domain.proto',
  package='spaceone.api.identity.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%spaceone/api/identity/v1/domain.proto\x12\x18spaceone.api.identity.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\x1a\"spaceone/api/core/v1/handler.proto\x1a\x1espaceone/api/core/v1/tag.proto\"\xb0\x01\n\x13\x43reateDomainRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x39\n\x0bplugin_info\x18\x02 \x01(\x0b\x32$.spaceone.api.identity.v1.PluginInfo\x12\'\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x04tags\x18\x04 \x03(\x0b\x32\x19.spaceone.api.core.v1.Tag\"\xb5\x01\n\x13UpdateDomainRequest\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x39\n\x0bplugin_info\x18\x02 \x01(\x0b\x32$.spaceone.api.identity.v1.PluginInfo\x12\'\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x04tags\x18\x04 \x03(\x0b\x32\x19.spaceone.api.core.v1.Tag\"\"\n\rDomainRequest\x12\x11\n\tdomain_id\x18\x01 \x01(\t\"3\n\x10GetDomainRequest\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x0c\n\x04only\x18\x02 \x03(\t\"\xc4\x01\n\x0b\x44omainQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12:\n\x05state\x18\x04 \x01(\x0e\x32+.spaceone.api.identity.v1.DomainQuery.State\",\n\x05State\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"\x83\x03\n\nDomainInfo\x12\x11\n\tdomain_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x39\n\x05state\x18\x03 \x01(\x0e\x32*.spaceone.api.identity.v1.DomainInfo.State\x12\x39\n\x0bplugin_info\x18\x04 \x01(\x0b\x32$.spaceone.api.identity.v1.PluginInfo\x12\'\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x04tags\x18\x06 \x03(\x0b\x32\x19.spaceone.api.core.v1.Tag\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\",\n\x05State\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\"Y\n\x0b\x44omainsInfo\x12\x35\n\x07results\x18\x01 \x03(\x0b\x32$.spaceone.api.identity.v1.DomainInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"G\n\x0f\x44omainStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\"m\n\nPluginInfo\x12\x11\n\tplugin_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x11\n\tsecret_id\x18\x03 \x01(\t\x12(\n\x07options\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct2\xfe\x08\n\x06\x44omain\x12{\n\x06\x63reate\x12-.spaceone.api.identity.v1.CreateDomainRequest\x1a$.spaceone.api.identity.v1.DomainInfo\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x14/identity/v1/domains\x12\x86\x01\n\x06update\x12-.spaceone.api.identity.v1.UpdateDomainRequest\x1a$.spaceone.api.identity.v1.DomainInfo\"\'\x82\xd3\xe4\x93\x02!\x1a\x1f/identity/v1/domain/{domain_id}\x12r\n\x06\x64\x65lete\x12\'.spaceone.api.identity.v1.DomainRequest\x1a\x16.google.protobuf.Empty\"\'\x82\xd3\xe4\x93\x02!*\x1f/identity/v1/domain/{domain_id}\x12\x80\x01\n\x06\x65nable\x12\'.spaceone.api.identity.v1.DomainRequest\x1a$.spaceone.api.identity.v1.DomainInfo\"\'\x82\xd3\xe4\x93\x02!\x1a\x1f/identity/v1/domain/{domain_id}\x12\x81\x01\n\x07\x64isable\x12\'.spaceone.api.identity.v1.DomainRequest\x1a$.spaceone.api.identity.v1.DomainInfo\"\'\x82\xd3\xe4\x93\x02!\x1a\x1f/identity/v1/domain/{domain_id}\x12\x80\x01\n\x03get\x12*.spaceone.api.identity.v1.GetDomainRequest\x1a$.spaceone.api.identity.v1.DomainInfo\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/identity/v1/domain/{domain_id}\x12\x91\x01\n\x04list\x12%.spaceone.api.identity.v1.DomainQuery\x1a%.spaceone.api.identity.v1.DomainsInfo\";\x82\xd3\xe4\x93\x02\x35\x12\x14/identity/v1/domainsZ\x1d\"\x1b/identity/v1/domains/search\x12m\n\x04stat\x12).spaceone.api.identity.v1.DomainStatQuery\x1a\x17.google.protobuf.Struct\"!\x82\xd3\xe4\x93\x02\x1b\"\x19/identity/v1/domains/stat\x12m\n\x0eget_public_key\x12+.spaceone.api.core.v1.AuthenticationRequest\x1a,.spaceone.api.core.v1.AuthenticationResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_handler__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_tag__pb2.DESCRIPTOR,])



_DOMAINQUERY_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='spaceone.api.identity.v1.DomainQuery.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
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
  serialized_start=896,
  serialized_end=940,
)
_sym_db.RegisterEnumDescriptor(_DOMAINQUERY_STATE)

_DOMAININFO_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='spaceone.api.identity.v1.DomainInfo.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
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
  serialized_start=896,
  serialized_end=940,
)
_sym_db.RegisterEnumDescriptor(_DOMAININFO_STATE)


_CREATEDOMAINREQUEST = _descriptor.Descriptor(
  name='CreateDomainRequest',
  full_name='spaceone.api.identity.v1.CreateDomainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.identity.v1.CreateDomainRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plugin_info', full_name='spaceone.api.identity.v1.CreateDomainRequest.plugin_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='spaceone.api.identity.v1.CreateDomainRequest.config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.identity.v1.CreateDomainRequest.tags', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=292,
  serialized_end=468,
)


_UPDATEDOMAINREQUEST = _descriptor.Descriptor(
  name='UpdateDomainRequest',
  full_name='spaceone.api.identity.v1.UpdateDomainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.UpdateDomainRequest.domain_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plugin_info', full_name='spaceone.api.identity.v1.UpdateDomainRequest.plugin_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='spaceone.api.identity.v1.UpdateDomainRequest.config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.identity.v1.UpdateDomainRequest.tags', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=471,
  serialized_end=652,
)


_DOMAINREQUEST = _descriptor.Descriptor(
  name='DomainRequest',
  full_name='spaceone.api.identity.v1.DomainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.DomainRequest.domain_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=654,
  serialized_end=688,
)


_GETDOMAINREQUEST = _descriptor.Descriptor(
  name='GetDomainRequest',
  full_name='spaceone.api.identity.v1.GetDomainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.GetDomainRequest.domain_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='only', full_name='spaceone.api.identity.v1.GetDomainRequest.only', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=690,
  serialized_end=741,
)


_DOMAINQUERY = _descriptor.Descriptor(
  name='DomainQuery',
  full_name='spaceone.api.identity.v1.DomainQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.identity.v1.DomainQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.DomainQuery.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.identity.v1.DomainQuery.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='spaceone.api.identity.v1.DomainQuery.state', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DOMAINQUERY_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=744,
  serialized_end=940,
)


_DOMAININFO = _descriptor.Descriptor(
  name='DomainInfo',
  full_name='spaceone.api.identity.v1.DomainInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.DomainInfo.domain_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.identity.v1.DomainInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='spaceone.api.identity.v1.DomainInfo.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plugin_info', full_name='spaceone.api.identity.v1.DomainInfo.plugin_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='spaceone.api.identity.v1.DomainInfo.config', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.identity.v1.DomainInfo.tags', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='spaceone.api.identity.v1.DomainInfo.created_at', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted_at', full_name='spaceone.api.identity.v1.DomainInfo.deleted_at', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DOMAININFO_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=943,
  serialized_end=1330,
)


_DOMAINSINFO = _descriptor.Descriptor(
  name='DomainsInfo',
  full_name='spaceone.api.identity.v1.DomainsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='spaceone.api.identity.v1.DomainsInfo.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='spaceone.api.identity.v1.DomainsInfo.total_count', index=1,
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
  serialized_start=1332,
  serialized_end=1421,
)


_DOMAINSTATQUERY = _descriptor.Descriptor(
  name='DomainStatQuery',
  full_name='spaceone.api.identity.v1.DomainStatQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.identity.v1.DomainStatQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1423,
  serialized_end=1494,
)


_PLUGININFO = _descriptor.Descriptor(
  name='PluginInfo',
  full_name='spaceone.api.identity.v1.PluginInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='plugin_id', full_name='spaceone.api.identity.v1.PluginInfo.plugin_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='spaceone.api.identity.v1.PluginInfo.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret_id', full_name='spaceone.api.identity.v1.PluginInfo.secret_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='options', full_name='spaceone.api.identity.v1.PluginInfo.options', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=1496,
  serialized_end=1605,
)

_CREATEDOMAINREQUEST.fields_by_name['plugin_info'].message_type = _PLUGININFO
_CREATEDOMAINREQUEST.fields_by_name['config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CREATEDOMAINREQUEST.fields_by_name['tags'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_tag__pb2._TAG
_UPDATEDOMAINREQUEST.fields_by_name['plugin_info'].message_type = _PLUGININFO
_UPDATEDOMAINREQUEST.fields_by_name['config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_UPDATEDOMAINREQUEST.fields_by_name['tags'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_tag__pb2._TAG
_DOMAINQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._QUERY
_DOMAINQUERY.fields_by_name['state'].enum_type = _DOMAINQUERY_STATE
_DOMAINQUERY_STATE.containing_type = _DOMAINQUERY
_DOMAININFO.fields_by_name['state'].enum_type = _DOMAININFO_STATE
_DOMAININFO.fields_by_name['plugin_info'].message_type = _PLUGININFO
_DOMAININFO.fields_by_name['config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_DOMAININFO.fields_by_name['tags'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_tag__pb2._TAG
_DOMAININFO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DOMAININFO.fields_by_name['deleted_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DOMAININFO_STATE.containing_type = _DOMAININFO
_DOMAINSINFO.fields_by_name['results'].message_type = _DOMAININFO
_DOMAINSTATQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._STATISTICSQUERY
_PLUGININFO.fields_by_name['options'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['CreateDomainRequest'] = _CREATEDOMAINREQUEST
DESCRIPTOR.message_types_by_name['UpdateDomainRequest'] = _UPDATEDOMAINREQUEST
DESCRIPTOR.message_types_by_name['DomainRequest'] = _DOMAINREQUEST
DESCRIPTOR.message_types_by_name['GetDomainRequest'] = _GETDOMAINREQUEST
DESCRIPTOR.message_types_by_name['DomainQuery'] = _DOMAINQUERY
DESCRIPTOR.message_types_by_name['DomainInfo'] = _DOMAININFO
DESCRIPTOR.message_types_by_name['DomainsInfo'] = _DOMAINSINFO
DESCRIPTOR.message_types_by_name['DomainStatQuery'] = _DOMAINSTATQUERY
DESCRIPTOR.message_types_by_name['PluginInfo'] = _PLUGININFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateDomainRequest = _reflection.GeneratedProtocolMessageType('CreateDomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDOMAINREQUEST,
  '__module__' : 'spaceone.api.identity.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.CreateDomainRequest)
  })
_sym_db.RegisterMessage(CreateDomainRequest)

UpdateDomainRequest = _reflection.GeneratedProtocolMessageType('UpdateDomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDOMAINREQUEST,
  '__module__' : 'spaceone.api.identity.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.UpdateDomainRequest)
  })
_sym_db.RegisterMessage(UpdateDomainRequest)

DomainRequest = _reflection.GeneratedProtocolMessageType('DomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOMAINREQUEST,
  '__module__' : 'spaceone.api.identity.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.DomainRequest)
  })
_sym_db.RegisterMessage(DomainRequest)

GetDomainRequest = _reflection.GeneratedProtocolMessageType('GetDomainRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDOMAINREQUEST,
  '__module__' : 'spaceone.api.identity.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.GetDomainRequest)
  })
_sym_db.RegisterMessage(GetDomainRequest)

DomainQuery = _reflection.GeneratedProtocolMessageType('DomainQuery', (_message.Message,), {
  'DESCRIPTOR' : _DOMAINQUERY,
  '__module__' : 'spaceone.api.identity.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.DomainQuery)
  })
_sym_db.RegisterMessage(DomainQuery)

DomainInfo = _reflection.GeneratedProtocolMessageType('DomainInfo', (_message.Message,), {
  'DESCRIPTOR' : _DOMAININFO,
  '__module__' : 'spaceone.api.identity.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.DomainInfo)
  })
_sym_db.RegisterMessage(DomainInfo)

DomainsInfo = _reflection.GeneratedProtocolMessageType('DomainsInfo', (_message.Message,), {
  'DESCRIPTOR' : _DOMAINSINFO,
  '__module__' : 'spaceone.api.identity.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.DomainsInfo)
  })
_sym_db.RegisterMessage(DomainsInfo)

DomainStatQuery = _reflection.GeneratedProtocolMessageType('DomainStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _DOMAINSTATQUERY,
  '__module__' : 'spaceone.api.identity.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.DomainStatQuery)
  })
_sym_db.RegisterMessage(DomainStatQuery)

PluginInfo = _reflection.GeneratedProtocolMessageType('PluginInfo', (_message.Message,), {
  'DESCRIPTOR' : _PLUGININFO,
  '__module__' : 'spaceone.api.identity.v1.domain_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.PluginInfo)
  })
_sym_db.RegisterMessage(PluginInfo)



_DOMAIN = _descriptor.ServiceDescriptor(
  name='Domain',
  full_name='spaceone.api.identity.v1.Domain',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1608,
  serialized_end=2758,
  methods=[
  _descriptor.MethodDescriptor(
    name='create',
    full_name='spaceone.api.identity.v1.Domain.create',
    index=0,
    containing_service=None,
    input_type=_CREATEDOMAINREQUEST,
    output_type=_DOMAININFO,
    serialized_options=b'\202\323\344\223\002\026\"\024/identity/v1/domains',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='spaceone.api.identity.v1.Domain.update',
    index=1,
    containing_service=None,
    input_type=_UPDATEDOMAINREQUEST,
    output_type=_DOMAININFO,
    serialized_options=b'\202\323\344\223\002!\032\037/identity/v1/domain/{domain_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='spaceone.api.identity.v1.Domain.delete',
    index=2,
    containing_service=None,
    input_type=_DOMAINREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002!*\037/identity/v1/domain/{domain_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='enable',
    full_name='spaceone.api.identity.v1.Domain.enable',
    index=3,
    containing_service=None,
    input_type=_DOMAINREQUEST,
    output_type=_DOMAININFO,
    serialized_options=b'\202\323\344\223\002!\032\037/identity/v1/domain/{domain_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='disable',
    full_name='spaceone.api.identity.v1.Domain.disable',
    index=4,
    containing_service=None,
    input_type=_DOMAINREQUEST,
    output_type=_DOMAININFO,
    serialized_options=b'\202\323\344\223\002!\032\037/identity/v1/domain/{domain_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='spaceone.api.identity.v1.Domain.get',
    index=5,
    containing_service=None,
    input_type=_GETDOMAINREQUEST,
    output_type=_DOMAININFO,
    serialized_options=b'\202\323\344\223\002!\022\037/identity/v1/domain/{domain_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='list',
    full_name='spaceone.api.identity.v1.Domain.list',
    index=6,
    containing_service=None,
    input_type=_DOMAINQUERY,
    output_type=_DOMAINSINFO,
    serialized_options=b'\202\323\344\223\0025\022\024/identity/v1/domainsZ\035\"\033/identity/v1/domains/search',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stat',
    full_name='spaceone.api.identity.v1.Domain.stat',
    index=7,
    containing_service=None,
    input_type=_DOMAINSTATQUERY,
    output_type=google_dot_protobuf_dot_struct__pb2._STRUCT,
    serialized_options=b'\202\323\344\223\002\033\"\031/identity/v1/domains/stat',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_public_key',
    full_name='spaceone.api.identity.v1.Domain.get_public_key',
    index=8,
    containing_service=None,
    input_type=spaceone_dot_api_dot_core_dot_v1_dot_handler__pb2._AUTHENTICATIONREQUEST,
    output_type=spaceone_dot_api_dot_core_dot_v1_dot_handler__pb2._AUTHENTICATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DOMAIN)

DESCRIPTOR.services_by_name['Domain'] = _DOMAIN

# @@protoc_insertion_point(module_scope)
