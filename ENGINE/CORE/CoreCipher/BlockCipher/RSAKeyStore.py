from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RsaKey
from ENGINE.CORE.CoreFile.FileBulk import FileIO


class DeriveKeyFromPass(object):
    """This class derives RSA Keys from User supplied password:"""

    def __init__(self, store_secret_code: str, key_to_store: RsaKey) -> None:
        self.store_secret_code = store_secret_code
        self.key_to_store = key_to_store

    # Derive Key Params:
    def store_rsa_key(self, key_type: str) -> int:
        encrypted_key: bytes = self.key_to_store.export_key(
            passphrase=self.store_secret_code,
            pkcs=11,  # default:8
            protection="scryptAndAES128-CBC")
        key_store_name: str = "rsa_" + key_type + "_key_store.emma"
        return FileIO.write_file_as_bytes(key_store_name, encrypted_key)

    def retrieve_rsa_key(self, key_store_name: str) -> RsaKey:
        key_store_content: bytes = FileIO.read_file_as_bytes(key_store_name)
        key_obj: RsaKey = RSA.import_key(key_store_content, passphrase=self.store_secret_code)
        return key_obj
