# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/inventory/v1/job_task.proto
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
from spaceone.api.inventory.v1 import collector_pb2 as spaceone_dot_api_dot_inventory_dot_v1_dot_collector__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spaceone/api/inventory/v1/job_task.proto',
  package='spaceone.api.inventory.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(spaceone/api/inventory/v1/job_task.proto\x12\x19spaceone.api.inventory.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\x1a)spaceone/api/inventory/v1/collector.proto\"\xf0\x02\n\x0cJobTaskQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x13\n\x0bjob_task_id\x18\x02 \x01(\t\x12\x45\n\x06status\x18\x03 \x01(\x0e\x32\x35.spaceone.api.inventory.v1.JobTaskQuery.JobTaskStatus\x12\x0e\n\x06job_id\x18\x04 \x01(\t\x12\x11\n\tsecret_id\x18\x05 \x01(\t\x12\x10\n\x08provider\x18\x06 \x01(\t\x12\x1a\n\x12service_account_id\x18\x07 \x01(\t\x12\x12\n\nproject_id\x18\x08 \x01(\t\x12\x11\n\tdomain_id\x18\t \x01(\t\"`\n\rJobTaskStatus\x12\x17\n\x13JOB_TASK_STATE_NONE\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0f\n\x0bIN_PROGRESS\x10\x02\x12\x0b\n\x07SUCCESS\x10\x03\x12\x0b\n\x07\x46\x41ILURE\x10\x04\"\x81\x05\n\x0bJobTaskInfo\x12\x13\n\x0bjob_task_id\x18\x01 \x01(\t\x12\x44\n\x06status\x18\x02 \x01(\x0e\x32\x34.spaceone.api.inventory.v1.JobTaskInfo.JobTaskStatus\x12\x15\n\rcreated_count\x18\x03 \x01(\x05\x12\x15\n\rupdated_count\x18\x04 \x01(\x05\x12\x15\n\rfailure_count\x18\x05 \x01(\x05\x12\x15\n\rdeleted_count\x18\x06 \x01(\x05\x12\x1a\n\x12\x64isconnected_count\x18\x07 \x01(\x05\x12\x34\n\x06\x65rrors\x18\t \x03(\x0b\x32$.spaceone.api.inventory.v1.ErrorInfo\x12\x0e\n\x06job_id\x18\x0b \x01(\t\x12\x11\n\tsecret_id\x18\x0c \x01(\t\x12\x10\n\x08provider\x18\r \x01(\t\x12\x1a\n\x12service_account_id\x18\x0e \x01(\t\x12\x12\n\nproject_id\x18\x0f \x01(\t\x12\x11\n\tdomain_id\x18\x10 \x01(\t\x12.\n\ncreated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nstarted_at\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x66inished_at\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"`\n\rJobTaskStatus\x12\x17\n\x13JOB_TASK_STATE_NONE\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0f\n\x0bIN_PROGRESS\x10\x02\x12\x0b\n\x07SUCCESS\x10\x03\x12\x0b\n\x07\x46\x41ILURE\x10\x04\"\\\n\x0cJobTasksInfo\x12\x37\n\x07results\x18\x01 \x03(\x0b\x32&.spaceone.api.inventory.v1.JobTaskInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"[\n\x10JobTaskStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\x9b\x02\n\x07JobTask\x12\x9b\x01\n\x04list\x12\'.spaceone.api.inventory.v1.JobTaskQuery\x1a\'.spaceone.api.inventory.v1.JobTasksInfo\"A\x82\xd3\xe4\x93\x02;\x12\x17/inventory/v1/job-tasksZ \"\x1e/inventory/v1/job-tasks/search\x12r\n\x04stat\x12+.spaceone.api.inventory.v1.JobTaskStatQuery\x1a\x17.google.protobuf.Struct\"$\x82\xd3\xe4\x93\x02\x1e\"\x1c/inventory/v1/job-tasks/statb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.DESCRIPTOR,spaceone_dot_api_dot_inventory_dot_v1_dot_collector__pb2.DESCRIPTOR,])



_JOBTASKQUERY_JOBTASKSTATUS = _descriptor.EnumDescriptor(
  name='JobTaskStatus',
  full_name='spaceone.api.inventory.v1.JobTaskQuery.JobTaskStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JOB_TASK_STATE_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IN_PROGRESS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=514,
  serialized_end=610,
)
_sym_db.RegisterEnumDescriptor(_JOBTASKQUERY_JOBTASKSTATUS)

_JOBTASKINFO_JOBTASKSTATUS = _descriptor.EnumDescriptor(
  name='JobTaskStatus',
  full_name='spaceone.api.inventory.v1.JobTaskInfo.JobTaskStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JOB_TASK_STATE_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IN_PROGRESS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=514,
  serialized_end=610,
)
_sym_db.RegisterEnumDescriptor(_JOBTASKINFO_JOBTASKSTATUS)


_JOBTASKQUERY = _descriptor.Descriptor(
  name='JobTaskQuery',
  full_name='spaceone.api.inventory.v1.JobTaskQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.inventory.v1.JobTaskQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_task_id', full_name='spaceone.api.inventory.v1.JobTaskQuery.job_task_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='spaceone.api.inventory.v1.JobTaskQuery.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='spaceone.api.inventory.v1.JobTaskQuery.job_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret_id', full_name='spaceone.api.inventory.v1.JobTaskQuery.secret_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider', full_name='spaceone.api.inventory.v1.JobTaskQuery.provider', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='spaceone.api.inventory.v1.JobTaskQuery.service_account_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='spaceone.api.inventory.v1.JobTaskQuery.project_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.JobTaskQuery.domain_id', index=8,
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
    _JOBTASKQUERY_JOBTASKSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=610,
)


_JOBTASKINFO = _descriptor.Descriptor(
  name='JobTaskInfo',
  full_name='spaceone.api.inventory.v1.JobTaskInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_task_id', full_name='spaceone.api.inventory.v1.JobTaskInfo.job_task_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='spaceone.api.inventory.v1.JobTaskInfo.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_count', full_name='spaceone.api.inventory.v1.JobTaskInfo.created_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated_count', full_name='spaceone.api.inventory.v1.JobTaskInfo.updated_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='failure_count', full_name='spaceone.api.inventory.v1.JobTaskInfo.failure_count', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted_count', full_name='spaceone.api.inventory.v1.JobTaskInfo.deleted_count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disconnected_count', full_name='spaceone.api.inventory.v1.JobTaskInfo.disconnected_count', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errors', full_name='spaceone.api.inventory.v1.JobTaskInfo.errors', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='spaceone.api.inventory.v1.JobTaskInfo.job_id', index=8,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret_id', full_name='spaceone.api.inventory.v1.JobTaskInfo.secret_id', index=9,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider', full_name='spaceone.api.inventory.v1.JobTaskInfo.provider', index=10,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='spaceone.api.inventory.v1.JobTaskInfo.service_account_id', index=11,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='spaceone.api.inventory.v1.JobTaskInfo.project_id', index=12,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.JobTaskInfo.domain_id', index=13,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='spaceone.api.inventory.v1.JobTaskInfo.created_at', index=14,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='spaceone.api.inventory.v1.JobTaskInfo.started_at', index=15,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='finished_at', full_name='spaceone.api.inventory.v1.JobTaskInfo.finished_at', index=16,
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
    _JOBTASKINFO_JOBTASKSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=613,
  serialized_end=1254,
)


_JOBTASKSINFO = _descriptor.Descriptor(
  name='JobTasksInfo',
  full_name='spaceone.api.inventory.v1.JobTasksInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='spaceone.api.inventory.v1.JobTasksInfo.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='spaceone.api.inventory.v1.JobTasksInfo.total_count', index=1,
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
  serialized_start=1256,
  serialized_end=1348,
)


_JOBTASKSTATQUERY = _descriptor.Descriptor(
  name='JobTaskStatQuery',
  full_name='spaceone.api.inventory.v1.JobTaskStatQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.inventory.v1.JobTaskStatQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.JobTaskStatQuery.domain_id', index=1,
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
  serialized_start=1350,
  serialized_end=1441,
)

_JOBTASKQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._QUERY
_JOBTASKQUERY.fields_by_name['status'].enum_type = _JOBTASKQUERY_JOBTASKSTATUS
_JOBTASKQUERY_JOBTASKSTATUS.containing_type = _JOBTASKQUERY
_JOBTASKINFO.fields_by_name['status'].enum_type = _JOBTASKINFO_JOBTASKSTATUS
_JOBTASKINFO.fields_by_name['errors'].message_type = spaceone_dot_api_dot_inventory_dot_v1_dot_collector__pb2._ERRORINFO
_JOBTASKINFO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_JOBTASKINFO.fields_by_name['started_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_JOBTASKINFO.fields_by_name['finished_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_JOBTASKINFO_JOBTASKSTATUS.containing_type = _JOBTASKINFO
_JOBTASKSINFO.fields_by_name['results'].message_type = _JOBTASKINFO
_JOBTASKSTATQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._STATISTICSQUERY
DESCRIPTOR.message_types_by_name['JobTaskQuery'] = _JOBTASKQUERY
DESCRIPTOR.message_types_by_name['JobTaskInfo'] = _JOBTASKINFO
DESCRIPTOR.message_types_by_name['JobTasksInfo'] = _JOBTASKSINFO
DESCRIPTOR.message_types_by_name['JobTaskStatQuery'] = _JOBTASKSTATQUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobTaskQuery = _reflection.GeneratedProtocolMessageType('JobTaskQuery', (_message.Message,), {
  'DESCRIPTOR' : _JOBTASKQUERY,
  '__module__' : 'spaceone.api.inventory.v1.job_task_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.JobTaskQuery)
  })
_sym_db.RegisterMessage(JobTaskQuery)

JobTaskInfo = _reflection.GeneratedProtocolMessageType('JobTaskInfo', (_message.Message,), {
  'DESCRIPTOR' : _JOBTASKINFO,
  '__module__' : 'spaceone.api.inventory.v1.job_task_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.JobTaskInfo)
  })
_sym_db.RegisterMessage(JobTaskInfo)

JobTasksInfo = _reflection.GeneratedProtocolMessageType('JobTasksInfo', (_message.Message,), {
  'DESCRIPTOR' : _JOBTASKSINFO,
  '__module__' : 'spaceone.api.inventory.v1.job_task_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.JobTasksInfo)
  })
_sym_db.RegisterMessage(JobTasksInfo)

JobTaskStatQuery = _reflection.GeneratedProtocolMessageType('JobTaskStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _JOBTASKSTATQUERY,
  '__module__' : 'spaceone.api.inventory.v1.job_task_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.JobTaskStatQuery)
  })
_sym_db.RegisterMessage(JobTaskStatQuery)



_JOBTASK = _descriptor.ServiceDescriptor(
  name='JobTask',
  full_name='spaceone.api.inventory.v1.JobTask',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1444,
  serialized_end=1727,
  methods=[
  _descriptor.MethodDescriptor(
    name='list',
    full_name='spaceone.api.inventory.v1.JobTask.list',
    index=0,
    containing_service=None,
    input_type=_JOBTASKQUERY,
    output_type=_JOBTASKSINFO,
    serialized_options=b'\202\323\344\223\002;\022\027/inventory/v1/job-tasksZ \"\036/inventory/v1/job-tasks/search',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stat',
    full_name='spaceone.api.inventory.v1.JobTask.stat',
    index=1,
    containing_service=None,
    input_type=_JOBTASKSTATQUERY,
    output_type=google_dot_protobuf_dot_struct__pb2._STRUCT,
    serialized_options=b'\202\323\344\223\002\036\"\034/inventory/v1/job-tasks/stat',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_JOBTASK)

DESCRIPTOR.services_by_name['JobTask'] = _JOBTASK

# @@protoc_insertion_point(module_scope)
