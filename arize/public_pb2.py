# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: public.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='public.proto',
  package='public',
  syntax='proto3',
  serialized_options=b'\n\022com.arize.protocolZ9github.com/Arize-ai/arize/go/pkg/receiver/protocol/public',
  serialized_pb=b'\n\x0cpublic.proto\x12\x06public\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9f\x01\n\nBulkRecord\x12\x18\n\x10organization_key\x18\x01 \x01(\t\x12\x10\n\x08model_id\x18\x02 \x01(\t\x12\x15\n\rmodel_version\x18\x03 \x01(\t\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1f\n\x07records\x18\x05 \x03(\x0b\x32\x0e.public.Record\"\xaf\x01\n\x06Record\x12\x18\n\x10organization_key\x18\x01 \x01(\t\x12\x10\n\x08model_id\x18\x02 \x01(\t\x12\x15\n\rprediction_id\x18\x03 \x01(\t\x12(\n\nprediction\x18\x04 \x01(\x0b\x32\x12.public.PredictionH\x00\x12 \n\x06\x61\x63tual\x18\x05 \x01(\x0b\x32\x0e.public.ActualH\x00\x42\x16\n\x14prediction_or_actual\"K\n\x05Label\x12\x10\n\x06\x62inary\x18\x01 \x01(\x08H\x00\x12\x15\n\x0b\x63\x61tegorical\x18\x02 \x01(\tH\x00\x12\x11\n\x07numeric\x18\x03 \x01(\x01H\x00\x42\x06\n\x04\x64\x61ta\"\xe4\x01\n\nPrediction\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rmodel_version\x18\x02 \x01(\t\x12\x1c\n\x05label\x18\x03 \x01(\x0b\x32\r.public.Label\x12\x32\n\x08\x66\x65\x61tures\x18\x04 \x03(\x0b\x32 .public.Prediction.FeaturesEntry\x1a>\n\rFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.public.Value:\x02\x38\x01\"m\n\x05Value\x12\x10\n\x06string\x18\x01 \x01(\tH\x00\x12\r\n\x03int\x18\x02 \x01(\x03H\x00\x12\x10\n\x06\x64ouble\x18\x03 \x01(\x01H\x00\x12)\n\x0bmulti_value\x18\x04 \x01(\x0b\x32\x12.public.MultiValueH\x00\x42\x06\n\x04\x64\x61ta\"\x1c\n\nMultiValue\x12\x0e\n\x06values\x18\x01 \x03(\t\"U\n\x06\x41\x63tual\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x05label\x18\x02 \x01(\x0b\x32\r.public.LabelBO\n\x12\x63om.arize.protocolZ9github.com/Arize-ai/arize/go/pkg/receiver/protocol/publicb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_BULKRECORD = _descriptor.Descriptor(
  name='BulkRecord',
  full_name='public.BulkRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_key', full_name='public.BulkRecord.organization_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_id', full_name='public.BulkRecord.model_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_version', full_name='public.BulkRecord.model_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='public.BulkRecord.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='public.BulkRecord.records', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=58,
  serialized_end=217,
)


_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='public.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_key', full_name='public.Record.organization_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_id', full_name='public.Record.model_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prediction_id', full_name='public.Record.prediction_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prediction', full_name='public.Record.prediction', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actual', full_name='public.Record.actual', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='prediction_or_actual', full_name='public.Record.prediction_or_actual',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=220,
  serialized_end=395,
)


_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='public.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binary', full_name='public.Label.binary', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='categorical', full_name='public.Label.categorical', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numeric', full_name='public.Label.numeric', index=2,
      number=3, type=1, cpp_type=5, label=1,
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
    _descriptor.OneofDescriptor(
      name='data', full_name='public.Label.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=397,
  serialized_end=472,
)


_PREDICTION_FEATURESENTRY = _descriptor.Descriptor(
  name='FeaturesEntry',
  full_name='public.Prediction.FeaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='public.Prediction.FeaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='public.Prediction.FeaturesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=641,
  serialized_end=703,
)

_PREDICTION = _descriptor.Descriptor(
  name='Prediction',
  full_name='public.Prediction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='public.Prediction.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_version', full_name='public.Prediction.model_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='public.Prediction.label', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='public.Prediction.features', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTION_FEATURESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=475,
  serialized_end=703,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='public.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='string', full_name='public.Value.string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int', full_name='public.Value.int', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double', full_name='public.Value.double', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multi_value', full_name='public.Value.multi_value', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='data', full_name='public.Value.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=705,
  serialized_end=814,
)


_MULTIVALUE = _descriptor.Descriptor(
  name='MultiValue',
  full_name='public.MultiValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='public.MultiValue.values', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=816,
  serialized_end=844,
)


_ACTUAL = _descriptor.Descriptor(
  name='Actual',
  full_name='public.Actual',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='public.Actual.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='public.Actual.label', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=846,
  serialized_end=931,
)

_BULKRECORD.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BULKRECORD.fields_by_name['records'].message_type = _RECORD
_RECORD.fields_by_name['prediction'].message_type = _PREDICTION
_RECORD.fields_by_name['actual'].message_type = _ACTUAL
_RECORD.oneofs_by_name['prediction_or_actual'].fields.append(
  _RECORD.fields_by_name['prediction'])
_RECORD.fields_by_name['prediction'].containing_oneof = _RECORD.oneofs_by_name['prediction_or_actual']
_RECORD.oneofs_by_name['prediction_or_actual'].fields.append(
  _RECORD.fields_by_name['actual'])
_RECORD.fields_by_name['actual'].containing_oneof = _RECORD.oneofs_by_name['prediction_or_actual']
_LABEL.oneofs_by_name['data'].fields.append(
  _LABEL.fields_by_name['binary'])
_LABEL.fields_by_name['binary'].containing_oneof = _LABEL.oneofs_by_name['data']
_LABEL.oneofs_by_name['data'].fields.append(
  _LABEL.fields_by_name['categorical'])
_LABEL.fields_by_name['categorical'].containing_oneof = _LABEL.oneofs_by_name['data']
_LABEL.oneofs_by_name['data'].fields.append(
  _LABEL.fields_by_name['numeric'])
_LABEL.fields_by_name['numeric'].containing_oneof = _LABEL.oneofs_by_name['data']
_PREDICTION_FEATURESENTRY.fields_by_name['value'].message_type = _VALUE
_PREDICTION_FEATURESENTRY.containing_type = _PREDICTION
_PREDICTION.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PREDICTION.fields_by_name['label'].message_type = _LABEL
_PREDICTION.fields_by_name['features'].message_type = _PREDICTION_FEATURESENTRY
_VALUE.fields_by_name['multi_value'].message_type = _MULTIVALUE
_VALUE.oneofs_by_name['data'].fields.append(
  _VALUE.fields_by_name['string'])
_VALUE.fields_by_name['string'].containing_oneof = _VALUE.oneofs_by_name['data']
_VALUE.oneofs_by_name['data'].fields.append(
  _VALUE.fields_by_name['int'])
_VALUE.fields_by_name['int'].containing_oneof = _VALUE.oneofs_by_name['data']
_VALUE.oneofs_by_name['data'].fields.append(
  _VALUE.fields_by_name['double'])
_VALUE.fields_by_name['double'].containing_oneof = _VALUE.oneofs_by_name['data']
_VALUE.oneofs_by_name['data'].fields.append(
  _VALUE.fields_by_name['multi_value'])
_VALUE.fields_by_name['multi_value'].containing_oneof = _VALUE.oneofs_by_name['data']
_ACTUAL.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ACTUAL.fields_by_name['label'].message_type = _LABEL
DESCRIPTOR.message_types_by_name['BulkRecord'] = _BULKRECORD
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['Label'] = _LABEL
DESCRIPTOR.message_types_by_name['Prediction'] = _PREDICTION
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['MultiValue'] = _MULTIVALUE
DESCRIPTOR.message_types_by_name['Actual'] = _ACTUAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BulkRecord = _reflection.GeneratedProtocolMessageType('BulkRecord', (_message.Message,), {
  'DESCRIPTOR' : _BULKRECORD,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.BulkRecord)
  })
_sym_db.RegisterMessage(BulkRecord)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), {
  'DESCRIPTOR' : _RECORD,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.Record)
  })
_sym_db.RegisterMessage(Record)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), {
  'DESCRIPTOR' : _LABEL,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.Label)
  })
_sym_db.RegisterMessage(Label)

Prediction = _reflection.GeneratedProtocolMessageType('Prediction', (_message.Message,), {

  'FeaturesEntry' : _reflection.GeneratedProtocolMessageType('FeaturesEntry', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTION_FEATURESENTRY,
    '__module__' : 'public_pb2'
    # @@protoc_insertion_point(class_scope:public.Prediction.FeaturesEntry)
    })
  ,
  'DESCRIPTOR' : _PREDICTION,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.Prediction)
  })
_sym_db.RegisterMessage(Prediction)
_sym_db.RegisterMessage(Prediction.FeaturesEntry)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.Value)
  })
_sym_db.RegisterMessage(Value)

MultiValue = _reflection.GeneratedProtocolMessageType('MultiValue', (_message.Message,), {
  'DESCRIPTOR' : _MULTIVALUE,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.MultiValue)
  })
_sym_db.RegisterMessage(MultiValue)

Actual = _reflection.GeneratedProtocolMessageType('Actual', (_message.Message,), {
  'DESCRIPTOR' : _ACTUAL,
  '__module__' : 'public_pb2'
  # @@protoc_insertion_point(class_scope:public.Actual)
  })
_sym_db.RegisterMessage(Actual)


DESCRIPTOR._options = None
_PREDICTION_FEATURESENTRY._options = None
# @@protoc_insertion_point(module_scope)
