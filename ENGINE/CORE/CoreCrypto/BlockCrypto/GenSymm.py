from typing import *
from Crypto.Random import get_random_bytes
from nacl.utils import *


class Symm(object):
    """This class generates the  secret key and associated Box"""

    def __init__(self) -> None:
        pass

    @staticmethod
    # generate Secret Key:
    def gen_secret() -> bytes:
        key_bytes: bytes = get_random_bytes(256)
        return key_bytes

    @staticmethod
    # generate Secret Key:
    def gen_secret_deterministic() -> bytes:
        init_random = random(size=32)
        # now specify the result you want:
        secret_key: bytes = randombytes_deterministic(256, init_random, encoder=encoding.RawEncoder)
        return secret_key
