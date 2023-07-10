from typing import *
import uuid


class UUID(object):
    """Compute uuid:"""

    def __init__(self):
        pass

    @classmethod
    def uuid_safe_random(cls) -> uuid:
        return uuid.uuid4()

    @classmethod
    def uuid_from_bytes(cls, input_byte: bytes) -> uuid:
        return uuid.UUID(bytes=input_byte)

