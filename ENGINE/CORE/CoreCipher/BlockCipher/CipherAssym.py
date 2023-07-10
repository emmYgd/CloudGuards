from typing import *
from typing import Union

from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RsaKey
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
from Crypto.Cipher.PKCS1_OAEP import PKCS1OAEP_Cipher
from Crypto.Cipher.PKCS1_v1_5 import PKCS115_Cipher


class AssymEnc(object):
    """This class encrypts using RSA Alg"""

    def __init__(self) -> None:
        pass

    @staticmethod
    # encrypt assets:
    def encrypt_assym(rsa_enc_scheme: str, raw_asset: bytes, public_key: Union[RsaKey, bytes]) -> Dict:

        global recipient_key, cipher_obj

        if type(public_key) == bytes:
            recipient_key: RsaKey = RSA.import_key(public_key)

        if rsa_enc_scheme == "PKCS1_OAEP":
            # Encrypt the asset with the public RSA key(OAEP)
            cipher_obj = PKCS1_OAEP.new(recipient_key)
        if rsa_enc_scheme == "PKCS1_v1_5":
            # Encrypt the asset with the public RSA key(v1_5)
            cipher_obj = PKCS1_v1_5.new(recipient_key)

        enc_asset: bytes = cipher_obj.encrypt(raw_asset)

        return {
            "rsa_enc_scheme": rsa_enc_scheme,
            "enc_asset": enc_asset
        }

    @staticmethod
    # decrypt assets:
    def decrypt_assym(enc_alg_scheme: str, enc_asset: bytes, private_key: Union[RsaKey, bytes]) -> bytes:
        global recipient_key, cipher_obj

        if type(private_key) == bytes:
            recipient_key: RsaKey = RSA.import_key(private_key)

        if enc_alg_scheme == "PKCS1_OAEP":
            # Encrypt the asset with the public RSA key(OAEP)
            cipher_obj = PKCS1_OAEP.new(private_key)
        if enc_alg_scheme == "PKCS1_v1_5":
            # Encrypt the asset with the public RSA key(v1_5)
            cipher_obj = PKCS1_v1_5.new(private_key)

        raw_asset: bytes = cipher_obj.decrypt(enc_asset)

        return raw_asset
