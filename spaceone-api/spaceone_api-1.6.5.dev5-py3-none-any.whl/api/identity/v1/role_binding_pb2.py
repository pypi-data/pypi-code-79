# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/v1/role_binding.proto
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
from spaceone.api.core.v1 import tag_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_tag__pb2
from spaceone.api.identity.v1 import project_pb2 as spaceone_dot_api_dot_identity_dot_v1_dot_project__pb2
from spaceone.api.identity.v1 import project_group_pb2 as spaceone_dot_api_dot_identity_dot_v1_dot_project__group__pb2
from spaceone.api.identity.v1 import role_pb2 as spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spaceone/api/identity/v1/role_binding.proto',
  package='spaceone.api.identity.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+spaceone/api/identity/v1/role_binding.proto\x12\x18spaceone.api.identity.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\x1a\x1espaceone/api/core/v1/tag.proto\x1a&spaceone/api/identity/v1/project.proto\x1a,spaceone/api/identity/v1/project_group.proto\x1a#spaceone/api/identity/v1/role.proto\"\xd1\x01\n\x18\x43reateRoleBindingRequest\x12\x15\n\rresource_type\x18\x01 \x01(\t\x12\x13\n\x0bresource_id\x18\x02 \x01(\t\x12\x0f\n\x07role_id\x18\x03 \x01(\t\x12\x12\n\nproject_id\x18\x04 \x01(\t\x12\x18\n\x10project_group_id\x18\x05 \x01(\t\x12\x0e\n\x06labels\x18\x06 \x03(\t\x12\'\n\x04tags\x18\x07 \x03(\x0b\x32\x19.spaceone.api.core.v1.Tag\x12\x11\n\tdomain_id\x18\x08 \x01(\t\"\x7f\n\x18UpdateRoleBindingRequest\x12\x17\n\x0frole_binding_id\x18\x01 \x01(\t\x12\x0e\n\x06labels\x18\x02 \x03(\t\x12\'\n\x04tags\x18\x03 \x03(\x0b\x32\x19.spaceone.api.core.v1.Tag\x12\x11\n\tdomain_id\x18\x04 \x01(\t\"@\n\x12RoleBindingRequest\x12\x17\n\x0frole_binding_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"Q\n\x15GetRoleBindingRequest\x12\x17\n\x0frole_binding_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\x8e\x03\n\x0fRoleBindingInfo\x12\x17\n\x0frole_binding_id\x18\x01 \x01(\t\x12\x15\n\rresource_type\x18\x02 \x01(\t\x12\x13\n\x0bresource_id\x18\x03 \x01(\t\x12\x35\n\trole_info\x18\x04 \x01(\x0b\x32\".spaceone.api.identity.v1.RoleInfo\x12;\n\x0cproject_info\x18\x05 \x01(\x0b\x32%.spaceone.api.identity.v1.ProjectInfo\x12\x46\n\x12project_group_info\x18\x06 \x01(\x0b\x32*.spaceone.api.identity.v1.ProjectGroupInfo\x12\x0e\n\x06labels\x18\x07 \x03(\t\x12\'\n\x04tags\x18\x08 \x03(\x0b\x32\x19.spaceone.api.core.v1.Tag\x12\x11\n\tdomain_id\x18\x0b \x01(\t\x12.\n\ncreated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xe8\x01\n\x10RoleBindingQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x17\n\x0frole_binding_id\x18\x02 \x01(\t\x12\x15\n\rresource_type\x18\x03 \x01(\t\x12\x13\n\x0bresource_id\x18\x04 \x01(\t\x12\x0f\n\x07role_id\x18\x05 \x01(\t\x12\x11\n\trole_type\x18\x06 \x01(\t\x12\x12\n\nproject_id\x18\x07 \x01(\t\x12\x18\n\x10project_group_id\x18\x08 \x01(\t\x12\x11\n\tdomain_id\x18\t \x01(\t\"c\n\x10RoleBindingsInfo\x12:\n\x07results\x18\x01 \x03(\x0b\x32).spaceone.api.identity.v1.RoleBindingInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"_\n\x14RoleBindingStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\xf8\x06\n\x0bRoleBinding\x12\x8b\x01\n\x06\x63reate\x12\x32.spaceone.api.identity.v1.CreateRoleBindingRequest\x1a).spaceone.api.identity.v1.RoleBindingInfo\"\"\x82\xd3\xe4\x93\x02\x1c\"\x1a/identity/v1/role-bindings\x12\x9d\x01\n\x06update\x12\x32.spaceone.api.identity.v1.UpdateRoleBindingRequest\x1a).spaceone.api.identity.v1.RoleBindingInfo\"4\x82\xd3\xe4\x93\x02.\x1a,/identity/v1/role-bindings/{role_binding_id}\x12\x84\x01\n\x06\x64\x65lete\x12,.spaceone.api.identity.v1.RoleBindingRequest\x1a\x16.google.protobuf.Empty\"4\x82\xd3\xe4\x93\x02.*,/identity/v1/role-bindings/{role_binding_id}\x12\x97\x01\n\x03get\x12/.spaceone.api.identity.v1.GetRoleBindingRequest\x1a).spaceone.api.identity.v1.RoleBindingInfo\"4\x82\xd3\xe4\x93\x02.\x12,/identity/v1/role-bindings/{role_binding_id}\x12\xa7\x01\n\x04list\x12*.spaceone.api.identity.v1.RoleBindingQuery\x1a*.spaceone.api.identity.v1.RoleBindingsInfo\"G\x82\xd3\xe4\x93\x02\x41\x12\x1a/identity/v1/role-bindingsZ#\"!/identity/v1/role-bindings/search\x12p\n\x04stat\x12..spaceone.api.identity.v1.RoleBindingStatQuery\x1a\x17.google.protobuf.Struct\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x17/identity/v1/roles/statb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_tag__pb2.DESCRIPTOR,spaceone_dot_api_dot_identity_dot_v1_dot_project__pb2.DESCRIPTOR,spaceone_dot_api_dot_identity_dot_v1_dot_project__group__pb2.DESCRIPTOR,spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.DESCRIPTOR,])




_CREATEROLEBINDINGREQUEST = _descriptor.Descriptor(
  name='CreateRoleBindingRequest',
  full_name='spaceone.api.identity.v1.CreateRoleBindingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='spaceone.api.identity.v1.CreateRoleBindingRequest.resource_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='spaceone.api.identity.v1.CreateRoleBindingRequest.resource_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='spaceone.api.identity.v1.CreateRoleBindingRequest.role_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='spaceone.api.identity.v1.CreateRoleBindingRequest.project_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_group_id', full_name='spaceone.api.identity.v1.CreateRoleBindingRequest.project_group_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='spaceone.api.identity.v1.CreateRoleBindingRequest.labels', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.identity.v1.CreateRoleBindingRequest.tags', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.CreateRoleBindingRequest.domain_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=385,
  serialized_end=594,
)


_UPDATEROLEBINDINGREQUEST = _descriptor.Descriptor(
  name='UpdateRoleBindingRequest',
  full_name='spaceone.api.identity.v1.UpdateRoleBindingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_binding_id', full_name='spaceone.api.identity.v1.UpdateRoleBindingRequest.role_binding_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='spaceone.api.identity.v1.UpdateRoleBindingRequest.labels', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.identity.v1.UpdateRoleBindingRequest.tags', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.UpdateRoleBindingRequest.domain_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=596,
  serialized_end=723,
)


_ROLEBINDINGREQUEST = _descriptor.Descriptor(
  name='RoleBindingRequest',
  full_name='spaceone.api.identity.v1.RoleBindingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_binding_id', full_name='spaceone.api.identity.v1.RoleBindingRequest.role_binding_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.RoleBindingRequest.domain_id', index=1,
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
  serialized_start=725,
  serialized_end=789,
)


_GETROLEBINDINGREQUEST = _descriptor.Descriptor(
  name='GetRoleBindingRequest',
  full_name='spaceone.api.identity.v1.GetRoleBindingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_binding_id', full_name='spaceone.api.identity.v1.GetRoleBindingRequest.role_binding_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.GetRoleBindingRequest.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='only', full_name='spaceone.api.identity.v1.GetRoleBindingRequest.only', index=2,
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
  serialized_start=791,
  serialized_end=872,
)


_ROLEBINDINGINFO = _descriptor.Descriptor(
  name='RoleBindingInfo',
  full_name='spaceone.api.identity.v1.RoleBindingInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_binding_id', full_name='spaceone.api.identity.v1.RoleBindingInfo.role_binding_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='spaceone.api.identity.v1.RoleBindingInfo.resource_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='spaceone.api.identity.v1.RoleBindingInfo.resource_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_info', full_name='spaceone.api.identity.v1.RoleBindingInfo.role_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_info', full_name='spaceone.api.identity.v1.RoleBindingInfo.project_info', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_group_info', full_name='spaceone.api.identity.v1.RoleBindingInfo.project_group_info', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='spaceone.api.identity.v1.RoleBindingInfo.labels', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.identity.v1.RoleBindingInfo.tags', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.RoleBindingInfo.domain_id', index=8,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='spaceone.api.identity.v1.RoleBindingInfo.created_at', index=9,
      number=21, type=11, cpp_type=10, label=1,
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
  serialized_start=875,
  serialized_end=1273,
)


_ROLEBINDINGQUERY = _descriptor.Descriptor(
  name='RoleBindingQuery',
  full_name='spaceone.api.identity.v1.RoleBindingQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.identity.v1.RoleBindingQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_binding_id', full_name='spaceone.api.identity.v1.RoleBindingQuery.role_binding_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='spaceone.api.identity.v1.RoleBindingQuery.resource_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='spaceone.api.identity.v1.RoleBindingQuery.resource_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='spaceone.api.identity.v1.RoleBindingQuery.role_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_type', full_name='spaceone.api.identity.v1.RoleBindingQuery.role_type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='spaceone.api.identity.v1.RoleBindingQuery.project_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_group_id', full_name='spaceone.api.identity.v1.RoleBindingQuery.project_group_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.RoleBindingQuery.domain_id', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=1276,
  serialized_end=1508,
)


_ROLEBINDINGSINFO = _descriptor.Descriptor(
  name='RoleBindingsInfo',
  full_name='spaceone.api.identity.v1.RoleBindingsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='spaceone.api.identity.v1.RoleBindingsInfo.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='spaceone.api.identity.v1.RoleBindingsInfo.total_count', index=1,
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
  serialized_start=1510,
  serialized_end=1609,
)


_ROLEBINDINGSTATQUERY = _descriptor.Descriptor(
  name='RoleBindingStatQuery',
  full_name='spaceone.api.identity.v1.RoleBindingStatQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.identity.v1.RoleBindingStatQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.RoleBindingStatQuery.domain_id', index=1,
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
  serialized_start=1611,
  serialized_end=1706,
)

_CREATEROLEBINDINGREQUEST.fields_by_name['tags'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_tag__pb2._TAG
_UPDATEROLEBINDINGREQUEST.fields_by_name['tags'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_tag__pb2._TAG
_ROLEBINDINGINFO.fields_by_name['role_info'].message_type = spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2._ROLEINFO
_ROLEBINDINGINFO.fields_by_name['project_info'].message_type = spaceone_dot_api_dot_identity_dot_v1_dot_project__pb2._PROJECTINFO
_ROLEBINDINGINFO.fields_by_name['project_group_info'].message_type = spaceone_dot_api_dot_identity_dot_v1_dot_project__group__pb2._PROJECTGROUPINFO
_ROLEBINDINGINFO.fields_by_name['tags'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_tag__pb2._TAG
_ROLEBINDINGINFO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ROLEBINDINGQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._QUERY
_ROLEBINDINGSINFO.fields_by_name['results'].message_type = _ROLEBINDINGINFO
_ROLEBINDINGSTATQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._STATISTICSQUERY
DESCRIPTOR.message_types_by_name['CreateRoleBindingRequest'] = _CREATEROLEBINDINGREQUEST
DESCRIPTOR.message_types_by_name['UpdateRoleBindingRequest'] = _UPDATEROLEBINDINGREQUEST
DESCRIPTOR.message_types_by_name['RoleBindingRequest'] = _ROLEBINDINGREQUEST
DESCRIPTOR.message_types_by_name['GetRoleBindingRequest'] = _GETROLEBINDINGREQUEST
DESCRIPTOR.message_types_by_name['RoleBindingInfo'] = _ROLEBINDINGINFO
DESCRIPTOR.message_types_by_name['RoleBindingQuery'] = _ROLEBINDINGQUERY
DESCRIPTOR.message_types_by_name['RoleBindingsInfo'] = _ROLEBINDINGSINFO
DESCRIPTOR.message_types_by_name['RoleBindingStatQuery'] = _ROLEBINDINGSTATQUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateRoleBindingRequest = _reflection.GeneratedProtocolMessageType('CreateRoleBindingRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEROLEBINDINGREQUEST,
  '__module__' : 'spaceone.api.identity.v1.role_binding_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.CreateRoleBindingRequest)
  })
_sym_db.RegisterMessage(CreateRoleBindingRequest)

UpdateRoleBindingRequest = _reflection.GeneratedProtocolMessageType('UpdateRoleBindingRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEROLEBINDINGREQUEST,
  '__module__' : 'spaceone.api.identity.v1.role_binding_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.UpdateRoleBindingRequest)
  })
_sym_db.RegisterMessage(UpdateRoleBindingRequest)

RoleBindingRequest = _reflection.GeneratedProtocolMessageType('RoleBindingRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEBINDINGREQUEST,
  '__module__' : 'spaceone.api.identity.v1.role_binding_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.RoleBindingRequest)
  })
_sym_db.RegisterMessage(RoleBindingRequest)

GetRoleBindingRequest = _reflection.GeneratedProtocolMessageType('GetRoleBindingRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETROLEBINDINGREQUEST,
  '__module__' : 'spaceone.api.identity.v1.role_binding_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.GetRoleBindingRequest)
  })
_sym_db.RegisterMessage(GetRoleBindingRequest)

RoleBindingInfo = _reflection.GeneratedProtocolMessageType('RoleBindingInfo', (_message.Message,), {
  'DESCRIPTOR' : _ROLEBINDINGINFO,
  '__module__' : 'spaceone.api.identity.v1.role_binding_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.RoleBindingInfo)
  })
_sym_db.RegisterMessage(RoleBindingInfo)

RoleBindingQuery = _reflection.GeneratedProtocolMessageType('RoleBindingQuery', (_message.Message,), {
  'DESCRIPTOR' : _ROLEBINDINGQUERY,
  '__module__' : 'spaceone.api.identity.v1.role_binding_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.RoleBindingQuery)
  })
_sym_db.RegisterMessage(RoleBindingQuery)

RoleBindingsInfo = _reflection.GeneratedProtocolMessageType('RoleBindingsInfo', (_message.Message,), {
  'DESCRIPTOR' : _ROLEBINDINGSINFO,
  '__module__' : 'spaceone.api.identity.v1.role_binding_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.RoleBindingsInfo)
  })
_sym_db.RegisterMessage(RoleBindingsInfo)

RoleBindingStatQuery = _reflection.GeneratedProtocolMessageType('RoleBindingStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _ROLEBINDINGSTATQUERY,
  '__module__' : 'spaceone.api.identity.v1.role_binding_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.RoleBindingStatQuery)
  })
_sym_db.RegisterMessage(RoleBindingStatQuery)



_ROLEBINDING = _descriptor.ServiceDescriptor(
  name='RoleBinding',
  full_name='spaceone.api.identity.v1.RoleBinding',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1709,
  serialized_end=2597,
  methods=[
  _descriptor.MethodDescriptor(
    name='create',
    full_name='spaceone.api.identity.v1.RoleBinding.create',
    index=0,
    containing_service=None,
    input_type=_CREATEROLEBINDINGREQUEST,
    output_type=_ROLEBINDINGINFO,
    serialized_options=b'\202\323\344\223\002\034\"\032/identity/v1/role-bindings',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='spaceone.api.identity.v1.RoleBinding.update',
    index=1,
    containing_service=None,
    input_type=_UPDATEROLEBINDINGREQUEST,
    output_type=_ROLEBINDINGINFO,
    serialized_options=b'\202\323\344\223\002.\032,/identity/v1/role-bindings/{role_binding_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='spaceone.api.identity.v1.RoleBinding.delete',
    index=2,
    containing_service=None,
    input_type=_ROLEBINDINGREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002.*,/identity/v1/role-bindings/{role_binding_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='spaceone.api.identity.v1.RoleBinding.get',
    index=3,
    containing_service=None,
    input_type=_GETROLEBINDINGREQUEST,
    output_type=_ROLEBINDINGINFO,
    serialized_options=b'\202\323\344\223\002.\022,/identity/v1/role-bindings/{role_binding_id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='list',
    full_name='spaceone.api.identity.v1.RoleBinding.list',
    index=4,
    containing_service=None,
    input_type=_ROLEBINDINGQUERY,
    output_type=_ROLEBINDINGSINFO,
    serialized_options=b'\202\323\344\223\002A\022\032/identity/v1/role-bindingsZ#\"!/identity/v1/role-bindings/search',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stat',
    full_name='spaceone.api.identity.v1.RoleBinding.stat',
    index=5,
    containing_service=None,
    input_type=_ROLEBINDINGSTATQUERY,
    output_type=google_dot_protobuf_dot_struct__pb2._STRUCT,
    serialized_options=b'\202\323\344\223\002\031\"\027/identity/v1/roles/stat',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROLEBINDING)

DESCRIPTOR.services_by_name['RoleBinding'] = _ROLEBINDING

# @@protoc_insertion_point(module_scope)
