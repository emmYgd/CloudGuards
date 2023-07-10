from typing import *
import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box


class Assym(object):
    """This class generates the elliptic assymetric public key, private Key and associated Box"""

    def __init__(self) -> None:
        pass

    @staticmethod
    # generate Private Key:
    def gen_private() -> PrivateKey:
        privateKey: PrivateKey = PrivateKey.generate()
        return privateKey

    @staticmethod
    # generate Public Key:
    def gen_public(private_key: PrivateKey) -> PublicKey:
        publicKey: PublicKey = private_key.public_key
        return publicKey

    @staticmethod
    def gen_assym_box(private_key: PrivateKey, public_key: PublicKey) -> Box:
        # generate safe encryption Box:
        safe_assym_box: Box = Box(private_key, public_key)
        return safe_assym_box

    @staticmethod
    def gen_asymm_nonce(safe_assym_box: Box) -> bytes:
        preferred_nonce_size: int = safe_assym_box.NONCE_SIZE
        nonce: bytes = nacl.utils.random(preferred_nonce_size)
        return nonce
