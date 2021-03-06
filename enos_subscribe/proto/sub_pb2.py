# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sub.proto

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




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sub.proto',
  package='proto',
  serialized_pb=_b('\n\tsub.proto\x12\x05proto\"\t\n\x07IdleReq\"\x1a\n\x07IdleRsp\x12\x0f\n\x07svrTime\x18\x01 \x02(\x03\"J\n\x07\x41uthReq\x12\x11\n\taccessKey\x18\x01 \x02(\t\x12\r\n\x05subId\x18\x02 \x02(\t\x12\x0c\n\x04sign\x18\x03 \x02(\t\x12\x0f\n\x07subType\x18\x04 \x02(\x05\"6\n\x07\x41uthRsp\x12\x0b\n\x03\x61\x63k\x18\x01 \x02(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x11\n\tchannelId\x18\x03 \x01(\t\"e\n\x06SubReq\x12\x10\n\x08\x63\x61tegory\x18\x01 \x02(\x05\x12\x10\n\x08\x63lientId\x18\x02 \x02(\t\x12\r\n\x05subId\x18\x03 \x02(\t\x12\x11\n\taccessKey\x18\x04 \x02(\t\x12\x15\n\rconsumerGroup\x18\x05 \x02(\t\"5\n\x06SubRsp\x12\x0b\n\x03\x61\x63k\x18\x01 \x02(\x05\x12\x11\n\tchannelId\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\"\x15\n\x07PullReq\x12\n\n\x02id\x18\x01 \x02(\x03\"j\n\x07Message\x12\r\n\x05topic\x18\x01 \x02(\t\x12\x11\n\tpartition\x18\x02 \x02(\x05\x12\x0e\n\x06offset\x18\x03 \x02(\x03\x12\x11\n\ttimestamp\x18\x04 \x02(\x03\x12\x0b\n\x03key\x18\x05 \x01(\t\x12\r\n\x05value\x18\x06 \x01(\t\".\n\nMessageDTO\x12 \n\x08messages\x18\x01 \x03(\x0b\x32\x0e.proto.Message\"F\n\x07PullRsp\x12\n\n\x02id\x18\x01 \x02(\x03\x12\x0c\n\x04\x63ode\x18\x02 \x02(\x05\x12!\n\x06msgDTO\x18\x03 \x02(\x0b\x32\x11.proto.MessageDTO\":\n\x06\x43ommit\x12\r\n\x05topic\x18\x01 \x02(\t\x12\x11\n\tpartition\x18\x02 \x02(\x05\x12\x0e\n\x06offset\x18\x03 \x02(\x03\"+\n\tCommitDTO\x12\x1e\n\x07\x63ommits\x18\x01 \x03(\x0b\x32\r.proto.Commit\"\x16\n\x08\x43loseReq\x12\n\n\x02id\x18\x01 \x02(\x03*\xb3\x01\n\x05\x43mdId\x12\x0c\n\x08idle_req\x10\x00\x12\x0c\n\x08idle_rsp\x10\x01\x12\x0c\n\x08\x61uth_req\x10\x02\x12\x0c\n\x08\x61uth_rsp\x10\x03\x12\x0c\n\x08pull_req\x10\x04\x12\x0c\n\x08pull_rsp\x10\x05\x12\x0b\n\x07sub_req\x10\x06\x12\x0b\n\x07sub_rsp\x10\x07\x12\x0e\n\ncommit_req\x10\x08\x12\x0e\n\ncommit_rsp\x10\t\x12\r\n\tclose_req\x10\n\x12\r\n\tclose_rsp\x10\x0b')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CMDID = _descriptor.EnumDescriptor(
  name='CmdId',
  full_name='proto.CmdId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='idle_req', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='idle_rsp', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='auth_req', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='auth_rsp', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='pull_req', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='pull_rsp', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='sub_req', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='sub_rsp', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='commit_req', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='commit_rsp', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='close_req', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='close_rsp', index=11, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=730,
  serialized_end=909,
)
_sym_db.RegisterEnumDescriptor(_CMDID)

CmdId = enum_type_wrapper.EnumTypeWrapper(_CMDID)
idle_req = 0
idle_rsp = 1
auth_req = 2
auth_rsp = 3
pull_req = 4
pull_rsp = 5
sub_req = 6
sub_rsp = 7
commit_req = 8
commit_rsp = 9
close_req = 10
close_rsp = 11



_IDLEREQ = _descriptor.Descriptor(
  name='IdleReq',
  full_name='proto.IdleReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=29,
)


_IDLERSP = _descriptor.Descriptor(
  name='IdleRsp',
  full_name='proto.IdleRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='svrTime', full_name='proto.IdleRsp.svrTime', index=0,
      number=1, type=3, cpp_type=2, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=57,
)


_AUTHREQ = _descriptor.Descriptor(
  name='AuthReq',
  full_name='proto.AuthReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accessKey', full_name='proto.AuthReq.accessKey', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subId', full_name='proto.AuthReq.subId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sign', full_name='proto.AuthReq.sign', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subType', full_name='proto.AuthReq.subType', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=133,
)


_AUTHRSP = _descriptor.Descriptor(
  name='AuthRsp',
  full_name='proto.AuthRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='proto.AuthRsp.ack', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='proto.AuthRsp.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channelId', full_name='proto.AuthRsp.channelId', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=189,
)


_SUBREQ = _descriptor.Descriptor(
  name='SubReq',
  full_name='proto.SubReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='proto.SubReq.category', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='proto.SubReq.clientId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subId', full_name='proto.SubReq.subId', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accessKey', full_name='proto.SubReq.accessKey', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consumerGroup', full_name='proto.SubReq.consumerGroup', index=4,
      number=5, type=9, cpp_type=9, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=292,
)


_SUBRSP = _descriptor.Descriptor(
  name='SubRsp',
  full_name='proto.SubRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ack', full_name='proto.SubRsp.ack', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channelId', full_name='proto.SubRsp.channelId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='proto.SubRsp.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=294,
  serialized_end=347,
)


_PULLREQ = _descriptor.Descriptor(
  name='PullReq',
  full_name='proto.PullReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto.PullReq.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=349,
  serialized_end=370,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='proto.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='proto.Message.topic', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='partition', full_name='proto.Message.partition', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='proto.Message.offset', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='proto.Message.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.Message.key', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.Message.value', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=478,
)


_MESSAGEDTO = _descriptor.Descriptor(
  name='MessageDTO',
  full_name='proto.MessageDTO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='proto.MessageDTO.messages', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=480,
  serialized_end=526,
)


_PULLRSP = _descriptor.Descriptor(
  name='PullRsp',
  full_name='proto.PullRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto.PullRsp.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='proto.PullRsp.code', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msgDTO', full_name='proto.PullRsp.msgDTO', index=2,
      number=3, type=11, cpp_type=10, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=528,
  serialized_end=598,
)


_COMMIT = _descriptor.Descriptor(
  name='Commit',
  full_name='proto.Commit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='proto.Commit.topic', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='partition', full_name='proto.Commit.partition', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='proto.Commit.offset', index=2,
      number=3, type=3, cpp_type=2, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=600,
  serialized_end=658,
)


_COMMITDTO = _descriptor.Descriptor(
  name='CommitDTO',
  full_name='proto.CommitDTO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commits', full_name='proto.CommitDTO.commits', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=660,
  serialized_end=703,
)


_CLOSEREQ = _descriptor.Descriptor(
  name='CloseReq',
  full_name='proto.CloseReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto.CloseReq.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=705,
  serialized_end=727,
)

_MESSAGEDTO.fields_by_name['messages'].message_type = _MESSAGE
_PULLRSP.fields_by_name['msgDTO'].message_type = _MESSAGEDTO
_COMMITDTO.fields_by_name['commits'].message_type = _COMMIT
DESCRIPTOR.message_types_by_name['IdleReq'] = _IDLEREQ
DESCRIPTOR.message_types_by_name['IdleRsp'] = _IDLERSP
DESCRIPTOR.message_types_by_name['AuthReq'] = _AUTHREQ
DESCRIPTOR.message_types_by_name['AuthRsp'] = _AUTHRSP
DESCRIPTOR.message_types_by_name['SubReq'] = _SUBREQ
DESCRIPTOR.message_types_by_name['SubRsp'] = _SUBRSP
DESCRIPTOR.message_types_by_name['PullReq'] = _PULLREQ
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['MessageDTO'] = _MESSAGEDTO
DESCRIPTOR.message_types_by_name['PullRsp'] = _PULLRSP
DESCRIPTOR.message_types_by_name['Commit'] = _COMMIT
DESCRIPTOR.message_types_by_name['CommitDTO'] = _COMMITDTO
DESCRIPTOR.message_types_by_name['CloseReq'] = _CLOSEREQ
DESCRIPTOR.enum_types_by_name['CmdId'] = _CMDID

IdleReq = _reflection.GeneratedProtocolMessageType('IdleReq', (_message.Message,), dict(
  DESCRIPTOR = _IDLEREQ,
  __module__ = 'sub_pb2'
  # @@protoc_insertion_point(class_scope:proto.IdleReq)
  ))
_sym_db.RegisterMessage(IdleReq)

IdleRsp = _reflection.GeneratedProtocolMessageType('IdleRsp', (_message.Message,), dict(
  DESCRIPTOR = _IDLERSP,
  __module__ = 'sub_pb2'
  # @@protoc_insertion_point(class_scope:proto.IdleRsp)
  ))
_sym_db.RegisterMessage(IdleRsp)

AuthReq = _reflection.GeneratedProtocolMessageType('AuthReq', (_message.Message,), dict(
  DESCRIPTOR = _AUTHREQ,
  __module__ = 'sub_pb2'
  # @@protoc_insertion_point(class_scope:proto.AuthReq)
  ))
_sym_db.RegisterMessage(AuthReq)

AuthRsp = _reflection.GeneratedProtocolMessageType('AuthRsp', (_message.Message,), dict(
  DESCRIPTOR = _AUTHRSP,
  __module__ = 'sub_pb2'
  # @@protoc_insertion_point(class_scope:proto.AuthRsp)
  ))
_sym_db.RegisterMessage(AuthRsp)

SubReq = _reflection.GeneratedProtocolMessageType('SubReq', (_message.Message,), dict(
  DESCRIPTOR = _SUBREQ,
  __module__ = 'sub_pb2'
  # @@protoc_insertion_point(class_scope:proto.SubReq)
  ))
_sym_db.RegisterMessage(SubReq)

SubRsp = _reflection.GeneratedProtocolMessageType('SubRsp', (_message.Message,), dict(
  DESCRIPTOR = _SUBRSP,
  __module__ = 'sub_pb2'
  # @@protoc_insertion_point(class_scope:proto.SubRsp)
  ))
_sym_db.RegisterMessage(SubRsp)

PullReq = _reflection.GeneratedProtocolMessageType('PullReq', (_message.Message,), dict(
  DESCRIPTOR = _PULLREQ,
  __module__ = 'sub_pb2'
  # @@protoc_insertion_point(class_scope:proto.PullReq)
  ))
_sym_db.RegisterMessage(PullReq)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'sub_pb2'
  # @@protoc_insertion_point(class_scope:proto.Message)
  ))
_sym_db.RegisterMessage(Message)

MessageDTO = _reflection.GeneratedProtocolMessageType('MessageDTO', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEDTO,
  __module__ = 'sub_pb2'
  # @@protoc_insertion_point(class_scope:proto.MessageDTO)
  ))
_sym_db.RegisterMessage(MessageDTO)

PullRsp = _reflection.GeneratedProtocolMessageType('PullRsp', (_message.Message,), dict(
  DESCRIPTOR = _PULLRSP,
  __module__ = 'sub_pb2'
  # @@protoc_insertion_point(class_scope:proto.PullRsp)
  ))
_sym_db.RegisterMessage(PullRsp)

Commit = _reflection.GeneratedProtocolMessageType('Commit', (_message.Message,), dict(
  DESCRIPTOR = _COMMIT,
  __module__ = 'sub_pb2'
  # @@protoc_insertion_point(class_scope:proto.Commit)
  ))
_sym_db.RegisterMessage(Commit)

CommitDTO = _reflection.GeneratedProtocolMessageType('CommitDTO', (_message.Message,), dict(
  DESCRIPTOR = _COMMITDTO,
  __module__ = 'sub_pb2'
  # @@protoc_insertion_point(class_scope:proto.CommitDTO)
  ))
_sym_db.RegisterMessage(CommitDTO)

CloseReq = _reflection.GeneratedProtocolMessageType('CloseReq', (_message.Message,), dict(
  DESCRIPTOR = _CLOSEREQ,
  __module__ = 'sub_pb2'
  # @@protoc_insertion_point(class_scope:proto.CloseReq)
  ))
_sym_db.RegisterMessage(CloseReq)


# @@protoc_insertion_point(module_scope)
