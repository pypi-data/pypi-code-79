# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bosdyn/api/data_chunk.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bosdyn/api/data_chunk.proto',
  package='bosdyn.api',
  syntax='proto3',
  serialized_pb=_b('\n\x1b\x62osdyn/api/data_chunk.proto\x12\nbosdyn.api\"-\n\tDataChunk\x12\x12\n\ntotal_size\x18\x01 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x42\x10\x42\x0e\x44\x61taChunkProtob\x06proto3')
)




_DATACHUNK = _descriptor.Descriptor(
  name='DataChunk',
  full_name='bosdyn.api.DataChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_size', full_name='bosdyn.api.DataChunk.total_size', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='bosdyn.api.DataChunk.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['DataChunk'] = _DATACHUNK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataChunk = _reflection.GeneratedProtocolMessageType('DataChunk', (_message.Message,), dict(
  DESCRIPTOR = _DATACHUNK,
  __module__ = 'bosdyn.api.data_chunk_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.DataChunk)
  ))
_sym_db.RegisterMessage(DataChunk)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\016DataChunkProto'))
# @@protoc_insertion_point(module_scope)
