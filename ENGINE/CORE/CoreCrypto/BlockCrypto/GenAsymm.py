"""As this would have been an RSA encryption, I chose to limit the usage for the sake of speed"""
from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RsaKey


class Assym(object):
    """This class encrypts using Block Alg"""

    def __init__(self) -> None:
        pass

    @staticmethod
    # Generate RSA key:
    def gen_asymm_keypair() -> RsaKey:
        key_pair_obj: RsaKey = RSA.generate(3072)
        return key_pair_obj

    @staticmethod
    def gen_assym_private(key_pair_obj: RsaKey) -> bytes:
        private_key: bytes = key_pair_obj.export_key()
        return private_key

    @staticmethod
    def gen_assym_public(key_pair_obj: RsaKey) -> bytes:
        public_key: bytes = key_pair_obj.public_key().export_key()
        return public_key
