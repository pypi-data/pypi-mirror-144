# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cogment/api/environment.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cogment.api import common_pb2 as cogment_dot_api_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cogment/api/environment.proto',
  package='cogmentAPI',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x63ogment/api/environment.proto\x12\ncogmentAPI\x1a\x18\x63ogment/api/common.proto\"^\n\x0eObservationSet\x12\x0f\n\x07tick_id\x18\x01 \x01(\x12\x12\x11\n\ttimestamp\x18\x02 \x01(\x06\x12\x14\n\x0cobservations\x18\x03 \x03(\x0c\x12\x12\n\nactors_map\x18\x04 \x03(\x05\"@\n\tActionSet\x12\x0f\n\x07tick_id\x18\x01 \x01(\x04\x12\x11\n\ttimestamp\x18\x02 \x01(\x06\x12\x0f\n\x07\x61\x63tions\x18\x03 \x03(\x0c\"\xe4\x01\n\x10\x45nvRunTrialInput\x12-\n\x05state\x18\x01 \x01(\x0e\x32\x1e.cogmentAPI.CommunicationState\x12\x31\n\ninit_input\x18\x02 \x01(\x0b\x32\x1b.cogmentAPI.EnvInitialInputH\x00\x12+\n\naction_set\x18\x03 \x01(\x0b\x32\x15.cogmentAPI.ActionSetH\x00\x12&\n\x07message\x18\x04 \x01(\x0b\x32\x13.cogmentAPI.MessageH\x00\x12\x11\n\x07\x64\x65tails\x18\x05 \x01(\tH\x00\x42\x06\n\x04\x64\x61ta\"\x97\x02\n\x11\x45nvRunTrialOutput\x12-\n\x05state\x18\x01 \x01(\x0e\x32\x1e.cogmentAPI.CommunicationState\x12\x33\n\x0binit_output\x18\x02 \x01(\x0b\x32\x1c.cogmentAPI.EnvInitialOutputH\x00\x12\x35\n\x0fobservation_set\x18\x03 \x01(\x0b\x32\x1a.cogmentAPI.ObservationSetH\x00\x12$\n\x06reward\x18\x04 \x01(\x0b\x32\x12.cogmentAPI.RewardH\x00\x12&\n\x07message\x18\x05 \x01(\x0b\x32\x13.cogmentAPI.MessageH\x00\x12\x11\n\x07\x64\x65tails\x18\x06 \x01(\tH\x00\x42\x06\n\x04\x64\x61ta\"\xa3\x01\n\x0f\x45nvInitialInput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\timpl_name\x18\x02 \x01(\t\x12\x0f\n\x07tick_id\x18\x03 \x01(\x04\x12/\n\x0f\x61\x63tors_in_trial\x18\x04 \x03(\x0b\x32\x16.cogmentAPI.TrialActor\x12-\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\x1d.cogmentAPI.EnvironmentConfig\"\x12\n\x10\x45nvInitialOutput2\xa0\x01\n\rEnvironmentSP\x12M\n\x08RunTrial\x12\x1c.cogmentAPI.EnvRunTrialInput\x1a\x1d.cogmentAPI.EnvRunTrialOutput\"\x00(\x01\x30\x01\x12@\n\x07Version\x12\x1a.cogmentAPI.VersionRequest\x1a\x17.cogmentAPI.VersionInfo\"\x00\x62\x06proto3'
  ,
  dependencies=[cogment_dot_api_dot_common__pb2.DESCRIPTOR,])




_OBSERVATIONSET = _descriptor.Descriptor(
  name='ObservationSet',
  full_name='cogmentAPI.ObservationSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tick_id', full_name='cogmentAPI.ObservationSet.tick_id', index=0,
      number=1, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cogmentAPI.ObservationSet.timestamp', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='observations', full_name='cogmentAPI.ObservationSet.observations', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actors_map', full_name='cogmentAPI.ObservationSet.actors_map', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=71,
  serialized_end=165,
)


_ACTIONSET = _descriptor.Descriptor(
  name='ActionSet',
  full_name='cogmentAPI.ActionSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tick_id', full_name='cogmentAPI.ActionSet.tick_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='cogmentAPI.ActionSet.timestamp', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actions', full_name='cogmentAPI.ActionSet.actions', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=167,
  serialized_end=231,
)


_ENVRUNTRIALINPUT = _descriptor.Descriptor(
  name='EnvRunTrialInput',
  full_name='cogmentAPI.EnvRunTrialInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='cogmentAPI.EnvRunTrialInput.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='init_input', full_name='cogmentAPI.EnvRunTrialInput.init_input', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action_set', full_name='cogmentAPI.EnvRunTrialInput.action_set', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='cogmentAPI.EnvRunTrialInput.message', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='details', full_name='cogmentAPI.EnvRunTrialInput.details', index=4,
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
    _descriptor.OneofDescriptor(
      name='data', full_name='cogmentAPI.EnvRunTrialInput.data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=234,
  serialized_end=462,
)


_ENVRUNTRIALOUTPUT = _descriptor.Descriptor(
  name='EnvRunTrialOutput',
  full_name='cogmentAPI.EnvRunTrialOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='cogmentAPI.EnvRunTrialOutput.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='init_output', full_name='cogmentAPI.EnvRunTrialOutput.init_output', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='observation_set', full_name='cogmentAPI.EnvRunTrialOutput.observation_set', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reward', full_name='cogmentAPI.EnvRunTrialOutput.reward', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='cogmentAPI.EnvRunTrialOutput.message', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='details', full_name='cogmentAPI.EnvRunTrialOutput.details', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='data', full_name='cogmentAPI.EnvRunTrialOutput.data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=465,
  serialized_end=744,
)


_ENVINITIALINPUT = _descriptor.Descriptor(
  name='EnvInitialInput',
  full_name='cogmentAPI.EnvInitialInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cogmentAPI.EnvInitialInput.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='impl_name', full_name='cogmentAPI.EnvInitialInput.impl_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tick_id', full_name='cogmentAPI.EnvInitialInput.tick_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actors_in_trial', full_name='cogmentAPI.EnvInitialInput.actors_in_trial', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='cogmentAPI.EnvInitialInput.config', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=747,
  serialized_end=910,
)


_ENVINITIALOUTPUT = _descriptor.Descriptor(
  name='EnvInitialOutput',
  full_name='cogmentAPI.EnvInitialOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=912,
  serialized_end=930,
)

_ENVRUNTRIALINPUT.fields_by_name['state'].enum_type = cogment_dot_api_dot_common__pb2._COMMUNICATIONSTATE
_ENVRUNTRIALINPUT.fields_by_name['init_input'].message_type = _ENVINITIALINPUT
_ENVRUNTRIALINPUT.fields_by_name['action_set'].message_type = _ACTIONSET
_ENVRUNTRIALINPUT.fields_by_name['message'].message_type = cogment_dot_api_dot_common__pb2._MESSAGE
_ENVRUNTRIALINPUT.oneofs_by_name['data'].fields.append(
  _ENVRUNTRIALINPUT.fields_by_name['init_input'])
_ENVRUNTRIALINPUT.fields_by_name['init_input'].containing_oneof = _ENVRUNTRIALINPUT.oneofs_by_name['data']
_ENVRUNTRIALINPUT.oneofs_by_name['data'].fields.append(
  _ENVRUNTRIALINPUT.fields_by_name['action_set'])
_ENVRUNTRIALINPUT.fields_by_name['action_set'].containing_oneof = _ENVRUNTRIALINPUT.oneofs_by_name['data']
_ENVRUNTRIALINPUT.oneofs_by_name['data'].fields.append(
  _ENVRUNTRIALINPUT.fields_by_name['message'])
_ENVRUNTRIALINPUT.fields_by_name['message'].containing_oneof = _ENVRUNTRIALINPUT.oneofs_by_name['data']
_ENVRUNTRIALINPUT.oneofs_by_name['data'].fields.append(
  _ENVRUNTRIALINPUT.fields_by_name['details'])
_ENVRUNTRIALINPUT.fields_by_name['details'].containing_oneof = _ENVRUNTRIALINPUT.oneofs_by_name['data']
_ENVRUNTRIALOUTPUT.fields_by_name['state'].enum_type = cogment_dot_api_dot_common__pb2._COMMUNICATIONSTATE
_ENVRUNTRIALOUTPUT.fields_by_name['init_output'].message_type = _ENVINITIALOUTPUT
_ENVRUNTRIALOUTPUT.fields_by_name['observation_set'].message_type = _OBSERVATIONSET
_ENVRUNTRIALOUTPUT.fields_by_name['reward'].message_type = cogment_dot_api_dot_common__pb2._REWARD
_ENVRUNTRIALOUTPUT.fields_by_name['message'].message_type = cogment_dot_api_dot_common__pb2._MESSAGE
_ENVRUNTRIALOUTPUT.oneofs_by_name['data'].fields.append(
  _ENVRUNTRIALOUTPUT.fields_by_name['init_output'])
_ENVRUNTRIALOUTPUT.fields_by_name['init_output'].containing_oneof = _ENVRUNTRIALOUTPUT.oneofs_by_name['data']
_ENVRUNTRIALOUTPUT.oneofs_by_name['data'].fields.append(
  _ENVRUNTRIALOUTPUT.fields_by_name['observation_set'])
_ENVRUNTRIALOUTPUT.fields_by_name['observation_set'].containing_oneof = _ENVRUNTRIALOUTPUT.oneofs_by_name['data']
_ENVRUNTRIALOUTPUT.oneofs_by_name['data'].fields.append(
  _ENVRUNTRIALOUTPUT.fields_by_name['reward'])
_ENVRUNTRIALOUTPUT.fields_by_name['reward'].containing_oneof = _ENVRUNTRIALOUTPUT.oneofs_by_name['data']
_ENVRUNTRIALOUTPUT.oneofs_by_name['data'].fields.append(
  _ENVRUNTRIALOUTPUT.fields_by_name['message'])
_ENVRUNTRIALOUTPUT.fields_by_name['message'].containing_oneof = _ENVRUNTRIALOUTPUT.oneofs_by_name['data']
_ENVRUNTRIALOUTPUT.oneofs_by_name['data'].fields.append(
  _ENVRUNTRIALOUTPUT.fields_by_name['details'])
_ENVRUNTRIALOUTPUT.fields_by_name['details'].containing_oneof = _ENVRUNTRIALOUTPUT.oneofs_by_name['data']
_ENVINITIALINPUT.fields_by_name['actors_in_trial'].message_type = cogment_dot_api_dot_common__pb2._TRIALACTOR
_ENVINITIALINPUT.fields_by_name['config'].message_type = cogment_dot_api_dot_common__pb2._ENVIRONMENTCONFIG
DESCRIPTOR.message_types_by_name['ObservationSet'] = _OBSERVATIONSET
DESCRIPTOR.message_types_by_name['ActionSet'] = _ACTIONSET
DESCRIPTOR.message_types_by_name['EnvRunTrialInput'] = _ENVRUNTRIALINPUT
DESCRIPTOR.message_types_by_name['EnvRunTrialOutput'] = _ENVRUNTRIALOUTPUT
DESCRIPTOR.message_types_by_name['EnvInitialInput'] = _ENVINITIALINPUT
DESCRIPTOR.message_types_by_name['EnvInitialOutput'] = _ENVINITIALOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObservationSet = _reflection.GeneratedProtocolMessageType('ObservationSet', (_message.Message,), {
  'DESCRIPTOR' : _OBSERVATIONSET,
  '__module__' : 'cogment.api.environment_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.ObservationSet)
  })
_sym_db.RegisterMessage(ObservationSet)

ActionSet = _reflection.GeneratedProtocolMessageType('ActionSet', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONSET,
  '__module__' : 'cogment.api.environment_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.ActionSet)
  })
_sym_db.RegisterMessage(ActionSet)

EnvRunTrialInput = _reflection.GeneratedProtocolMessageType('EnvRunTrialInput', (_message.Message,), {
  'DESCRIPTOR' : _ENVRUNTRIALINPUT,
  '__module__' : 'cogment.api.environment_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.EnvRunTrialInput)
  })
_sym_db.RegisterMessage(EnvRunTrialInput)

EnvRunTrialOutput = _reflection.GeneratedProtocolMessageType('EnvRunTrialOutput', (_message.Message,), {
  'DESCRIPTOR' : _ENVRUNTRIALOUTPUT,
  '__module__' : 'cogment.api.environment_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.EnvRunTrialOutput)
  })
_sym_db.RegisterMessage(EnvRunTrialOutput)

EnvInitialInput = _reflection.GeneratedProtocolMessageType('EnvInitialInput', (_message.Message,), {
  'DESCRIPTOR' : _ENVINITIALINPUT,
  '__module__' : 'cogment.api.environment_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.EnvInitialInput)
  })
_sym_db.RegisterMessage(EnvInitialInput)

EnvInitialOutput = _reflection.GeneratedProtocolMessageType('EnvInitialOutput', (_message.Message,), {
  'DESCRIPTOR' : _ENVINITIALOUTPUT,
  '__module__' : 'cogment.api.environment_pb2'
  # @@protoc_insertion_point(class_scope:cogmentAPI.EnvInitialOutput)
  })
_sym_db.RegisterMessage(EnvInitialOutput)



_ENVIRONMENTSP = _descriptor.ServiceDescriptor(
  name='EnvironmentSP',
  full_name='cogmentAPI.EnvironmentSP',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=933,
  serialized_end=1093,
  methods=[
  _descriptor.MethodDescriptor(
    name='RunTrial',
    full_name='cogmentAPI.EnvironmentSP.RunTrial',
    index=0,
    containing_service=None,
    input_type=_ENVRUNTRIALINPUT,
    output_type=_ENVRUNTRIALOUTPUT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Version',
    full_name='cogmentAPI.EnvironmentSP.Version',
    index=1,
    containing_service=None,
    input_type=cogment_dot_api_dot_common__pb2._VERSIONREQUEST,
    output_type=cogment_dot_api_dot_common__pb2._VERSIONINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENVIRONMENTSP)

DESCRIPTOR.services_by_name['EnvironmentSP'] = _ENVIRONMENTSP

# @@protoc_insertion_point(module_scope)
