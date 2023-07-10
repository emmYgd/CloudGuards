from typing import *
import codecs


class Coding(object):
    """This class encrypts and decrypts the real objects:"""

    def __init__(self) -> None:
        pass

    @classmethod
    # Encode:
    def encode_utf(cls, raw_asset: str) -> bytes:
        encoded_raw_asset: bytes = codecs.encode(raw_asset, 'utf-8')
        return encoded_raw_asset

    @classmethod
    # Decode:
    def decode_utf(cls, encoded_asset: bytes) -> AnyStr:
        decoded_raw_asset: AnyStr = codecs.decode(encoded_asset, 'utf-8')
        return decoded_raw_asset

    @classmethod
    # Encode base-64
    def encode_base_64(cls, raw_asset: str) -> bytes:
        encoded_raw_asset: bytes = codecs.encode(raw_asset, 'base-64')
        return encoded_raw_asset

    @classmethod
    # Decode base-64:
    def decode_base_64(cls, encoded_asset: bytes) -> AnyStr:
        decoded_raw_asset: AnyStr = codecs.decode(encoded_asset, 'base-64')
        return decoded_raw_asset

    @classmethod
    # Encode base-64
    def encode_hex(cls, raw_asset: str) -> bytes:
        encoded_raw_asset: bytes = codecs.encode(raw_asset, 'hex')
        return encoded_raw_asset

    @classmethod
    # Decode base-64:
    def decode_hex(cls, encoded_asset: bytes) -> AnyStr:
        decoded_raw_asset: AnyStr = codecs.decode(encoded_asset, 'hex')
        return decoded_raw_asset


