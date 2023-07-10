import random
from typing import *
from typing import Dict, Union, Any

from nacl import pwhash, secret, utils


class DeriveKeyFromPass(object):
    """This class derives Key from User supplied password:"""

    # expecting argon2id, scrypt, argon2i for the algorithm choice string:
    def __init__(self, alg_choice: str) -> None:
        self.alg_choice = alg_choice
        pass

    # Derive Key Params:
    def derive_kdf_params(self) -> dict[str, Union[bytes, int, Any]]:
        if self.alg_choice == 'argon2id':
            kdf: Any = pwhash.argon2id.kdf
            salt: bytes = utils.random(pwhash.argon2id.SALTBYTES)
            ops: int = pwhash.argon2id.OPSLIMIT_SENSITIVE
            mem: int = pwhash.argon2id.MEMLIMIT_SENSITIVE
        elif self.alg_choice == 'scrypt':
            kdf: Any = pwhash.scrypt.kdf
            salt: bytes = utils.random(pwhash.scrypt.SALTBYTES)
            ops: int = pwhash.scrypt.OPSLIMIT_SENSITIVE
            mem: int = pwhash.scrypt.MEMLIMIT_SENSITIVE
        else:
            kdf: Any = pwhash.argon2i.kdf
            salt: bytes = utils.random(pwhash.argon2id.SALTBYTES)
            ops: int = pwhash.argon2id.OPSLIMIT_SENSITIVE
            mem: int = pwhash.argon2id.MEMLIMIT_SENSITIVE

        return {
            'kdf': kdf,
            'salt': salt,
            'ops': ops,
            'mem': mem
        }

    @classmethod
    def use_kdf_params(cls,
                       user_pass: str,
                       kdf: Any,
                       salt: bytes,
                       ops: int,
                       mem: int) -> bytes:
        secret_key: bytes = kdf(secret.SecretBox.KEY_SIZE,
                                user_pass,
                                salt,
                                opslimit=ops,
                                memlimit=mem)
        return secret_key

