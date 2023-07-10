from typing import *
from Crypto.Hash import SHAKE256
from Crypto.Hash import cSHAKE256
from Crypto.Hash import KangarooTwelve


class XOF(object):
    '''A XOF is similar to a conventional cryptographic hash: I
    t is a one-way function that maps a piece of data of arbitrary size to a random-like output.'''

    def __init__(self, alg_name: str) -> None:
        self.alg_name = alg_name

    def gen_xof(self, input_data: bytes) -> bytes:
        if self.alg_name == "SHAKE-256":
            return self.gen_xof_shake_256(input_data)
        elif self.alg_name == "cSHAKE-256":
            return self.gen_xof_cshake_256(input_data)
        elif self.alg_name == "KANGAROO-TWELVE":
            return self.gen_xof_kangaroo_twelve(input_data)

    @classmethod
    def gen_xof_shake_256(cls, input_data: bytes) -> bytes:
        hash_obj: SHAKE256 = SHAKE256.new(data=input_data)
        return hash_obj.read(25)

    @classmethod
    def gen_xof_cshake_256(cls, input_data: bytes) -> bytes:
        hash_obj: cSHAKE256 = cSHAKE256.new(data=input_data)
        return hash_obj.read(50)

    @classmethod
    def gen_xof_kangaroo_twelve(cls, input_data: bytes) -> bytes:
        hash_obj: KangarooTwelve = KangarooTwelve.new(data=input_data)
        return hash_obj.read(50)
