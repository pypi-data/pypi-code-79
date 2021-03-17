# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/gateway/v1beta1/resources.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2
from cs3.storage.provider.v1beta1 import resources_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/gateway/v1beta1/resources.proto',
  package='cs3.gateway.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\027com.cs3.gateway.v1beta1B\016ResourcesProtoP\001Z\016gatewayv1beta1\242\002\003CGX\252\002\023Cs3.Gateway.V1Beta1\312\002\023Cs3\\Gateway\\V1Beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#cs3/gateway/v1beta1/resources.proto\x12\x13\x63s3.gateway.v1beta1\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a,cs3/storage/provider/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xce\x01\n\x12\x46ileUploadProtocol\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x10\n\x08protocol\x18\x02 \x01(\t\x12\x17\n\x0fupload_endpoint\x18\x03 \x01(\t\x12S\n\x13\x61vailable_checksums\x18\x04 \x03(\x0b\x32\x36.cs3.storage.provider.v1beta1.ResourceChecksumPriority\x12\r\n\x05token\x18\x05 \x01(\t\"}\n\x14\x46ileDownloadProtocol\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x10\n\x08protocol\x18\x02 \x01(\t\x12\x19\n\x11\x64ownload_endpoint\x18\x03 \x01(\t\x12\r\n\x05token\x18\x04 \x01(\tBm\n\x17\x63om.cs3.gateway.v1beta1B\x0eResourcesProtoP\x01Z\x0egatewayv1beta1\xa2\x02\x03\x43GX\xaa\x02\x13\x43s3.Gateway.V1Beta1\xca\x02\x13\x43s3\\Gateway\\V1Beta1b\x06proto3'
  ,
  dependencies=[cs3_dot_rpc_dot_v1beta1_dot_status__pb2.DESCRIPTOR,cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2.DESCRIPTOR,cs3_dot_types_dot_v1beta1_dot_types__pb2.DESCRIPTOR,])




_FILEUPLOADPROTOCOL = _descriptor.Descriptor(
  name='FileUploadProtocol',
  full_name='cs3.gateway.v1beta1.FileUploadProtocol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.gateway.v1beta1.FileUploadProtocol.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='cs3.gateway.v1beta1.FileUploadProtocol.protocol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='upload_endpoint', full_name='cs3.gateway.v1beta1.FileUploadProtocol.upload_endpoint', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='available_checksums', full_name='cs3.gateway.v1beta1.FileUploadProtocol.available_checksums', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='cs3.gateway.v1beta1.FileUploadProtocol.token', index=4,
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
  serialized_start=168,
  serialized_end=374,
)


_FILEDOWNLOADPROTOCOL = _descriptor.Descriptor(
  name='FileDownloadProtocol',
  full_name='cs3.gateway.v1beta1.FileDownloadProtocol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.gateway.v1beta1.FileDownloadProtocol.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='cs3.gateway.v1beta1.FileDownloadProtocol.protocol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='download_endpoint', full_name='cs3.gateway.v1beta1.FileDownloadProtocol.download_endpoint', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='cs3.gateway.v1beta1.FileDownloadProtocol.token', index=3,
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
  serialized_start=376,
  serialized_end=501,
)

_FILEUPLOADPROTOCOL.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_FILEUPLOADPROTOCOL.fields_by_name['available_checksums'].message_type = cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2._RESOURCECHECKSUMPRIORITY
_FILEDOWNLOADPROTOCOL.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
DESCRIPTOR.message_types_by_name['FileUploadProtocol'] = _FILEUPLOADPROTOCOL
DESCRIPTOR.message_types_by_name['FileDownloadProtocol'] = _FILEDOWNLOADPROTOCOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileUploadProtocol = _reflection.GeneratedProtocolMessageType('FileUploadProtocol', (_message.Message,), {
  'DESCRIPTOR' : _FILEUPLOADPROTOCOL,
  '__module__' : 'cs3.gateway.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gateway.v1beta1.FileUploadProtocol)
  })
_sym_db.RegisterMessage(FileUploadProtocol)

FileDownloadProtocol = _reflection.GeneratedProtocolMessageType('FileDownloadProtocol', (_message.Message,), {
  'DESCRIPTOR' : _FILEDOWNLOADPROTOCOL,
  '__module__' : 'cs3.gateway.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gateway.v1beta1.FileDownloadProtocol)
  })
_sym_db.RegisterMessage(FileDownloadProtocol)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
