# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bosdyn/api/lease.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bosdyn.api import header_pb2 as bosdyn_dot_api_dot_header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bosdyn/api/lease.proto',
  package='bosdyn.api',
  syntax='proto3',
  serialized_pb=_b('\n\x16\x62osdyn/api/lease.proto\x12\nbosdyn.api\x1a\x17\x62osdyn/api/header.proto\"P\n\x05Lease\x12\x10\n\x08resource\x18\x01 \x01(\t\x12\r\n\x05\x65poch\x18\x02 \x01(\t\x12\x10\n\x08sequence\x18\x03 \x03(\r\x12\x14\n\x0c\x63lient_names\x18\x04 \x03(\t\"4\n\nLeaseOwner\x12\x13\n\x0b\x63lient_name\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\"\xdd\x02\n\x0eLeaseUseResult\x12\x31\n\x06status\x18\x01 \x01(\x0e\x32!.bosdyn.api.LeaseUseResult.Status\x12%\n\x05owner\x18\x02 \x01(\x0b\x32\x16.bosdyn.api.LeaseOwner\x12*\n\x0f\x61ttempted_lease\x18\x03 \x01(\x0b\x32\x11.bosdyn.api.Lease\x12)\n\x0eprevious_lease\x18\x04 \x01(\x0b\x32\x11.bosdyn.api.Lease\"\x99\x01\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\r\n\tSTATUS_OK\x10\x01\x12\x18\n\x14STATUS_INVALID_LEASE\x10\x02\x12\x10\n\x0cSTATUS_OLDER\x10\x03\x12\x12\n\x0eSTATUS_REVOKED\x10\x04\x12\x14\n\x10STATUS_UNMANAGED\x10\x05\x12\x16\n\x12STATUS_WRONG_EPOCH\x10\x06\"R\n\x13\x41\x63quireLeaseRequest\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.bosdyn.api.RequestHeader\x12\x10\n\x08resource\x18\x02 \x01(\t\"\xe0\x02\n\x14\x41\x63quireLeaseResponse\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.bosdyn.api.ResponseHeader\x12\x37\n\x06status\x18\x02 \x01(\x0e\x32\'.bosdyn.api.AcquireLeaseResponse.Status\x12 \n\x05lease\x18\x03 \x01(\x0b\x32\x11.bosdyn.api.Lease\x12+\n\x0blease_owner\x18\x04 \x01(\x0b\x32\x16.bosdyn.api.LeaseOwner\"\x93\x01\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\r\n\tSTATUS_OK\x10\x01\x12#\n\x1fSTATUS_RESOURCE_ALREADY_CLAIMED\x10\x02\x12\x1b\n\x17STATUS_INVALID_RESOURCE\x10\x03\x12$\n STATUS_NOT_AUTHORITATIVE_SERVICE\x10\x04\"O\n\x10TakeLeaseRequest\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.bosdyn.api.RequestHeader\x12\x10\n\x08resource\x18\x02 \x01(\t\"\xb4\x02\n\x11TakeLeaseResponse\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.bosdyn.api.ResponseHeader\x12\x34\n\x06status\x18\x02 \x01(\x0e\x32$.bosdyn.api.TakeLeaseResponse.Status\x12 \n\x05lease\x18\x03 \x01(\x0b\x32\x11.bosdyn.api.Lease\x12+\n\x0blease_owner\x18\x04 \x01(\x0b\x32\x16.bosdyn.api.LeaseOwner\"n\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\r\n\tSTATUS_OK\x10\x01\x12\x1b\n\x17STATUS_INVALID_RESOURCE\x10\x02\x12$\n STATUS_NOT_AUTHORITATIVE_SERVICE\x10\x03\"a\n\x12ReturnLeaseRequest\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.bosdyn.api.RequestHeader\x12 \n\x05lease\x18\x02 \x01(\x0b\x32\x11.bosdyn.api.Lease\"\x87\x02\n\x13ReturnLeaseResponse\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.bosdyn.api.ResponseHeader\x12\x36\n\x06status\x18\x02 \x01(\x0e\x32&.bosdyn.api.ReturnLeaseResponse.Status\"\x8b\x01\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\r\n\tSTATUS_OK\x10\x01\x12\x1b\n\x17STATUS_INVALID_RESOURCE\x10\x02\x12\x1b\n\x17STATUS_NOT_ACTIVE_LEASE\x10\x03\x12$\n STATUS_NOT_AUTHORITATIVE_SERVICE\x10\x04\"_\n\x11ListLeasesRequest\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.bosdyn.api.RequestHeader\x12\x1f\n\x17include_full_lease_info\x18\x02 \x01(\x08\"p\n\rLeaseResource\x12\x10\n\x08resource\x18\x01 \x01(\t\x12 \n\x05lease\x18\x02 \x01(\x0b\x32\x11.bosdyn.api.Lease\x12+\n\x0blease_owner\x18\x03 \x01(\x0b\x32\x16.bosdyn.api.LeaseOwner\"n\n\x12ListLeasesResponse\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.bosdyn.api.ResponseHeader\x12,\n\tresources\x18\x02 \x03(\x0b\x32\x19.bosdyn.api.LeaseResource\"a\n\x12RetainLeaseRequest\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.bosdyn.api.RequestHeader\x12 \n\x05lease\x18\x02 \x01(\x0b\x32\x11.bosdyn.api.Lease\"w\n\x13RetainLeaseResponse\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.bosdyn.api.ResponseHeader\x12\x34\n\x10lease_use_result\x18\x02 \x01(\x0b\x32\x1a.bosdyn.api.LeaseUseResultB\x0c\x42\nLeaseProtob\x06proto3')
  ,
  dependencies=[bosdyn_dot_api_dot_header__pb2.DESCRIPTOR,])



_LEASEUSERESULT_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='bosdyn.api.LeaseUseResult.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_OK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_INVALID_LEASE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_OLDER', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_REVOKED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNMANAGED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_WRONG_EPOCH', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=396,
  serialized_end=549,
)
_sym_db.RegisterEnumDescriptor(_LEASEUSERESULT_STATUS)

_ACQUIRELEASERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='bosdyn.api.AcquireLeaseResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_OK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_RESOURCE_ALREADY_CLAIMED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_INVALID_RESOURCE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_NOT_AUTHORITATIVE_SERVICE', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=841,
  serialized_end=988,
)
_sym_db.RegisterEnumDescriptor(_ACQUIRELEASERESPONSE_STATUS)

_TAKELEASERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='bosdyn.api.TakeLeaseResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_OK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_INVALID_RESOURCE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_NOT_AUTHORITATIVE_SERVICE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1270,
  serialized_end=1380,
)
_sym_db.RegisterEnumDescriptor(_TAKELEASERESPONSE_STATUS)

_RETURNLEASERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='bosdyn.api.ReturnLeaseResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_OK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_INVALID_RESOURCE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_NOT_ACTIVE_LEASE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_NOT_AUTHORITATIVE_SERVICE', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1606,
  serialized_end=1745,
)
_sym_db.RegisterEnumDescriptor(_RETURNLEASERESPONSE_STATUS)


_LEASE = _descriptor.Descriptor(
  name='Lease',
  full_name='bosdyn.api.Lease',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource', full_name='bosdyn.api.Lease.resource', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='epoch', full_name='bosdyn.api.Lease.epoch', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='bosdyn.api.Lease.sequence', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_names', full_name='bosdyn.api.Lease.client_names', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=63,
  serialized_end=143,
)


_LEASEOWNER = _descriptor.Descriptor(
  name='LeaseOwner',
  full_name='bosdyn.api.LeaseOwner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_name', full_name='bosdyn.api.LeaseOwner.client_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='bosdyn.api.LeaseOwner.user_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=145,
  serialized_end=197,
)


_LEASEUSERESULT = _descriptor.Descriptor(
  name='LeaseUseResult',
  full_name='bosdyn.api.LeaseUseResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bosdyn.api.LeaseUseResult.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owner', full_name='bosdyn.api.LeaseUseResult.owner', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attempted_lease', full_name='bosdyn.api.LeaseUseResult.attempted_lease', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='previous_lease', full_name='bosdyn.api.LeaseUseResult.previous_lease', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LEASEUSERESULT_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=549,
)


_ACQUIRELEASEREQUEST = _descriptor.Descriptor(
  name='AcquireLeaseRequest',
  full_name='bosdyn.api.AcquireLeaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.AcquireLeaseRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='bosdyn.api.AcquireLeaseRequest.resource', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=551,
  serialized_end=633,
)


_ACQUIRELEASERESPONSE = _descriptor.Descriptor(
  name='AcquireLeaseResponse',
  full_name='bosdyn.api.AcquireLeaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.AcquireLeaseResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='bosdyn.api.AcquireLeaseResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lease', full_name='bosdyn.api.AcquireLeaseResponse.lease', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lease_owner', full_name='bosdyn.api.AcquireLeaseResponse.lease_owner', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACQUIRELEASERESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=636,
  serialized_end=988,
)


_TAKELEASEREQUEST = _descriptor.Descriptor(
  name='TakeLeaseRequest',
  full_name='bosdyn.api.TakeLeaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.TakeLeaseRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='bosdyn.api.TakeLeaseRequest.resource', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=990,
  serialized_end=1069,
)


_TAKELEASERESPONSE = _descriptor.Descriptor(
  name='TakeLeaseResponse',
  full_name='bosdyn.api.TakeLeaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.TakeLeaseResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='bosdyn.api.TakeLeaseResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lease', full_name='bosdyn.api.TakeLeaseResponse.lease', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lease_owner', full_name='bosdyn.api.TakeLeaseResponse.lease_owner', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TAKELEASERESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1072,
  serialized_end=1380,
)


_RETURNLEASEREQUEST = _descriptor.Descriptor(
  name='ReturnLeaseRequest',
  full_name='bosdyn.api.ReturnLeaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.ReturnLeaseRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lease', full_name='bosdyn.api.ReturnLeaseRequest.lease', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1382,
  serialized_end=1479,
)


_RETURNLEASERESPONSE = _descriptor.Descriptor(
  name='ReturnLeaseResponse',
  full_name='bosdyn.api.ReturnLeaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.ReturnLeaseResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='bosdyn.api.ReturnLeaseResponse.status', index=1,
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
    _RETURNLEASERESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1482,
  serialized_end=1745,
)


_LISTLEASESREQUEST = _descriptor.Descriptor(
  name='ListLeasesRequest',
  full_name='bosdyn.api.ListLeasesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.ListLeasesRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_full_lease_info', full_name='bosdyn.api.ListLeasesRequest.include_full_lease_info', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1747,
  serialized_end=1842,
)


_LEASERESOURCE = _descriptor.Descriptor(
  name='LeaseResource',
  full_name='bosdyn.api.LeaseResource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource', full_name='bosdyn.api.LeaseResource.resource', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lease', full_name='bosdyn.api.LeaseResource.lease', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lease_owner', full_name='bosdyn.api.LeaseResource.lease_owner', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1844,
  serialized_end=1956,
)


_LISTLEASESRESPONSE = _descriptor.Descriptor(
  name='ListLeasesResponse',
  full_name='bosdyn.api.ListLeasesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.ListLeasesResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resources', full_name='bosdyn.api.ListLeasesResponse.resources', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1958,
  serialized_end=2068,
)


_RETAINLEASEREQUEST = _descriptor.Descriptor(
  name='RetainLeaseRequest',
  full_name='bosdyn.api.RetainLeaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.RetainLeaseRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lease', full_name='bosdyn.api.RetainLeaseRequest.lease', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=2070,
  serialized_end=2167,
)


_RETAINLEASERESPONSE = _descriptor.Descriptor(
  name='RetainLeaseResponse',
  full_name='bosdyn.api.RetainLeaseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.RetainLeaseResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lease_use_result', full_name='bosdyn.api.RetainLeaseResponse.lease_use_result', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=2169,
  serialized_end=2288,
)

_LEASEUSERESULT.fields_by_name['status'].enum_type = _LEASEUSERESULT_STATUS
_LEASEUSERESULT.fields_by_name['owner'].message_type = _LEASEOWNER
_LEASEUSERESULT.fields_by_name['attempted_lease'].message_type = _LEASE
_LEASEUSERESULT.fields_by_name['previous_lease'].message_type = _LEASE
_LEASEUSERESULT_STATUS.containing_type = _LEASEUSERESULT
_ACQUIRELEASEREQUEST.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._REQUESTHEADER
_ACQUIRELEASERESPONSE.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._RESPONSEHEADER
_ACQUIRELEASERESPONSE.fields_by_name['status'].enum_type = _ACQUIRELEASERESPONSE_STATUS
_ACQUIRELEASERESPONSE.fields_by_name['lease'].message_type = _LEASE
_ACQUIRELEASERESPONSE.fields_by_name['lease_owner'].message_type = _LEASEOWNER
_ACQUIRELEASERESPONSE_STATUS.containing_type = _ACQUIRELEASERESPONSE
_TAKELEASEREQUEST.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._REQUESTHEADER
_TAKELEASERESPONSE.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._RESPONSEHEADER
_TAKELEASERESPONSE.fields_by_name['status'].enum_type = _TAKELEASERESPONSE_STATUS
_TAKELEASERESPONSE.fields_by_name['lease'].message_type = _LEASE
_TAKELEASERESPONSE.fields_by_name['lease_owner'].message_type = _LEASEOWNER
_TAKELEASERESPONSE_STATUS.containing_type = _TAKELEASERESPONSE
_RETURNLEASEREQUEST.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._REQUESTHEADER
_RETURNLEASEREQUEST.fields_by_name['lease'].message_type = _LEASE
_RETURNLEASERESPONSE.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._RESPONSEHEADER
_RETURNLEASERESPONSE.fields_by_name['status'].enum_type = _RETURNLEASERESPONSE_STATUS
_RETURNLEASERESPONSE_STATUS.containing_type = _RETURNLEASERESPONSE
_LISTLEASESREQUEST.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._REQUESTHEADER
_LEASERESOURCE.fields_by_name['lease'].message_type = _LEASE
_LEASERESOURCE.fields_by_name['lease_owner'].message_type = _LEASEOWNER
_LISTLEASESRESPONSE.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._RESPONSEHEADER
_LISTLEASESRESPONSE.fields_by_name['resources'].message_type = _LEASERESOURCE
_RETAINLEASEREQUEST.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._REQUESTHEADER
_RETAINLEASEREQUEST.fields_by_name['lease'].message_type = _LEASE
_RETAINLEASERESPONSE.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._RESPONSEHEADER
_RETAINLEASERESPONSE.fields_by_name['lease_use_result'].message_type = _LEASEUSERESULT
DESCRIPTOR.message_types_by_name['Lease'] = _LEASE
DESCRIPTOR.message_types_by_name['LeaseOwner'] = _LEASEOWNER
DESCRIPTOR.message_types_by_name['LeaseUseResult'] = _LEASEUSERESULT
DESCRIPTOR.message_types_by_name['AcquireLeaseRequest'] = _ACQUIRELEASEREQUEST
DESCRIPTOR.message_types_by_name['AcquireLeaseResponse'] = _ACQUIRELEASERESPONSE
DESCRIPTOR.message_types_by_name['TakeLeaseRequest'] = _TAKELEASEREQUEST
DESCRIPTOR.message_types_by_name['TakeLeaseResponse'] = _TAKELEASERESPONSE
DESCRIPTOR.message_types_by_name['ReturnLeaseRequest'] = _RETURNLEASEREQUEST
DESCRIPTOR.message_types_by_name['ReturnLeaseResponse'] = _RETURNLEASERESPONSE
DESCRIPTOR.message_types_by_name['ListLeasesRequest'] = _LISTLEASESREQUEST
DESCRIPTOR.message_types_by_name['LeaseResource'] = _LEASERESOURCE
DESCRIPTOR.message_types_by_name['ListLeasesResponse'] = _LISTLEASESRESPONSE
DESCRIPTOR.message_types_by_name['RetainLeaseRequest'] = _RETAINLEASEREQUEST
DESCRIPTOR.message_types_by_name['RetainLeaseResponse'] = _RETAINLEASERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Lease = _reflection.GeneratedProtocolMessageType('Lease', (_message.Message,), dict(
  DESCRIPTOR = _LEASE,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.Lease)
  ))
_sym_db.RegisterMessage(Lease)

LeaseOwner = _reflection.GeneratedProtocolMessageType('LeaseOwner', (_message.Message,), dict(
  DESCRIPTOR = _LEASEOWNER,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.LeaseOwner)
  ))
_sym_db.RegisterMessage(LeaseOwner)

LeaseUseResult = _reflection.GeneratedProtocolMessageType('LeaseUseResult', (_message.Message,), dict(
  DESCRIPTOR = _LEASEUSERESULT,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.LeaseUseResult)
  ))
_sym_db.RegisterMessage(LeaseUseResult)

AcquireLeaseRequest = _reflection.GeneratedProtocolMessageType('AcquireLeaseRequest', (_message.Message,), dict(
  DESCRIPTOR = _ACQUIRELEASEREQUEST,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.AcquireLeaseRequest)
  ))
_sym_db.RegisterMessage(AcquireLeaseRequest)

AcquireLeaseResponse = _reflection.GeneratedProtocolMessageType('AcquireLeaseResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACQUIRELEASERESPONSE,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.AcquireLeaseResponse)
  ))
_sym_db.RegisterMessage(AcquireLeaseResponse)

TakeLeaseRequest = _reflection.GeneratedProtocolMessageType('TakeLeaseRequest', (_message.Message,), dict(
  DESCRIPTOR = _TAKELEASEREQUEST,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.TakeLeaseRequest)
  ))
_sym_db.RegisterMessage(TakeLeaseRequest)

TakeLeaseResponse = _reflection.GeneratedProtocolMessageType('TakeLeaseResponse', (_message.Message,), dict(
  DESCRIPTOR = _TAKELEASERESPONSE,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.TakeLeaseResponse)
  ))
_sym_db.RegisterMessage(TakeLeaseResponse)

ReturnLeaseRequest = _reflection.GeneratedProtocolMessageType('ReturnLeaseRequest', (_message.Message,), dict(
  DESCRIPTOR = _RETURNLEASEREQUEST,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.ReturnLeaseRequest)
  ))
_sym_db.RegisterMessage(ReturnLeaseRequest)

ReturnLeaseResponse = _reflection.GeneratedProtocolMessageType('ReturnLeaseResponse', (_message.Message,), dict(
  DESCRIPTOR = _RETURNLEASERESPONSE,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.ReturnLeaseResponse)
  ))
_sym_db.RegisterMessage(ReturnLeaseResponse)

ListLeasesRequest = _reflection.GeneratedProtocolMessageType('ListLeasesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTLEASESREQUEST,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.ListLeasesRequest)
  ))
_sym_db.RegisterMessage(ListLeasesRequest)

LeaseResource = _reflection.GeneratedProtocolMessageType('LeaseResource', (_message.Message,), dict(
  DESCRIPTOR = _LEASERESOURCE,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.LeaseResource)
  ))
_sym_db.RegisterMessage(LeaseResource)

ListLeasesResponse = _reflection.GeneratedProtocolMessageType('ListLeasesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTLEASESRESPONSE,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.ListLeasesResponse)
  ))
_sym_db.RegisterMessage(ListLeasesResponse)

RetainLeaseRequest = _reflection.GeneratedProtocolMessageType('RetainLeaseRequest', (_message.Message,), dict(
  DESCRIPTOR = _RETAINLEASEREQUEST,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.RetainLeaseRequest)
  ))
_sym_db.RegisterMessage(RetainLeaseRequest)

RetainLeaseResponse = _reflection.GeneratedProtocolMessageType('RetainLeaseResponse', (_message.Message,), dict(
  DESCRIPTOR = _RETAINLEASERESPONSE,
  __module__ = 'bosdyn.api.lease_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.RetainLeaseResponse)
  ))
_sym_db.RegisterMessage(RetainLeaseResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\nLeaseProto'))
# @@protoc_insertion_point(module_scope)
