from typing import *

from Crypto.Cipher import ChaCha20_Poly1305
from nacl.public import Box
from nacl.utils import EncryptedMessage


class SymmEnc(object):
    """This class encrypts and decrypts the real objects:"""

    def __init__(self,
                 secret_key: Optional[bytes],
                 cipher_alg: AnyStr = "XSalsa-Poly",
                 sym_box: Optional[Box] = None,
                 nonce: Optional[bytes] = None
                 ) -> None:
        self.sym_box = sym_box
        self.secret_key = secret_key
        self.nonce = nonce
        self.cipher_alg = cipher_alg

    def encrypt(self, raw_data: bytes) -> Union[EncryptedMessage, Dict]:
        global enc_data
        if self.cipher_alg == "XSalsa-Poly":
            enc_data: bytes = self.encrypt_symm_salsa(raw_data)
        elif self.cipher_alg == "Chacha-Poly":
            # call Chacha alg:
            enc_data: Dict = self.encrypt_symm_chacha(raw_data)
        return enc_data

    def decrypt(self, enc_data: EncryptedMessage, auth_tag: Optional[bytes]) -> bytes:
        global raw_data
        if self.cipher_alg == "XSalsa-Poly":
            raw_data: bytes = self.decrypt_symm_salsa(enc_data)
        elif self.cipher_alg == "Chacha-Poly":
            # call Chacha alg:
            raw_data: bytes = self.decrypt_symm_chacha(enc_data, auth_tag)
        return enc_data

    def encrypt_symm_chacha(self, raw_asset: bytes) -> Dict:
        cipher = ChaCha20_Poly1305.new(self.secret_key, self.nonce)
        (cipher_asset, tag) = cipher.encrypt_and_digest(raw_asset)
        return {
            'enc_data': cipher_asset,
            'nonce': cipher.nonce,
            'auth_tag': tag
        }

    def decrypt_symm_chacha(self, enc_asset: bytes, auth_tag: bytes) -> bytes:
        # let's assume that the key is somehow available again
        cipher = ChaCha20_Poly1305.new(self.secret_key, self.nonce)
        raw_asset: bytes = cipher.decrypt_and_verify(enc_asset, auth_tag)
        return raw_asset

    # Encrypt Assymetric Salsa:
    def encrypt_symm_salsa(self, raw_asset: bytes) -> EncryptedMessage:
        cipher_asset: EncryptedMessage = self.sym_box.encrypt(raw_asset, self.nonce)
        return cipher_asset

    # Decrypt Assymetric:
    def decrypt_symm_salsa(self, enc_asset: EncryptedMessage) -> bytes:
        raw_asset: bytes = self.sym_box.decrypt(enc_asset)
        return raw_asset
