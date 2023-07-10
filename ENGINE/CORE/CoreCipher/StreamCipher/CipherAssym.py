from typing import *
import nacl
import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box
from nacl.utils import EncryptedMessage


class AssymEnc(object):
    """This class encrypts and decrypts the real objects:"""

    def __init__(self) -> None:
        pass

    @staticmethod
    # Encrypt Assymetric:
    def encrypt_assym(raw_asset: bytes, assym_box: Box,  nonce: bytes) -> EncryptedMessage:
        enc_asset: EncryptedMessage = assym_box.encrypt(raw_asset, nonce)
        return enc_asset

    @staticmethod
    # Decrypt Assymetric:
    def decrypt_assym(enc_asset: EncryptedMessage, assym_box: Box, nonce: bytes) -> bytes:
        raw_asset: bytes = assym_box.decrypt(enc_asset, nonce)
        return raw_asset
