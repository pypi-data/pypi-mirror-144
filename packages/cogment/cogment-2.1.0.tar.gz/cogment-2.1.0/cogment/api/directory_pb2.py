# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cogment/api/directory.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cogment.api import common_pb2 as cogment_dot_api_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cogment/api/directory.proto',
  package='cogmentAPI',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x63ogment/api/directory.proto\x12\ncogmentAPI\x1a\x18\x63ogment/api/common.proto\"m\n\x0fRegisterRequest\x12-\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32\x1b.cogmentAPI.ServiceEndpoint\x12+\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32\x1a.cogmentAPI.ServiceDetails\"\xab\x01\n\rRegisterReply\x12\x30\n\x06status\x18\x01 \x01(\x0e\x32 .cogmentAPI.RegisterReply.Status\x12\x11\n\terror_msg\x18\x02 \x01(\t\x12\x12\n\nservice_id\x18\x03 \x01(\x04\x12\x0e\n\x06secret\x18\x04 \x01(\t\"1\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\"7\n\x11\x44\x65registerRequest\x12\x12\n\nservice_id\x18\x01 \x01(\x04\x12\x0e\n\x06secret\x18\x02 \x01(\t\"\x8b\x01\n\x0f\x44\x65registerReply\x12\x32\n\x06status\x18\x01 \x01(\x0e\x32\".cogmentAPI.DeregisterReply.Status\x12\x11\n\terror_msg\x18\x02 \x01(\t\"1\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\"`\n\x0eInquireRequest\x12\x14\n\nservice_id\x18\x01 \x01(\x04H\x00\x12-\n\x07\x64\x65tails\x18\x02 \x01(\x0b\x32\x1a.cogmentAPI.ServiceDetailsH\x00\x42\t\n\x07inquiry\"9\n\x0cInquireReply\x12)\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1b.cogmentAPI.FullServiceData\"\xa7\x01\n\x0fServiceEndpoint\x12\x36\n\x08protocol\x18\x01 \x01(\x0e\x32$.cogmentAPI.ServiceEndpoint.Protocol\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\r\"<\n\x08Protocol\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04GRPC\x10\x01\x12\x0c\n\x08GRPC_SSL\x10\x02\x12\x0b\n\x07\x43OGMENT\x10\x03\"\xaa\x01\n\x0eServiceDetails\x12%\n\x04type\x18\x01 \x01(\x0e\x32\x17.cogmentAPI.ServiceType\x12>\n\nproperties\x18\x02 \x03(\x0b\x32*.cogmentAPI.ServiceDetails.PropertiesEntry\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x81\x01\n\x0f\x46ullServiceData\x12-\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32\x1b.cogmentAPI.ServiceEndpoint\x12\x12\n\nservice_id\x18\x02 \x01(\x04\x12+\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x1a.cogmentAPI.ServiceDetails*\xbc\x01\n\x0bServiceType\x12\x13\n\x0fUNKNOWN_SERVICE\x10\x00\x12\x1c\n\x18TRIAL_LIFE_CYCLE_SERVICE\x10\x01\x12#\n\x1f\x43LIENT_ACTOR_CONNECTION_SERVICE\x10\x02\x12\x11\n\rACTOR_SERVICE\x10\x03\x12\x17\n\x13\x45NVIRONMENT_SERVICE\x10\x04\x12\x14\n\x10PRE_HOOK_SERVICE\x10\x05\x12\x13\n\x0f\x44\x41TALOG_SERVICE\x10\x06\x32\xae\x02\n\x0b\x44irectorySP\x12H\n\x08Register\x12\x1b.cogmentAPI.RegisterRequest\x1a\x19.cogmentAPI.RegisterReply\"\x00(\x01\x30\x01\x12N\n\nDeregister\x12\x1d.cogmentAPI.DeregisterRequest\x1a\x1b.cogmentAPI.DeregisterReply\"\x00(\x01\x30\x01\x12\x43\n\x07Inquire\x12\x1a.cogmentAPI.InquireRequest\x1a\x18.cogmentAPI.InquireReply\"\x00\x30\x01\x12@\n\x07Version\x12\x1a.cogmentAPI.VersionRequest\x1a\x17.cogmentAPI.VersionInfo\"\x00\x62\x06proto3'
  ,
  dependencies=[cogment_dot_api_dot_common__pb2.DESCRIPTOR,])

_SERVICETYPE = _descriptor.EnumDescriptor(
  name='ServiceType',
  full_name='cogmentAPI.ServiceType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_SERVICE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRIAL_LIFE_CYCLE_SERVICE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_ACTOR_CONNECTION_SERVICE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTOR_SERVICE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENVIRONMENT_SERVICE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRE_HOOK_SERVICE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DATALOG_SERVICE', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1186,
  serialized_end=1374,
)
_sym_db.RegisterEnumDescriptor(_SERVICETYPE)

ServiceType = enum_type_wrapper.EnumTypeWrapper(_SERVICETYPE)
UNKNOWN_SERVICE = 0
TRIAL_LIFE_CYCLE_SERVICE = 1
CLIENT_ACTOR_CONNECTION_SERVICE = 2
ACTOR_SERVICE = 3
ENVIRONMENT_SERVICE = 4
PRE_HOOK_SERVICE = 5
DATALOG_SERVICE = 6


_REGISTERREPLY_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='cogmentAPI.RegisterReply.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=303,
  serialized_end=352,
)
_sym_db.RegisterEnumDescriptor(_REGISTERREPLY_STATUS)

_DEREGISTERREPLY_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='cogmentAPI.DeregisterReply.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=303,
  serialized_end=352,
)
_sym_db.RegisterEnumDescriptor(_DEREGISTERREPLY_STATUS)

_SERVICEENDPOINT_PROTOCOL = _descriptor.EnumDescriptor(
  name='Protocol',
  full_name='cogmentAPI.ServiceEndpoint.Protocol',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GRPC', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GRPC_SSL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COGMENT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=818,
  serialized_end=878,
)
_sym_db.RegisterEnumDescriptor(_SERVICEENDPOINT_PROTOCOL)


_REGISTERREQUEST = _descriptor.Descriptor(
  name='RegisterRequest',
  full_name='cogmentAPI.RegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='cogmentAPI.RegisterRequest.endpoint', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='details', full_name='cogmentAPI.RegisterRequest.details', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=69,
  serialized_end=178,
)


_REGISTERREPLY = _descriptor.Descriptor(
  name='RegisterReply',
  full_name='cogmentAPI.RegisterReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cogmentAPI.RegisterReply.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_msg', full_name='cogmentAPI.RegisterReply.error_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_id', full_name='cogmentAPI.RegisterReply.service_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret', full_name='cogmentAPI.RegisterReply.secret', index=3,
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
    _REGISTERREPLY_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=352,
)


_DEREGISTERREQUEST = _descriptor.Descriptor(
  name='DeregisterRequest',
  full_name='cogmentAPI.DeregisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_id', full_name='cogmentAPI.DeregisterRequest.service_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret', full_name='cogmentAPI.DeregisterRequest.secret', index=1,
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
  serialized_start=354,
  serialized_end=409,
)


_DEREGISTERREPLY = _descriptor.Descriptor(
  name='DeregisterReply',
  full_name='cogmentAPI.DeregisterReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cogmentAPI.DeregisterReply.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_msg', full_name='cogmentAPI.DeregisterReply.error_msg', index=1,
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
    _DEREGISTERREPLY_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=412,
  serialized_end=551,
)


_INQUIREREQUEST = _descriptor.Descriptor(
  name='InquireRequest',
  full_name='cogmentAPI.InquireRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_id', full_name='cogmentAPI.InquireRequest.service_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='details', full_name='cogmentAPI.InquireRequest.details', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='inquiry', full_name='cogmentAPI.InquireRequest.inquiry',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=553,
  serialized_end=649,
)


_INQUIREREPLY = _descriptor.Descriptor(
  name='InquireReply',
  full_name='cogmentAPI.InquireReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='cogmentAPI.InquireReply.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=651,
  serialized_end=708,
)


_SERVICEENDPOINT = _descriptor.Descriptor(
  name='ServiceEndpoint',
  full_name='cogmentAPI.ServiceEndpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol', full_name='cogmentAPI.ServiceEndpoint.protocol', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='cogmentAPI.ServiceEndpoint.hostname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='cogmentAPI.ServiceEndpoint.port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVICEENDPOINT_PROTOCOL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=711,
  serialized_end=878,
)


_SERVICEDETAILS_PROPERTIESENTRY = _descriptor.Descriptor(
  name='PropertiesEntry',
  full_name='cogmentAPI.ServiceDetails.PropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cogmentAPI.ServiceDetails.PropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='cogmentAPI.ServiceDetails.PropertiesEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1002,
  serialized_end=1051,
)

_SERVICEDETAILS = _descriptor.Descriptor(
  name='ServiceDetails',
  full_name='cogmentAPI.ServiceDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='cogmentAPI.ServiceDetails.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='cogmentAPI.ServiceDetails.properties', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SERVICEDETAILS_PROPERTIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=881,
  serialized_end=1051,
)


_FULLSERVICEDATA = _descriptor.Descriptor(
  name='FullServiceData',
  full_name='cogmentAPI.FullServiceData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='cogmentAPI.FullServiceData.endpoint', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_id', full_name='cogmentAPI.FullServiceData.service_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='details', full_name='cogmentAPI.FullServiceData.details', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1054,
  serialized_end=1183,
)

_REGISTERREQUEST.fields_by_name['endpoint'].message_type = _SERVICEENDPOINT
_REGISTERREQUEST.fields_by_name['details'].message_type = _SERVICEDETAILS
_REGISTERREPLY.fields_by_name['status'].enum_type = _REGISTERREPLY_STATUS
_REGISTERREPLY_STATUS.containing_type = _REGISTERREPLY
_DEREGISTERREPLY.fields_by_name['status'].enum_type = _DEREGISTERREPLY_STATUS
_DEREGISTERREPLY_STATUS.containing_type = _DEREGISTERREPLY
_INQUIREREQUEST.fields_by_name['details'].message_type = _SERVICEDETAILS
_INQUIREREQUEST.oneofs_by_name['inquiry'].fields.append(
  _INQUIREREQUEST.fields_by_name['service_id'])
_INQUIREREQUEST.fields_by_name['service_id'].containing_oneof = _INQUIREREQUEST.oneofs_by_name['inquiry']
_INQUIREREQUEST.oneofs_by_name['inquiry'].fields.append(
  _INQUIREREQUEST.fields_by_name['details'])
_INQUIREREQUEST.fields_by_name['details'].containing_oneof = _INQUIREREQUEST.oneofs_by_name['inquiry']
_INQUIREREPLY.fields_by_name['data'].message_type = _FULLSERVICEDATA
_SERVICEENDPOINT.fields_by_name['protocol'].enum_type = _SERVICEENDPOINT_PROTOCOL
_SERVICEENDPOINT_PROTOCOL.containing_type = _SERVICEENDPOINT
_SERVICEDETAILS_PROPERTIESENTRY.containing_type = _SERVICEDETAILS
_SERVICEDETAILS.fields_by_name['type'].enum_type = _SERVICETYPE
_SERVICEDETAILS.fields_by_name['properties'].message_type = _SERVICEDETAILS_PROPERTIESENTRY
_FULLSERVICEDATA.fields_by_name['endpoint'].message_type = _SERVICEENDPOINT
_FULLSERVICEDATA.fields_by_name['details'].message_type = _SERVICEDETAILS
DESCRIPTOR.message_types_by_name['RegisterRequest'] = _REGISTERREQUEST
DESCRIPTOR.message_types_by_name['RegisterReply'] = _REGISTERREPLY
DESCRIPTOR.message_types_by_name['DeregisterRequest'] = _DEREGISTERREQUEST
DESCRIPTOR.message_types_by_name['DeregisterReply'] = _DEREGISTERREPLY
DESCRIPTOR.message_types_by_name['InquireRequest'] = _INQUIREREQUEST
DESCRIPTOR.message_types_by_name['InquireReply'] = _INQUIREREPLY
DESCRIPTOR.message_types_by_name['ServiceEndpoint'] = _SERVICEENDPOINT
DESCRIPTOR.message_types_by_name['ServiceDetails'] = _SERVICEDETAILS
DESCRIPTOR.message_types_by_name['FullServiceData'] = _FULLSERVICEDATA
DESCRIPTOR.enum_types_by_name['ServiceType'] = _SERVICETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'cogment.api.directory_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

RegisterReply = _reflection.GeneratedProtocolMessageType('RegisterReply', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREPLY,
  '__module__' : 'cogment.api.directory_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.RegisterReply)
  })
_sym_db.RegisterMessage(RegisterReply)

DeregisterRequest = _reflection.GeneratedProtocolMessageType('DeregisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEREGISTERREQUEST,
  '__module__' : 'cogment.api.directory_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.DeregisterRequest)
  })
_sym_db.RegisterMessage(DeregisterRequest)

DeregisterReply = _reflection.GeneratedProtocolMessageType('DeregisterReply', (_message.Message,), {
  'DESCRIPTOR' : _DEREGISTERREPLY,
  '__module__' : 'cogment.api.directory_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.DeregisterReply)
  })
_sym_db.RegisterMessage(DeregisterReply)

InquireRequest = _reflection.GeneratedProtocolMessageType('InquireRequest', (_message.Message,), {
  'DESCRIPTOR' : _INQUIREREQUEST,
  '__module__' : 'cogment.api.directory_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.InquireRequest)
  })
_sym_db.RegisterMessage(InquireRequest)

InquireReply = _reflection.GeneratedProtocolMessageType('InquireReply', (_message.Message,), {
  'DESCRIPTOR' : _INQUIREREPLY,
  '__module__' : 'cogment.api.directory_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.InquireReply)
  })
_sym_db.RegisterMessage(InquireReply)

ServiceEndpoint = _reflection.GeneratedProtocolMessageType('ServiceEndpoint', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEENDPOINT,
  '__module__' : 'cogment.api.directory_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.ServiceEndpoint)
  })
_sym_db.RegisterMessage(ServiceEndpoint)

ServiceDetails = _reflection.GeneratedProtocolMessageType('ServiceDetails', (_message.Message,), {

  'PropertiesEntry' : _reflection.GeneratedProtocolMessageType('PropertiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _SERVICEDETAILS_PROPERTIESENTRY,
    '__module__' : 'cogment.api.directory_pb2'
    # @@protoc_insertion_point(class_scope:cogmentAPI.ServiceDetails.PropertiesEntry)
    })
  ,
  'DESCRIPTOR' : _SERVICEDETAILS,
  '__module__' : 'cogment.api.directory_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.ServiceDetails)
  })
_sym_db.RegisterMessage(ServiceDetails)
_sym_db.RegisterMessage(ServiceDetails.PropertiesEntry)

FullServiceData = _reflection.GeneratedProtocolMessageType('FullServiceData', (_message.Message,), {
  'DESCRIPTOR' : _FULLSERVICEDATA,
  '__module__' : 'cogment.api.directory_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.FullServiceData)
  })
_sym_db.RegisterMessage(FullServiceData)


_SERVICEDETAILS_PROPERTIESENTRY._options = None

_DIRECTORYSP = _descriptor.ServiceDescriptor(
  name='DirectorySP',
  full_name='cogmentAPI.DirectorySP',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1377,
  serialized_end=1679,
  methods=[
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='cogmentAPI.DirectorySP.Register',
    index=0,
    containing_service=None,
    input_type=_REGISTERREQUEST,
    output_type=_REGISTERREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Deregister',
    full_name='cogmentAPI.DirectorySP.Deregister',
    index=1,
    containing_service=None,
    input_type=_DEREGISTERREQUEST,
    output_type=_DEREGISTERREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Inquire',
    full_name='cogmentAPI.DirectorySP.Inquire',
    index=2,
    containing_service=None,
    input_type=_INQUIREREQUEST,
    output_type=_INQUIREREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Version',
    full_name='cogmentAPI.DirectorySP.Version',
    index=3,
    containing_service=None,
    input_type=cogment_dot_api_dot_common__pb2._VERSIONREQUEST,
    output_type=cogment_dot_api_dot_common__pb2._VERSIONINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DIRECTORYSP)

DESCRIPTOR.services_by_name['DirectorySP'] = _DIRECTORYSP

# @@protoc_insertion_point(module_scope)
