from typing import *
import nacl.utils
from nacl.secret import SecretBox


class Symm(object):
    """This class generates the  secret key and associated Box"""

    def __init__(self) -> None:
        pass

    @staticmethod
    # generate Secret Key:
    def gen_secret() -> bytes:
        key_size_spec: int = nacl.secret.SecretBox.KEY_SIZE
        secret_key: bytes = nacl.utils.random(key_size_spec)
        return secret_key

    @staticmethod
    # generate Nonce:
    def gen_symm_nonce() -> bytes:
        preferred_nonce_size: int = nacl.secret.SecretBox.NONCE_SIZE
        nonce: bytes = nacl.utils.random(preferred_nonce_size)
        return nonce

    @staticmethod
    def gen_symm_box(key: bytes) -> SecretBox:
        # generate safe encryption Box:
        safe_symm_box: SecretBox = nacl.secret.SecretBox(key)
        return safe_symm_box
