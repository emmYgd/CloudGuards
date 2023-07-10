from typing import *
from Crypto.Hash import SHA256
from Crypto.Hash import SHA512
from Crypto.Hash import BLAKE2b
from Crypto.Hash import SHA3_256
from Crypto.Hash import SHA3_512


class Hash(object):
    """Compute hashes using various algorithms:"""

    def __init__(self, alg_name: str) -> None:
        self.alg_name = alg_name

    def gen_hash(self, input_data: bytes) -> bytes:
        if self.alg_name == "SHA-256":
            return self.gen_hash_sha_256(input_data)
        elif self.alg_name == "SHA-512":
            return self.gen_hash_sha_512(input_data)
        elif self.alg_name == "BLAKE-2b":
            return self.gen_hash_blake_2b(input_data)
        elif self.alg_name == "SHA-3-256":
            return self.gen_hash_sha_3_256(input_data)
        elif self.alg_name == "SHA-3-512":
            return self.gen_hash_sha_3_512(input_data)

    @classmethod
    def gen_hash_sha_256(cls, input_data: bytes) -> bytes:
        hash_obj: SHA256 = SHA256.new(data=input_data)
        return hash_obj.digest()

    @classmethod
    def gen_hash_sha_512(cls, input_data: bytes) -> bytes:
        hash_obj: SHA512 = SHA512.new(data=input_data)
        return hash_obj.digest()

    @classmethod
    def gen_hash_blake_2b(cls, input_data: bytes) -> bytes:
        hash_obj: BLAKE2b = BLAKE2b.new(data=input_data)
        return hash_obj.digest()

    @classmethod
    def gen_hash_sha_3_256(cls, input_data: bytes) -> bytes:
        hash_obj: SHA3_256 = SHA3_256.new(__data=input_data)
        return hash_obj.digest()

    @classmethod
    def gen_hash_sha_3_512(cls, input_data: bytes) -> bytes:
        hash_obj: SHA3_512 = SHA3_512.new(__data=input_data)
        return hash_obj.digest()
