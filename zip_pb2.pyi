from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ZipInput(_message.Message):
    __slots__ = ["radius", "zipCode"]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    ZIPCODE_FIELD_NUMBER: _ClassVar[int]
    radius: int
    zipCode: str
    def __init__(self, zipCode: _Optional[str] = ..., radius: _Optional[int] = ...) -> None: ...

class ZipOutput(_message.Message):
    __slots__ = ["output"]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    output: str
    def __init__(self, output: _Optional[str] = ...) -> None: ...
