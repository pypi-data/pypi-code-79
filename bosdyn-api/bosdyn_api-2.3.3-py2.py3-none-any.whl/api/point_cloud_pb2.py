# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bosdyn/api/point_cloud.proto

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
from bosdyn.api import geometry_pb2 as bosdyn_dot_api_dot_geometry__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bosdyn/api/point_cloud.proto',
  package='bosdyn.api',
  syntax='proto3',
  serialized_pb=_b('\n\x1c\x62osdyn/api/point_cloud.proto\x12\nbosdyn.api\x1a\x17\x62osdyn/api/header.proto\x1a\x19\x62osdyn/api/geometry.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb3\x01\n\x10PointCloudSource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x11\x66rame_name_sensor\x18\x03 \x01(\t\x12\x34\n\x10\x61\x63quisition_time\x18\x1e \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x13transforms_snapshot\x18\x1f \x01(\x0b\x32\x1d.bosdyn.api.FrameTreeSnapshotJ\x04\x08\x02\x10\x03\"\xd6\x03\n\nPointCloud\x12,\n\x06source\x18\x01 \x01(\x0b\x32\x1c.bosdyn.api.PointCloudSource\x12\x12\n\nnum_points\x18\x02 \x01(\x05\x12\x31\n\x08\x65ncoding\x18\x03 \x01(\x0e\x32\x1f.bosdyn.api.PointCloud.Encoding\x12\x46\n\x13\x65ncoding_parameters\x18\x04 \x01(\x0b\x32).bosdyn.api.PointCloud.EncodingParameters\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\x1a\x8c\x01\n\x12\x45ncodingParameters\x12\x14\n\x0cscale_factor\x18\x01 \x01(\x05\x12\r\n\x05max_x\x18\x02 \x01(\x01\x12\r\n\x05max_y\x18\x03 \x01(\x01\x12\r\n\x05max_z\x18\x04 \x01(\x01\x12\x1a\n\x12remapping_constant\x18\x05 \x01(\x01\x12\x17\n\x0f\x62ytes_per_point\x18\x06 \x01(\x05\"b\n\x08\x45ncoding\x12\x14\n\x10\x45NCODING_UNKNOWN\x10\x00\x12\x14\n\x10\x45NCODING_XYZ_32F\x10\x01\x12\x14\n\x10\x45NCODING_XYZ_4SC\x10\x02\x12\x14\n\x10\x45NCODING_XYZ_5SC\x10\x03J\x04\x08\x08\x10\tJ\x04\x08\t\x10\n\"I\n\x1cListPointCloudSourcesRequest\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.bosdyn.api.RequestHeader\"\x86\x01\n\x1dListPointCloudSourcesResponse\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.bosdyn.api.ResponseHeader\x12\x39\n\x13point_cloud_sources\x18\x02 \x03(\x0b\x32\x1c.bosdyn.api.PointCloudSource\"4\n\x11PointCloudRequest\x12\x1f\n\x17point_cloud_source_name\x18\x01 \x01(\t\"~\n\x14GetPointCloudRequest\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.bosdyn.api.RequestHeader\x12;\n\x14point_cloud_requests\x18\x02 \x03(\x0b\x32\x1d.bosdyn.api.PointCloudRequest\"\x82\x02\n\x12PointCloudResponse\x12\x35\n\x06status\x18\x01 \x01(\x0e\x32%.bosdyn.api.PointCloudResponse.Status\x12+\n\x0bpoint_cloud\x18\x02 \x01(\x0b\x32\x16.bosdyn.api.PointCloud\"\x87\x01\n\x06Status\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\r\n\tSTATUS_OK\x10\x01\x12\x1c\n\x18STATUS_SOURCE_DATA_ERROR\x10\x02\x12!\n\x1dSTATUS_POINT_CLOUD_DATA_ERROR\x10\x03\x12\x19\n\x15STATUS_UNKNOWN_SOURCE\x10\x04\"\x82\x01\n\x15GetPointCloudResponse\x12*\n\x06header\x18\x01 \x01(\x0b\x32\x1a.bosdyn.api.ResponseHeader\x12=\n\x15point_cloud_responses\x18\x04 \x03(\x0b\x32\x1e.bosdyn.api.PointCloudResponseB\x11\x42\x0fPointCloudProtob\x06proto3')
  ,
  dependencies=[bosdyn_dot_api_dot_header__pb2.DESCRIPTOR,bosdyn_dot_api_dot_geometry__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_POINTCLOUD_ENCODING = _descriptor.EnumDescriptor(
  name='Encoding',
  full_name='bosdyn.api.PointCloud.Encoding',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENCODING_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCODING_XYZ_32F', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCODING_XYZ_4SC', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCODING_XYZ_5SC', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=672,
  serialized_end=770,
)
_sym_db.RegisterEnumDescriptor(_POINTCLOUD_ENCODING)

_POINTCLOUDRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='bosdyn.api.PointCloudResponse.Status',
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
      name='STATUS_SOURCE_DATA_ERROR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_POINT_CLOUD_DATA_ERROR', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNKNOWN_SOURCE', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1302,
  serialized_end=1437,
)
_sym_db.RegisterEnumDescriptor(_POINTCLOUDRESPONSE_STATUS)


_POINTCLOUDSOURCE = _descriptor.Descriptor(
  name='PointCloudSource',
  full_name='bosdyn.api.PointCloudSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='bosdyn.api.PointCloudSource.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frame_name_sensor', full_name='bosdyn.api.PointCloudSource.frame_name_sensor', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acquisition_time', full_name='bosdyn.api.PointCloudSource.acquisition_time', index=2,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transforms_snapshot', full_name='bosdyn.api.PointCloudSource.transforms_snapshot', index=3,
      number=31, type=11, cpp_type=10, label=1,
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
  serialized_start=130,
  serialized_end=309,
)


_POINTCLOUD_ENCODINGPARAMETERS = _descriptor.Descriptor(
  name='EncodingParameters',
  full_name='bosdyn.api.PointCloud.EncodingParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scale_factor', full_name='bosdyn.api.PointCloud.EncodingParameters.scale_factor', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_x', full_name='bosdyn.api.PointCloud.EncodingParameters.max_x', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_y', full_name='bosdyn.api.PointCloud.EncodingParameters.max_y', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_z', full_name='bosdyn.api.PointCloud.EncodingParameters.max_z', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remapping_constant', full_name='bosdyn.api.PointCloud.EncodingParameters.remapping_constant', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes_per_point', full_name='bosdyn.api.PointCloud.EncodingParameters.bytes_per_point', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=530,
  serialized_end=670,
)

_POINTCLOUD = _descriptor.Descriptor(
  name='PointCloud',
  full_name='bosdyn.api.PointCloud',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='bosdyn.api.PointCloud.source', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_points', full_name='bosdyn.api.PointCloud.num_points', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encoding', full_name='bosdyn.api.PointCloud.encoding', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encoding_parameters', full_name='bosdyn.api.PointCloud.encoding_parameters', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='bosdyn.api.PointCloud.data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_POINTCLOUD_ENCODINGPARAMETERS, ],
  enum_types=[
    _POINTCLOUD_ENCODING,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=782,
)


_LISTPOINTCLOUDSOURCESREQUEST = _descriptor.Descriptor(
  name='ListPointCloudSourcesRequest',
  full_name='bosdyn.api.ListPointCloudSourcesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.ListPointCloudSourcesRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=784,
  serialized_end=857,
)


_LISTPOINTCLOUDSOURCESRESPONSE = _descriptor.Descriptor(
  name='ListPointCloudSourcesResponse',
  full_name='bosdyn.api.ListPointCloudSourcesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.ListPointCloudSourcesResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point_cloud_sources', full_name='bosdyn.api.ListPointCloudSourcesResponse.point_cloud_sources', index=1,
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
  serialized_start=860,
  serialized_end=994,
)


_POINTCLOUDREQUEST = _descriptor.Descriptor(
  name='PointCloudRequest',
  full_name='bosdyn.api.PointCloudRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point_cloud_source_name', full_name='bosdyn.api.PointCloudRequest.point_cloud_source_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=996,
  serialized_end=1048,
)


_GETPOINTCLOUDREQUEST = _descriptor.Descriptor(
  name='GetPointCloudRequest',
  full_name='bosdyn.api.GetPointCloudRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.GetPointCloudRequest.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point_cloud_requests', full_name='bosdyn.api.GetPointCloudRequest.point_cloud_requests', index=1,
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
  serialized_start=1050,
  serialized_end=1176,
)


_POINTCLOUDRESPONSE = _descriptor.Descriptor(
  name='PointCloudResponse',
  full_name='bosdyn.api.PointCloudResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bosdyn.api.PointCloudResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point_cloud', full_name='bosdyn.api.PointCloudResponse.point_cloud', index=1,
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
    _POINTCLOUDRESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1179,
  serialized_end=1437,
)


_GETPOINTCLOUDRESPONSE = _descriptor.Descriptor(
  name='GetPointCloudResponse',
  full_name='bosdyn.api.GetPointCloudResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='bosdyn.api.GetPointCloudResponse.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point_cloud_responses', full_name='bosdyn.api.GetPointCloudResponse.point_cloud_responses', index=1,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=1440,
  serialized_end=1570,
)

_POINTCLOUDSOURCE.fields_by_name['acquisition_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_POINTCLOUDSOURCE.fields_by_name['transforms_snapshot'].message_type = bosdyn_dot_api_dot_geometry__pb2._FRAMETREESNAPSHOT
_POINTCLOUD_ENCODINGPARAMETERS.containing_type = _POINTCLOUD
_POINTCLOUD.fields_by_name['source'].message_type = _POINTCLOUDSOURCE
_POINTCLOUD.fields_by_name['encoding'].enum_type = _POINTCLOUD_ENCODING
_POINTCLOUD.fields_by_name['encoding_parameters'].message_type = _POINTCLOUD_ENCODINGPARAMETERS
_POINTCLOUD_ENCODING.containing_type = _POINTCLOUD
_LISTPOINTCLOUDSOURCESREQUEST.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._REQUESTHEADER
_LISTPOINTCLOUDSOURCESRESPONSE.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._RESPONSEHEADER
_LISTPOINTCLOUDSOURCESRESPONSE.fields_by_name['point_cloud_sources'].message_type = _POINTCLOUDSOURCE
_GETPOINTCLOUDREQUEST.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._REQUESTHEADER
_GETPOINTCLOUDREQUEST.fields_by_name['point_cloud_requests'].message_type = _POINTCLOUDREQUEST
_POINTCLOUDRESPONSE.fields_by_name['status'].enum_type = _POINTCLOUDRESPONSE_STATUS
_POINTCLOUDRESPONSE.fields_by_name['point_cloud'].message_type = _POINTCLOUD
_POINTCLOUDRESPONSE_STATUS.containing_type = _POINTCLOUDRESPONSE
_GETPOINTCLOUDRESPONSE.fields_by_name['header'].message_type = bosdyn_dot_api_dot_header__pb2._RESPONSEHEADER
_GETPOINTCLOUDRESPONSE.fields_by_name['point_cloud_responses'].message_type = _POINTCLOUDRESPONSE
DESCRIPTOR.message_types_by_name['PointCloudSource'] = _POINTCLOUDSOURCE
DESCRIPTOR.message_types_by_name['PointCloud'] = _POINTCLOUD
DESCRIPTOR.message_types_by_name['ListPointCloudSourcesRequest'] = _LISTPOINTCLOUDSOURCESREQUEST
DESCRIPTOR.message_types_by_name['ListPointCloudSourcesResponse'] = _LISTPOINTCLOUDSOURCESRESPONSE
DESCRIPTOR.message_types_by_name['PointCloudRequest'] = _POINTCLOUDREQUEST
DESCRIPTOR.message_types_by_name['GetPointCloudRequest'] = _GETPOINTCLOUDREQUEST
DESCRIPTOR.message_types_by_name['PointCloudResponse'] = _POINTCLOUDRESPONSE
DESCRIPTOR.message_types_by_name['GetPointCloudResponse'] = _GETPOINTCLOUDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PointCloudSource = _reflection.GeneratedProtocolMessageType('PointCloudSource', (_message.Message,), dict(
  DESCRIPTOR = _POINTCLOUDSOURCE,
  __module__ = 'bosdyn.api.point_cloud_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.PointCloudSource)
  ))
_sym_db.RegisterMessage(PointCloudSource)

PointCloud = _reflection.GeneratedProtocolMessageType('PointCloud', (_message.Message,), dict(

  EncodingParameters = _reflection.GeneratedProtocolMessageType('EncodingParameters', (_message.Message,), dict(
    DESCRIPTOR = _POINTCLOUD_ENCODINGPARAMETERS,
    __module__ = 'bosdyn.api.point_cloud_pb2'
    # @@protoc_insertion_point(class_scope:bosdyn.api.PointCloud.EncodingParameters)
    ))
  ,
  DESCRIPTOR = _POINTCLOUD,
  __module__ = 'bosdyn.api.point_cloud_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.PointCloud)
  ))
_sym_db.RegisterMessage(PointCloud)
_sym_db.RegisterMessage(PointCloud.EncodingParameters)

ListPointCloudSourcesRequest = _reflection.GeneratedProtocolMessageType('ListPointCloudSourcesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPOINTCLOUDSOURCESREQUEST,
  __module__ = 'bosdyn.api.point_cloud_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.ListPointCloudSourcesRequest)
  ))
_sym_db.RegisterMessage(ListPointCloudSourcesRequest)

ListPointCloudSourcesResponse = _reflection.GeneratedProtocolMessageType('ListPointCloudSourcesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTPOINTCLOUDSOURCESRESPONSE,
  __module__ = 'bosdyn.api.point_cloud_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.ListPointCloudSourcesResponse)
  ))
_sym_db.RegisterMessage(ListPointCloudSourcesResponse)

PointCloudRequest = _reflection.GeneratedProtocolMessageType('PointCloudRequest', (_message.Message,), dict(
  DESCRIPTOR = _POINTCLOUDREQUEST,
  __module__ = 'bosdyn.api.point_cloud_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.PointCloudRequest)
  ))
_sym_db.RegisterMessage(PointCloudRequest)

GetPointCloudRequest = _reflection.GeneratedProtocolMessageType('GetPointCloudRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPOINTCLOUDREQUEST,
  __module__ = 'bosdyn.api.point_cloud_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.GetPointCloudRequest)
  ))
_sym_db.RegisterMessage(GetPointCloudRequest)

PointCloudResponse = _reflection.GeneratedProtocolMessageType('PointCloudResponse', (_message.Message,), dict(
  DESCRIPTOR = _POINTCLOUDRESPONSE,
  __module__ = 'bosdyn.api.point_cloud_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.PointCloudResponse)
  ))
_sym_db.RegisterMessage(PointCloudResponse)

GetPointCloudResponse = _reflection.GeneratedProtocolMessageType('GetPointCloudResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPOINTCLOUDRESPONSE,
  __module__ = 'bosdyn.api.point_cloud_pb2'
  # @@protoc_insertion_point(class_scope:bosdyn.api.GetPointCloudResponse)
  ))
_sym_db.RegisterMessage(GetPointCloudResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\017PointCloudProto'))
# @@protoc_insertion_point(module_scope)
