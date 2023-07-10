'''Signature algorithm here: Will use the PyNacl framework for more speed...'''
from types import ModuleType
from typing import *
from typing import Union

from nacl.exceptions import BadSignatureError
from nacl.signing import SigningKey, VerifyKey
from nacl.signing import SignedMessage
from nacl.encoding import Base64Encoder


class Signature(object):
    """Computes File Checksum"""

    def __init__(self):
        pass

    @staticmethod
    def compute_signature(data_bytes: bytes) -> Dict:
        signing_key: SigningKey = SigningKey.generate()
        signed_message: SignedMessage = signing_key.sign(data_bytes, encoder=Base64Encoder)

        # obtain verification key from signing key:
        verify_key: VerifyKey = signing_key.verify_key
        # serialize:
        verify_key_serialized: bytes = verify_key.encode(encoder=Base64Encoder)
        return {
            "signed_message": signed_message,
            "verify_key": verify_key_serialized
        }

    @staticmethod
    def verify_signature(cls, signature_params: Dict[str:Union[ModuleType, bytes]]) -> bool:
        verify_key_serialized: bytes = signature_params["verify_key"]
        # Deserialize:
        verify_key: VerifyKey = VerifyKey(verify_key_serialized)
        # Sign:
        signed_message: SignedMessage = signature_params["signed_message"]
        try:
            verify_key.verify(signed_message, encoder=Base64Encoder)
            return True
        except Union[BadSignatureError, Exception]:
            return False


