from typing import *
from Crypto.Cipher import AES


class SymmEnc(object):
    """This class encrypts using Block Alg"""

    def __init__(self, cipher_alg: AnyStr = "AES_EAX") -> None:
        self.cipher_alg = cipher_alg
        if self.cipher_alg == "AES_EAX":
            self.enc_mode: int = AES.MODE_GCM
        elif self.cipher_alg == "AES_GCM":
            self.enc_mode: int = AES.MODE_EAX
        elif self.cipher_alg == "AES_SIV":
            self.enc_mode: int = AES.MODE_SIV
        elif self.cipher_alg == "AES_CCM":
            self.enc_mode: int = AES.MODE_CCM
        elif self.cipher_alg == "AES_OCB":
            self.enc_mode: int = AES.MODE_OCB

    # encrypt assets:
    def encrypt_symm(self, secret_key: bytes, raw_data: bytes) -> Dict[Union[str, bytes, Any]]:
        cipher = AES.new(secret_key, self.enc_alg_mode)
        (cipher_data, tag) = cipher.encrypt_and_digest(raw_data)
        return {'enc_data': cipher_data,
                'nonce': cipher.nonce,
                'auth_tag': tag
                }

    # decrypt assets:
    def decrypt_symm(self, secret_key: bytes, enc_data: bytes, nonce: bytes, auth_tag: bytes) -> bytes:
        # let's assume that the key is somehow available again
        cipher = AES.new(secret_key, self.enc_mode, nonce)
        raw_data: bytes = cipher.decrypt_and_verify(enc_data, auth_tag)
        return raw_data
