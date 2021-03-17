# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bosdyn/api/power.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bosdyn.api import header_pb2 as bosdyn_dot_api_dot_header__pb2
from bosdyn.api import lease_pb2 as bosdyn_dot_api_dot_lease__pb2
from bosdyn.api import license_pb2 as bosdyn_dot_api_dot_license__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bosdyn/api/power.proto',
  package='bosdyn.api',
  syntax='proto3',
  serialized_pb=_b('\n\x16\x62osdyn/api/power.proto\x12\nbosdyn.api\x1a\x17\x62osdyn/api/header.proto\x1a\x16\x62osdyn/api/lease.proto\x1a\x18\x62osdyn/api/license.proto\"\xdd\x01\n\x13PowerCommandRequest\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.bosdyn.api.RequestHeader\x12 \n\x05lease\x18\x02 \x01(\x0b\x32\x11.bosdyn.api.Lease\x12\x38\n\x07request\x18\x03 \x01(\x0e\x32\'.bosdyn.api.PowerCommandRequest.Request\"?\n\x07Request\x12\x13\n\x0fREQUEST_UNKNOWN\x10\x00\x12\x0f\n\x0bREQUEST_OFF\x10\x01\x12\x0e\n\nREQUEST_ON\x10\x02\"\xfa\x01\n\x14PowerCommandResponse\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.bosdyn.api.ResponseHeader\x12\x34\n\x10lease_use_result\x18\x02 \x01(\x0b\x32\x1a.bosdyn.api.LeaseUseResult\x12.\n\x06status\x18\x03 \x01(\x0e\x32\x1e.bosdyn.api.PowerCommandStatus\x12\x18\n\x10power_command_id\x18\x04 \x01(\r\x12\x36\n\x0elicense_status\x18\x05 \x01(\x0e\x32\x1e.bosdyn.api.LicenseInfo.Status\"b\n\x1bPowerCommandFeedbackRequest\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.bosdyn.api.RequestHeader\x12\x18\n\x10power_command_id\x18\x02 \x01(\r\"z\n\x1cPowerCommandFeedbackResponse\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.bosdyn.api.ResponseHeader\x12.\n\x06status\x18\x02 \x01(\x0e\x32\x1e.bosdyn.api.PowerCommandStatus*\x90\x02\n\x12PowerCommandStatus\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x16\n\x12STATUS_IN_PROGRESS\x10\x01\x12\x12\n\x0eSTATUS_SUCCESS\x10\x02\x12 \n\x1cSTATUS_SHORE_POWER_CONNECTED\x10\x03\x12\x1a\n\x16STATUS_BATTERY_MISSING\x10\x04\x12\x1e\n\x1aSTATUS_COMMAND_IN_PROGRESS\x10\x05\x12\x13\n\x0fSTATUS_ESTOPPED\x10\x06\x12\x12\n\x0eSTATUS_FAULTED\x10\x07\x12\x19\n\x15STATUS_INTERNAL_ERROR\x10\x08\x12\x18\n\x14STATUS_LICENSE_ERROR\x10\tB\x0c\x42\nPowerProtob\x06proto3')
  ,
  dependencies=[bosdyn_dot_api_dot_header__pb2.DESCRIPTOR,bosdyn_dot_api_dot_lease__pb2.DESCRIPTOR,bosdyn_dot_api_dot_license__pb2.DESCRIPTOR,])

_POWERCOMMANDSTATUS = _descriptor.EnumDescriptor(
  name='PowerCommandStatus',
  full_name='bosdyn.api.PowerCommandStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_IN_PROGRESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_SUCCESS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_SHORE_POWER_CONNECTED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_BATTERY_MISSING', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_COMMAND_IN_PROGRESS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_ESTOPPED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_FAULTED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_INTERNAL_ERROR', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_LICENSE_ERROR', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=815,
  serialized_end=1087,
)
_sym_db.RegisterEnumDescriptor(_POWERCOMMANDSTATUS)

PowerCommandStatus = enum_type_wrapper.EnumTypeWrapper(_POWERCOMMANDSTATUS)
STATUS_UNKNOWN = 0
STATUS_IN_PROGRESS = 1
STATUS_SUCCESS = 2
STATUS_SHORE_POWER_CONNECTED = 3
STATUS_BATTERY_MISSING = 4
STATUS_COMMAND_IN_PROGRESS = 5
STATUS_ESTOPPED = 6
STATUS_FAULTED = 7
STATUS_INTERNAL_ERROR = 8
STATUS_LICENSE_ERROR = 9


_POWERCOMMANDREQUEST_REQUEST = _descriptor.EnumDescriptor(
  name='Request',
  full_name='bosdyn.api.PowerCommandRequest.Request',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REQUEST_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_OFF', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_ON', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=272,
  serialized_end=335,
)
_sym_db.RegisterEnumDescriptor(_POWERCOMMANDREQUEST_REQUEST)


_POWERCOMMANDREQUEST = _descriptor.Descriptor(
  name='PowerCommandRequest',
  full_name='bosdyn.api.PowerCommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.PowerCommandRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lease', full_name='bosdyn.api.PowerCommandRequest.lease', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request', full_name='bosdyn.api.PowerCommandRequest.request', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POWERCOMMANDREQUEST_REQUEST,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=335,
)


_POWERCOMMANDRESPONSE = _descriptor.Descriptor(
  name='PowerCommandResponse',
  full_name='bosdyn.api.PowerCommandResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.PowerCommandResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lease_use_result', full_name='bosdyn.api.PowerCommandResponse.lease_use_result', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='bosdyn.api.PowerCommandResponse.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power_command_id', full_name='bosdyn.api.PowerCommandResponse.power_command_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='license_status', full_name='bosdyn.api.PowerCommandResponse.license_status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=338,
  serialized_end=588,
)


_POWERCOMMANDFEEDBACKREQUEST = _descriptor.Descriptor(
  name='PowerCommandFeedbackRequest',
  full_name='bosdyn.api.PowerCommandFeedbackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.PowerCommandFeedbackRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power_command_id', full_name='bosdyn.api.PowerCommandFeedbackRequest.power_command_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=590,
  serialized_end=688,
)


_POWERCOMMANDFEEDBACKRESPONSE = _descriptor.Descriptor(
  name='PowerCommandFeedbackResponse',
  full_name='bosdyn.api.PowerCommandFeedbackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.PowerCommandFeedbackResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='bosdyn.api.PowerCommandFeedbackResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=690,
  serialized_end=812,
)

_POWERCOMMANDREQUEST.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._REQUESTHEADER
_POWERCOMMANDREQUEST.fields_by_name['lease'].message_type = bosdyn_dot_api_dot_lease__pb2._LEASE
_POWERCOMMANDREQUEST.fields_by_name['request'].enum_type = _POWERCOMMANDREQUEST_REQUEST
_POWERCOMMANDREQUEST_REQUEST.containing_type = _POWERCOMMANDREQUEST
_POWERCOMMANDRESPONSE.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._RESPONSEHEADER
_POWERCOMMANDRESPONSE.fields_by_name['lease_use_result'].message_type = bosdyn_dot_api_dot_lease__pb2._LEASEUSERESULT
_POWERCOMMANDRESPONSE.fields_by_name['status'].enum_type = _POWERCOMMANDSTATUS
_POWERCOMMANDRESPONSE.fields_by_name['license_status'].enum_type = bosdyn_dot_api_dot_license__pb2._LICENSEINFO_STATUS
_POWERCOMMANDFEEDBACKREQUEST.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._REQUESTHEADER
_POWERCOMMANDFEEDBACKRESPONSE.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._RESPONSEHEADER
_POWERCOMMANDFEEDBACKRESPONSE.fields_by_name['status'].enum_type = _POWERCOMMANDSTATUS
DESCRIPTOR.message_types_by_name['PowerCommandRequest'] = _POWERCOMMANDREQUEST
DESCRIPTOR.message_types_by_name['PowerCommandResponse'] = _POWERCOMMANDRESPONSE
DESCRIPTOR.message_types_by_name['PowerCommandFeedbackRequest'] = _POWERCOMMANDFEEDBACKREQUEST
DESCRIPTOR.message_types_by_name['PowerCommandFeedbackResponse'] = _POWERCOMMANDFEEDBACKRESPONSE
DESCRIPTOR.enum_types_by_name['PowerCommandStatus'] = _POWERCOMMANDSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PowerCommandRequest = _reflection.GeneratedProtocolMessageType('PowerCommandRequest', (_message.Message,), dict(
  DESCRIPTOR = _POWERCOMMANDREQUEST,
  __module__ = 'bosdyn.api.power_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.PowerCommandRequest)
  ))
_sym_db.RegisterMessage(PowerCommandRequest)

PowerCommandResponse = _reflection.GeneratedProtocolMessageType('PowerCommandResponse', (_message.Message,), dict(
  DESCRIPTOR = _POWERCOMMANDRESPONSE,
  __module__ = 'bosdyn.api.power_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.PowerCommandResponse)
  ))
_sym_db.RegisterMessage(PowerCommandResponse)

PowerCommandFeedbackRequest = _reflection.GeneratedProtocolMessageType('PowerCommandFeedbackRequest', (_message.Message,), dict(
  DESCRIPTOR = _POWERCOMMANDFEEDBACKREQUEST,
  __module__ = 'bosdyn.api.power_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.PowerCommandFeedbackRequest)
  ))
_sym_db.RegisterMessage(PowerCommandFeedbackRequest)

PowerCommandFeedbackResponse = _reflection.GeneratedProtocolMessageType('PowerCommandFeedbackResponse', (_message.Message,), dict(
  DESCRIPTOR = _POWERCOMMANDFEEDBACKRESPONSE,
  __module__ = 'bosdyn.api.power_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.PowerCommandFeedbackResponse)
  ))
_sym_db.RegisterMessage(PowerCommandFeedbackResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\nPowerProto'))
# @@protoc_insertion_point(module_scope)
