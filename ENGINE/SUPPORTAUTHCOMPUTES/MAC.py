from random import random
from types import ModuleType
from typing import *

import nacl
import nacl.secret
import nacl.utils

from Crypto.Cipher import AES, ChaCha20
from Crypto.Hash import HMAC, SHA256, SHA512, BLAKE2b, SHA3_256, SHA3_512
from Crypto.Hash import Poly1305
from Crypto.Hash import KMAC256

from ENGINE.CORE.AlgSelectors.SupportAuthComputesAlgSelector.RandomAlgPicker import RandomAlg


class MAC(object):
    '''Random MAC generated for data'''

    def __init__(self) -> None:
        pass

    @staticmethod
    def verify_mac(cls, mac_tag: bytes, mac_key: bytes, data: bytes, dig_mod: str) -> bool:
        mac_obj: HMAC = HMAC.new(key=mac_key, msg=data, digestmod=dig_mod)
        try:
            mac_obj.verify(mac_tag)
            return True
        except Union[ValueError, Exception]:
            return False

    @staticmethod
    def gen_mac_hmac(mac_key: bytes, data: bytes, dig_mod: str) -> bytes:
        global mac_obj
        if dig_mod == "SHA-256":
            mac_obj: HMAC = HMAC.new(key=mac_key, msg=data, digestmod=SHA256)
        if dig_mod == "SHA-512":
            mac_obj: HMAC = HMAC.new(key=mac_key, msg=data, digestmod=SHA512)
        if dig_mod == "BLAKE-2b":
            mac_obj: HMAC = HMAC.new(key=mac_key, msg=data, digestmod=BLAKE2b)
        if dig_mod == "SHA-3-256":
            mac_obj: HMAC = HMAC.new(key=mac_key, msg=data, digestmod=SHA3_256)
        if dig_mod == "SHA-3-512":
            mac_obj: HMAC = HMAC.new(key=mac_key, msg=data, digestmod=SHA3_512)
        return mac_obj.digest()

    @staticmethod
    # cipher algorithm can only be Crypto.AES and Crypto.ChaCha
    def gen_mac_poly(data: bytes, mac_key: bytes) -> bytes:

        global mac_obj

        cipher_alg: List = ["AES", "CHACHA"]
        choice_alg = random.choice(cipher_alg)
        preferred_nonce_size: int = nacl.secret.SecretBox.NONCE_SIZE
        nonce: bytes = nacl.utils.random(preferred_nonce_size)
        if choice_alg == "AES":
            mac_obj: Poly1305 = Poly1305.new(key=mac_key, cipher=AES, nonce=nonce, data=data)
        if choice_alg == "CHACHA":
            mac_obj: Poly1305 = Poly1305.new(key=mac_key, cipher=ChaCha20, nonce=nonce, data=data)

        return mac_obj.digest()

    @staticmethod
    def gen_mac_kmac(data: bytes, mac_key: bytes) -> bytes:
        mac_obj: KMAC256 = KMAC256.new(key=mac_key, data=data, mac_len=20)
        return mac_obj.digest()
