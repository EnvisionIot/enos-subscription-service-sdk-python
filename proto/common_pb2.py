# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

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
  name='common.proto',
  package='proto',
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\x05proto\"S\n\x0bTransferPkg\x12\r\n\x05\x63mdId\x18\x01 \x02(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x02(\x0c\x12\r\n\x05seqId\x18\x03 \x02(\x05\x12\x0b\n\x03zip\x18\x04 \x01(\x08\x12\x0b\n\x03ver\x18\x05 \x01(\r\"Q\n\x08\x41sterPkg\x12\r\n\x05seqno\x18\x01 \x02(\x05\x12\r\n\x05\x61\x63kno\x18\x02 \x02(\x05\x12\x0c\n\x04\x66lag\x18\x03 \x01(\x05\x12\x0b\n\x03wnd\x18\x04 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x07 \x03(\x0c\"\r\n\x0bTransferAck\"\'\n\tPointAttr\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"0\n\x0cSliceTrigger\x12\x0e\n\x06isSame\x18\x01 \x02(\x08\x12\x10\n\x08sliceLen\x18\x02 \x02(\x03\"\x85\x01\n\tKVPair2_0\x12\r\n\x05point\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\x12\x0e\n\x06\x64omain\x18\x03 \x02(\t\x12\x1f\n\x05\x61ttrs\x18\x04 \x03(\x0b\x32\x10.proto.PointAttr\x12)\n\x0csliceTrigger\x18\x05 \x03(\x0b\x32\x13.proto.SliceTrigger\"B\n\x0fKVPairDevice2_0\x12\x1f\n\x05\x64\x61tas\x18\x01 \x03(\x0b\x32\x10.proto.KVPair2_0\x12\x0e\n\x06\x64\x65vice\x18\x02 \x02(\t\"e\n\x0fKVPairRecord2_0\x12\x13\n\x0b\x63ollectTime\x18\x01 \x02(\x03\x12+\n\x0b\x64\x65viceDatas\x18\x02 \x03(\x0b\x32\x16.proto.KVPairDevice2_0\x12\x10\n\x08sendTime\x18\x03 \x02(\x03\"i\n\x06KVPair\x12\x10\n\x08\x64\x65viceId\x18\x01 \x02(\t\x12\r\n\x05point\x18\x02 \x02(\t\x12\r\n\x05value\x18\x03 \x02(\t\x12\x1f\n\x05\x61ttrs\x18\x04 \x03(\x0b\x32\x10.proto.PointAttr\x12\x0e\n\x06\x64omain\x18\x05 \x02(\t\"E\n\x0cKVPairRecord\x12\x0b\n\x03utc\x18\x01 \x02(\x03\x12\x1c\n\x05\x64\x61tas\x18\x02 \x03(\x0b\x32\r.proto.KVPair\x12\n\n\x02ts\x18\x03 \x01(\x03*)\n\rCommonMsgType\x12\x18\n\x14\x45NUM_KVPairRecord2_0\x10\x65')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_COMMONMSGTYPE = _descriptor.EnumDescriptor(
  name='CommonMsgType',
  full_name='proto.CommonMsgType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENUM_KVPairRecord2_0', index=0, number=101,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=782,
  serialized_end=823,
)
_sym_db.RegisterEnumDescriptor(_COMMONMSGTYPE)

CommonMsgType = enum_type_wrapper.EnumTypeWrapper(_COMMONMSGTYPE)
ENUM_KVPairRecord2_0 = 101



_TRANSFERPKG = _descriptor.Descriptor(
  name='TransferPkg',
  full_name='proto.TransferPkg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmdId', full_name='proto.TransferPkg.cmdId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='proto.TransferPkg.data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seqId', full_name='proto.TransferPkg.seqId', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zip', full_name='proto.TransferPkg.zip', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ver', full_name='proto.TransferPkg.ver', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=23,
  serialized_end=106,
)


_ASTERPKG = _descriptor.Descriptor(
  name='AsterPkg',
  full_name='proto.AsterPkg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='seqno', full_name='proto.AsterPkg.seqno', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ackno', full_name='proto.AsterPkg.ackno', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flag', full_name='proto.AsterPkg.flag', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wnd', full_name='proto.AsterPkg.wnd', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='proto.AsterPkg.data', index=4,
      number=7, type=12, cpp_type=9, label=3,
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
  serialized_start=108,
  serialized_end=189,
)


_TRANSFERACK = _descriptor.Descriptor(
  name='TransferAck',
  full_name='proto.TransferAck',
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
  serialized_start=191,
  serialized_end=204,
)


_POINTATTR = _descriptor.Descriptor(
  name='PointAttr',
  full_name='proto.PointAttr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.PointAttr.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.PointAttr.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=206,
  serialized_end=245,
)


_SLICETRIGGER = _descriptor.Descriptor(
  name='SliceTrigger',
  full_name='proto.SliceTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='isSame', full_name='proto.SliceTrigger.isSame', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sliceLen', full_name='proto.SliceTrigger.sliceLen', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  serialized_start=247,
  serialized_end=295,
)


_KVPAIR2_0 = _descriptor.Descriptor(
  name='KVPair2_0',
  full_name='proto.KVPair2_0',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='point', full_name='proto.KVPair2_0.point', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.KVPair2_0.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain', full_name='proto.KVPair2_0.domain', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attrs', full_name='proto.KVPair2_0.attrs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sliceTrigger', full_name='proto.KVPair2_0.sliceTrigger', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=298,
  serialized_end=431,
)


_KVPAIRDEVICE2_0 = _descriptor.Descriptor(
  name='KVPairDevice2_0',
  full_name='proto.KVPairDevice2_0',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datas', full_name='proto.KVPairDevice2_0.datas', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device', full_name='proto.KVPairDevice2_0.device', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=433,
  serialized_end=499,
)


_KVPAIRRECORD2_0 = _descriptor.Descriptor(
  name='KVPairRecord2_0',
  full_name='proto.KVPairRecord2_0',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='collectTime', full_name='proto.KVPairRecord2_0.collectTime', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviceDatas', full_name='proto.KVPairRecord2_0.deviceDatas', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sendTime', full_name='proto.KVPairRecord2_0.sendTime', index=2,
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
  serialized_start=501,
  serialized_end=602,
)


_KVPAIR = _descriptor.Descriptor(
  name='KVPair',
  full_name='proto.KVPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='proto.KVPair.deviceId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point', full_name='proto.KVPair.point', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.KVPair.value', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attrs', full_name='proto.KVPair.attrs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain', full_name='proto.KVPair.domain', index=4,
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
  serialized_start=604,
  serialized_end=709,
)


_KVPAIRRECORD = _descriptor.Descriptor(
  name='KVPairRecord',
  full_name='proto.KVPairRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='utc', full_name='proto.KVPairRecord.utc', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datas', full_name='proto.KVPairRecord.datas', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ts', full_name='proto.KVPairRecord.ts', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=711,
  serialized_end=780,
)

_KVPAIR2_0.fields_by_name['attrs'].message_type = _POINTATTR
_KVPAIR2_0.fields_by_name['sliceTrigger'].message_type = _SLICETRIGGER
_KVPAIRDEVICE2_0.fields_by_name['datas'].message_type = _KVPAIR2_0
_KVPAIRRECORD2_0.fields_by_name['deviceDatas'].message_type = _KVPAIRDEVICE2_0
_KVPAIR.fields_by_name['attrs'].message_type = _POINTATTR
_KVPAIRRECORD.fields_by_name['datas'].message_type = _KVPAIR
DESCRIPTOR.message_types_by_name['TransferPkg'] = _TRANSFERPKG
DESCRIPTOR.message_types_by_name['AsterPkg'] = _ASTERPKG
DESCRIPTOR.message_types_by_name['TransferAck'] = _TRANSFERACK
DESCRIPTOR.message_types_by_name['PointAttr'] = _POINTATTR
DESCRIPTOR.message_types_by_name['SliceTrigger'] = _SLICETRIGGER
DESCRIPTOR.message_types_by_name['KVPair2_0'] = _KVPAIR2_0
DESCRIPTOR.message_types_by_name['KVPairDevice2_0'] = _KVPAIRDEVICE2_0
DESCRIPTOR.message_types_by_name['KVPairRecord2_0'] = _KVPAIRRECORD2_0
DESCRIPTOR.message_types_by_name['KVPair'] = _KVPAIR
DESCRIPTOR.message_types_by_name['KVPairRecord'] = _KVPAIRRECORD
DESCRIPTOR.enum_types_by_name['CommonMsgType'] = _COMMONMSGTYPE

TransferPkg = _reflection.GeneratedProtocolMessageType('TransferPkg', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERPKG,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.TransferPkg)
  ))
_sym_db.RegisterMessage(TransferPkg)

AsterPkg = _reflection.GeneratedProtocolMessageType('AsterPkg', (_message.Message,), dict(
  DESCRIPTOR = _ASTERPKG,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.AsterPkg)
  ))
_sym_db.RegisterMessage(AsterPkg)

TransferAck = _reflection.GeneratedProtocolMessageType('TransferAck', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERACK,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.TransferAck)
  ))
_sym_db.RegisterMessage(TransferAck)

PointAttr = _reflection.GeneratedProtocolMessageType('PointAttr', (_message.Message,), dict(
  DESCRIPTOR = _POINTATTR,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.PointAttr)
  ))
_sym_db.RegisterMessage(PointAttr)

SliceTrigger = _reflection.GeneratedProtocolMessageType('SliceTrigger', (_message.Message,), dict(
  DESCRIPTOR = _SLICETRIGGER,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.SliceTrigger)
  ))
_sym_db.RegisterMessage(SliceTrigger)

KVPair2_0 = _reflection.GeneratedProtocolMessageType('KVPair2_0', (_message.Message,), dict(
  DESCRIPTOR = _KVPAIR2_0,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.KVPair2_0)
  ))
_sym_db.RegisterMessage(KVPair2_0)

KVPairDevice2_0 = _reflection.GeneratedProtocolMessageType('KVPairDevice2_0', (_message.Message,), dict(
  DESCRIPTOR = _KVPAIRDEVICE2_0,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.KVPairDevice2_0)
  ))
_sym_db.RegisterMessage(KVPairDevice2_0)

KVPairRecord2_0 = _reflection.GeneratedProtocolMessageType('KVPairRecord2_0', (_message.Message,), dict(
  DESCRIPTOR = _KVPAIRRECORD2_0,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.KVPairRecord2_0)
  ))
_sym_db.RegisterMessage(KVPairRecord2_0)

KVPair = _reflection.GeneratedProtocolMessageType('KVPair', (_message.Message,), dict(
  DESCRIPTOR = _KVPAIR,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.KVPair)
  ))
_sym_db.RegisterMessage(KVPair)

KVPairRecord = _reflection.GeneratedProtocolMessageType('KVPairRecord', (_message.Message,), dict(
  DESCRIPTOR = _KVPAIRRECORD,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:proto.KVPairRecord)
  ))
_sym_db.RegisterMessage(KVPairRecord)


# @@protoc_insertion_point(module_scope)
