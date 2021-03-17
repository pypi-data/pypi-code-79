# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mindinsight/debugger/proto/debug_grpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mindinsight.debugger.proto import ms_graph_pb2 as mindinsight_dot_debugger_dot_proto_dot_ms__graph__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mindinsight/debugger/proto/debug_grpc.proto',
  package='debugger',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+mindinsight/debugger/proto/debug_grpc.proto\x12\x08\x64\x65\x62ugger\x1a)mindinsight/debugger/proto/ms_graph.proto\"\x92\x01\n\x08Metadata\x12\x13\n\x0b\x64\x65vice_name\x18\x01 \x01(\t\x12\x10\n\x08\x63ur_step\x18\x02 \x01(\x05\x12\x0f\n\x07\x62\x61\x63kend\x18\x03 \x01(\t\x12\x10\n\x08\x63ur_node\x18\x04 \x01(\t\x12\x15\n\rtraining_done\x18\x05 \x01(\x08\x12\x11\n\tgraph_num\x18\x06 \x01(\x05\x12\x12\n\nms_version\x18\x07 \x01(\t\")\n\x05\x43hunk\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\x12\x10\n\x08\x66inished\x18\x02 \x01(\x08\"\x87\x02\n\nEventReply\x12+\n\x06status\x18\x01 \x01(\x0e\x32\x1b.debugger.EventReply.Status\x12\x0e\n\x04\x65xit\x18\x02 \x01(\x08H\x00\x12#\n\x07run_cmd\x18\x03 \x01(\x0b\x32\x10.debugger.RunCMDH\x00\x12#\n\x07set_cmd\x18\x04 \x01(\x0b\x32\x10.debugger.SetCMDH\x00\x12%\n\x08view_cmd\x18\x05 \x01(\x0b\x32\x11.debugger.ViewCMDH\x00\x12\x19\n\x0fversion_matched\x18\x06 \x01(\x08H\x00\")\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\n\n\x06\x46\x41ILED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x42\x05\n\x03\x63md\"L\n\x06RunCMD\x12\x11\n\trun_level\x18\x01 \x01(\t\x12\x13\n\trun_steps\x18\x02 \x01(\x05H\x00\x12\x13\n\tnode_name\x18\x03 \x01(\tH\x00\x42\x05\n\x03\x63md\"\x81\x01\n\x06SetCMD\x12(\n\x0bwatch_nodes\x18\x01 \x03(\x0b\x32\x13.debugger.WatchNode\x12\x31\n\x0fwatch_condition\x18\x02 \x01(\x0b\x32\x18.debugger.WatchCondition\x12\x0e\n\x06\x64\x65lete\x18\x03 \x01(\x08\x12\n\n\x02id\x18\x04 \x01(\x05\"1\n\x07ViewCMD\x12&\n\x07tensors\x18\x01 \x03(\x0b\x32\x15.debugger.TensorProto\"\x81\x04\n\x0eWatchCondition\x12\x35\n\tcondition\x18\x01 \x01(\x0e\x32\".debugger.WatchCondition.Condition\x12\r\n\x05value\x18\x02 \x01(\x02\x12\x32\n\x06params\x18\x04 \x03(\x0b\x32\".debugger.WatchCondition.Parameter\x1a]\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x64isabled\x18\x02 \x01(\x08\x12\r\n\x05value\x18\x03 \x01(\x01\x12\x0b\n\x03hit\x18\x04 \x01(\x08\x12\x14\n\x0c\x61\x63tual_value\x18\x05 \x01(\x01\"\x95\x02\n\tCondition\x12\x07\n\x03nan\x10\x00\x12\x0c\n\x08overflow\x10\x02\x12\t\n\x05sd_gt\x10\x0b\x12\t\n\x05sd_lt\x10\x0c\x12\x1b\n\x17tensor_general_overflow\x10\r\x12\x19\n\x15tensor_initialization\x10\x0e\x12\x14\n\x10tensor_too_large\x10\x0f\x12\x14\n\x10tensor_too_small\x10\x10\x12\x13\n\x0ftensor_all_zero\x10\x11\x12\x1b\n\x17tensor_change_too_large\x10\x12\x12\x1b\n\x17tensor_change_too_small\x10\x13\x12\x16\n\x12tensor_not_changed\x10\x14\x12\x10\n\x0ctensor_range\x10\x15\"1\n\tWatchNode\x12\x11\n\tnode_name\x18\x01 \x01(\t\x12\x11\n\tnode_type\x18\x02 \x01(\t\"\x89\x01\n\rWatchpointHit\x12%\n\x06tensor\x18\x01 \x01(\x0b\x32\x15.debugger.TensorProto\x12\x31\n\x0fwatch_condition\x18\x02 \x01(\x0b\x32\x18.debugger.WatchCondition\x12\n\n\x02id\x18\x03 \x01(\x05\x12\x12\n\nerror_code\x18\x04 \x01(\x05\x32\x81\x03\n\rEventListener\x12\x35\n\x07WaitCMD\x12\x12.debugger.Metadata\x1a\x14.debugger.EventReply\"\x00\x12:\n\x0cSendMetadata\x12\x12.debugger.Metadata\x1a\x14.debugger.EventReply\"\x00\x12\x36\n\tSendGraph\x12\x0f.debugger.Chunk\x1a\x14.debugger.EventReply\"\x00(\x01\x12>\n\x0bSendTensors\x12\x15.debugger.TensorProto\x1a\x14.debugger.EventReply\"\x00(\x01\x12G\n\x12SendWatchpointHits\x12\x17.debugger.WatchpointHit\x1a\x14.debugger.EventReply\"\x00(\x01\x12<\n\x0fSendMultiGraphs\x12\x0f.debugger.Chunk\x1a\x14.debugger.EventReply\"\x00(\x01\x62\x06proto3')
  ,
  dependencies=[mindinsight_dot_debugger_dot_proto_dot_ms__graph__pb2.DESCRIPTOR,])



_EVENTREPLY_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='debugger.EventReply.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=508,
  serialized_end=549,
)
_sym_db.RegisterEnumDescriptor(_EVENTREPLY_STATUS)

_WATCHCONDITION_CONDITION = _descriptor.EnumDescriptor(
  name='Condition',
  full_name='debugger.WatchCondition.Condition',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='nan', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='overflow', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='sd_gt', index=2, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='sd_lt', index=3, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tensor_general_overflow', index=4, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tensor_initialization', index=5, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tensor_too_large', index=6, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tensor_too_small', index=7, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tensor_all_zero', index=8, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tensor_change_too_large', index=9, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tensor_change_too_small', index=10, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tensor_not_changed', index=11, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='tensor_range', index=12, number=21,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1056,
  serialized_end=1333,
)
_sym_db.RegisterEnumDescriptor(_WATCHCONDITION_CONDITION)


_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='debugger.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_name', full_name='debugger.Metadata.device_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cur_step', full_name='debugger.Metadata.cur_step', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='backend', full_name='debugger.Metadata.backend', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cur_node', full_name='debugger.Metadata.cur_node', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='training_done', full_name='debugger.Metadata.training_done', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graph_num', full_name='debugger.Metadata.graph_num', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ms_version', full_name='debugger.Metadata.ms_version', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=101,
  serialized_end=247,
)


_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='debugger.Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buffer', full_name='debugger.Chunk.buffer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished', full_name='debugger.Chunk.finished', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=249,
  serialized_end=290,
)


_EVENTREPLY = _descriptor.Descriptor(
  name='EventReply',
  full_name='debugger.EventReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='debugger.EventReply.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit', full_name='debugger.EventReply.exit', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_cmd', full_name='debugger.EventReply.run_cmd', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set_cmd', full_name='debugger.EventReply.set_cmd', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view_cmd', full_name='debugger.EventReply.view_cmd', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_matched', full_name='debugger.EventReply.version_matched', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVENTREPLY_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='cmd', full_name='debugger.EventReply.cmd',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=293,
  serialized_end=556,
)


_RUNCMD = _descriptor.Descriptor(
  name='RunCMD',
  full_name='debugger.RunCMD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='run_level', full_name='debugger.RunCMD.run_level', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_steps', full_name='debugger.RunCMD.run_steps', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_name', full_name='debugger.RunCMD.node_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='cmd', full_name='debugger.RunCMD.cmd',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=558,
  serialized_end=634,
)


_SETCMD = _descriptor.Descriptor(
  name='SetCMD',
  full_name='debugger.SetCMD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='watch_nodes', full_name='debugger.SetCMD.watch_nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='watch_condition', full_name='debugger.SetCMD.watch_condition', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delete', full_name='debugger.SetCMD.delete', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='debugger.SetCMD.id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=637,
  serialized_end=766,
)


_VIEWCMD = _descriptor.Descriptor(
  name='ViewCMD',
  full_name='debugger.ViewCMD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensors', full_name='debugger.ViewCMD.tensors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=768,
  serialized_end=817,
)


_WATCHCONDITION_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='debugger.WatchCondition.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='debugger.WatchCondition.Parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='debugger.WatchCondition.Parameter.disabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='debugger.WatchCondition.Parameter.value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hit', full_name='debugger.WatchCondition.Parameter.hit', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actual_value', full_name='debugger.WatchCondition.Parameter.actual_value', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=960,
  serialized_end=1053,
)

_WATCHCONDITION = _descriptor.Descriptor(
  name='WatchCondition',
  full_name='debugger.WatchCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condition', full_name='debugger.WatchCondition.condition', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='debugger.WatchCondition.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params', full_name='debugger.WatchCondition.params', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WATCHCONDITION_PARAMETER, ],
  enum_types=[
    _WATCHCONDITION_CONDITION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=820,
  serialized_end=1333,
)


_WATCHNODE = _descriptor.Descriptor(
  name='WatchNode',
  full_name='debugger.WatchNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_name', full_name='debugger.WatchNode.node_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_type', full_name='debugger.WatchNode.node_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1335,
  serialized_end=1384,
)


_WATCHPOINTHIT = _descriptor.Descriptor(
  name='WatchpointHit',
  full_name='debugger.WatchpointHit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor', full_name='debugger.WatchpointHit.tensor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='watch_condition', full_name='debugger.WatchpointHit.watch_condition', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='debugger.WatchpointHit.id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='debugger.WatchpointHit.error_code', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1387,
  serialized_end=1524,
)

_EVENTREPLY.fields_by_name['status'].enum_type = _EVENTREPLY_STATUS
_EVENTREPLY.fields_by_name['run_cmd'].message_type = _RUNCMD
_EVENTREPLY.fields_by_name['set_cmd'].message_type = _SETCMD
_EVENTREPLY.fields_by_name['view_cmd'].message_type = _VIEWCMD
_EVENTREPLY_STATUS.containing_type = _EVENTREPLY
_EVENTREPLY.oneofs_by_name['cmd'].fields.append(
  _EVENTREPLY.fields_by_name['exit'])
_EVENTREPLY.fields_by_name['exit'].containing_oneof = _EVENTREPLY.oneofs_by_name['cmd']
_EVENTREPLY.oneofs_by_name['cmd'].fields.append(
  _EVENTREPLY.fields_by_name['run_cmd'])
_EVENTREPLY.fields_by_name['run_cmd'].containing_oneof = _EVENTREPLY.oneofs_by_name['cmd']
_EVENTREPLY.oneofs_by_name['cmd'].fields.append(
  _EVENTREPLY.fields_by_name['set_cmd'])
_EVENTREPLY.fields_by_name['set_cmd'].containing_oneof = _EVENTREPLY.oneofs_by_name['cmd']
_EVENTREPLY.oneofs_by_name['cmd'].fields.append(
  _EVENTREPLY.fields_by_name['view_cmd'])
_EVENTREPLY.fields_by_name['view_cmd'].containing_oneof = _EVENTREPLY.oneofs_by_name['cmd']
_EVENTREPLY.oneofs_by_name['cmd'].fields.append(
  _EVENTREPLY.fields_by_name['version_matched'])
_EVENTREPLY.fields_by_name['version_matched'].containing_oneof = _EVENTREPLY.oneofs_by_name['cmd']
_RUNCMD.oneofs_by_name['cmd'].fields.append(
  _RUNCMD.fields_by_name['run_steps'])
_RUNCMD.fields_by_name['run_steps'].containing_oneof = _RUNCMD.oneofs_by_name['cmd']
_RUNCMD.oneofs_by_name['cmd'].fields.append(
  _RUNCMD.fields_by_name['node_name'])
_RUNCMD.fields_by_name['node_name'].containing_oneof = _RUNCMD.oneofs_by_name['cmd']
_SETCMD.fields_by_name['watch_nodes'].message_type = _WATCHNODE
_SETCMD.fields_by_name['watch_condition'].message_type = _WATCHCONDITION
_VIEWCMD.fields_by_name['tensors'].message_type = mindinsight_dot_debugger_dot_proto_dot_ms__graph__pb2._TENSORPROTO
_WATCHCONDITION_PARAMETER.containing_type = _WATCHCONDITION
_WATCHCONDITION.fields_by_name['condition'].enum_type = _WATCHCONDITION_CONDITION
_WATCHCONDITION.fields_by_name['params'].message_type = _WATCHCONDITION_PARAMETER
_WATCHCONDITION_CONDITION.containing_type = _WATCHCONDITION
_WATCHPOINTHIT.fields_by_name['tensor'].message_type = mindinsight_dot_debugger_dot_proto_dot_ms__graph__pb2._TENSORPROTO
_WATCHPOINTHIT.fields_by_name['watch_condition'].message_type = _WATCHCONDITION
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK
DESCRIPTOR.message_types_by_name['EventReply'] = _EVENTREPLY
DESCRIPTOR.message_types_by_name['RunCMD'] = _RUNCMD
DESCRIPTOR.message_types_by_name['SetCMD'] = _SETCMD
DESCRIPTOR.message_types_by_name['ViewCMD'] = _VIEWCMD
DESCRIPTOR.message_types_by_name['WatchCondition'] = _WATCHCONDITION
DESCRIPTOR.message_types_by_name['WatchNode'] = _WATCHNODE
DESCRIPTOR.message_types_by_name['WatchpointHit'] = _WATCHPOINTHIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'mindinsight.debugger.proto.debug_grpc_pb2'
  # @@protoc_insertion_point(class_scope:debugger.Metadata)
  })
_sym_db.RegisterMessage(Metadata)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), {
  'DESCRIPTOR' : _CHUNK,
  '__module__' : 'mindinsight.debugger.proto.debug_grpc_pb2'
  # @@protoc_insertion_point(class_scope:debugger.Chunk)
  })
_sym_db.RegisterMessage(Chunk)

EventReply = _reflection.GeneratedProtocolMessageType('EventReply', (_message.Message,), {
  'DESCRIPTOR' : _EVENTREPLY,
  '__module__' : 'mindinsight.debugger.proto.debug_grpc_pb2'
  # @@protoc_insertion_point(class_scope:debugger.EventReply)
  })
_sym_db.RegisterMessage(EventReply)

RunCMD = _reflection.GeneratedProtocolMessageType('RunCMD', (_message.Message,), {
  'DESCRIPTOR' : _RUNCMD,
  '__module__' : 'mindinsight.debugger.proto.debug_grpc_pb2'
  # @@protoc_insertion_point(class_scope:debugger.RunCMD)
  })
_sym_db.RegisterMessage(RunCMD)

SetCMD = _reflection.GeneratedProtocolMessageType('SetCMD', (_message.Message,), {
  'DESCRIPTOR' : _SETCMD,
  '__module__' : 'mindinsight.debugger.proto.debug_grpc_pb2'
  # @@protoc_insertion_point(class_scope:debugger.SetCMD)
  })
_sym_db.RegisterMessage(SetCMD)

ViewCMD = _reflection.GeneratedProtocolMessageType('ViewCMD', (_message.Message,), {
  'DESCRIPTOR' : _VIEWCMD,
  '__module__' : 'mindinsight.debugger.proto.debug_grpc_pb2'
  # @@protoc_insertion_point(class_scope:debugger.ViewCMD)
  })
_sym_db.RegisterMessage(ViewCMD)

WatchCondition = _reflection.GeneratedProtocolMessageType('WatchCondition', (_message.Message,), {

  'Parameter' : _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), {
    'DESCRIPTOR' : _WATCHCONDITION_PARAMETER,
    '__module__' : 'mindinsight.debugger.proto.debug_grpc_pb2'
    # @@protoc_insertion_point(class_scope:debugger.WatchCondition.Parameter)
    })
  ,
  'DESCRIPTOR' : _WATCHCONDITION,
  '__module__' : 'mindinsight.debugger.proto.debug_grpc_pb2'
  # @@protoc_insertion_point(class_scope:debugger.WatchCondition)
  })
_sym_db.RegisterMessage(WatchCondition)
_sym_db.RegisterMessage(WatchCondition.Parameter)

WatchNode = _reflection.GeneratedProtocolMessageType('WatchNode', (_message.Message,), {
  'DESCRIPTOR' : _WATCHNODE,
  '__module__' : 'mindinsight.debugger.proto.debug_grpc_pb2'
  # @@protoc_insertion_point(class_scope:debugger.WatchNode)
  })
_sym_db.RegisterMessage(WatchNode)

WatchpointHit = _reflection.GeneratedProtocolMessageType('WatchpointHit', (_message.Message,), {
  'DESCRIPTOR' : _WATCHPOINTHIT,
  '__module__' : 'mindinsight.debugger.proto.debug_grpc_pb2'
  # @@protoc_insertion_point(class_scope:debugger.WatchpointHit)
  })
_sym_db.RegisterMessage(WatchpointHit)



_EVENTLISTENER = _descriptor.ServiceDescriptor(
  name='EventListener',
  full_name='debugger.EventListener',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1527,
  serialized_end=1912,
  methods=[
  _descriptor.MethodDescriptor(
    name='WaitCMD',
    full_name='debugger.EventListener.WaitCMD',
    index=0,
    containing_service=None,
    input_type=_METADATA,
    output_type=_EVENTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendMetadata',
    full_name='debugger.EventListener.SendMetadata',
    index=1,
    containing_service=None,
    input_type=_METADATA,
    output_type=_EVENTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendGraph',
    full_name='debugger.EventListener.SendGraph',
    index=2,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_EVENTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendTensors',
    full_name='debugger.EventListener.SendTensors',
    index=3,
    containing_service=None,
    input_type=mindinsight_dot_debugger_dot_proto_dot_ms__graph__pb2._TENSORPROTO,
    output_type=_EVENTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendWatchpointHits',
    full_name='debugger.EventListener.SendWatchpointHits',
    index=4,
    containing_service=None,
    input_type=_WATCHPOINTHIT,
    output_type=_EVENTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendMultiGraphs',
    full_name='debugger.EventListener.SendMultiGraphs',
    index=5,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_EVENTREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTLISTENER)

DESCRIPTOR.services_by_name['EventListener'] = _EVENTLISTENER

# @@protoc_insertion_point(module_scope)
