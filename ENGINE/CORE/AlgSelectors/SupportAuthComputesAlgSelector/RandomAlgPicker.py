from typing import *
import random


class RandomAlg(object):
    """This class picks hash, mac and signature algorithms at random:"""

    def __init__(self) -> None:
        pass

    @staticmethod
    def pick_random_obf_alg() -> AnyStr:
        alg_list: List = ["ROT-13", "CUSTOM"]
        choice_alg = random.choice(alg_list)
        return choice_alg

    @staticmethod
    def pick_hash_or_xof() -> AnyStr:
        alg_list: List = ["HASH", "XOF"]
        choice_alg = random.choice(alg_list)
        return choice_alg

    # read choice enc alg at random:
    @staticmethod
    def pick_random_hash_alg() -> AnyStr:
        alg_list: List = ["SHA-256", "SHA-512", "BLAKE-2b", "SHA-3-256", "SHA-3-512"]
        choice_alg = random.choice(alg_list)
        return choice_alg

    @staticmethod
    def pick_random_xof_alg() -> AnyStr:
        alg_list: List = ["SHAKE-256", "cSHAKE-256", "KANGAROO-TWELVE"]
        choice_alg = random.choice(alg_list)
        return choice_alg

    @staticmethod
    def pick_random_mac_alg() -> AnyStr:
        alg_list: List = ["HMAC", "Poly", "KMAC"]
        choice_alg = random.choice(alg_list)
        return choice_alg

    @staticmethod
    def pick_random_checksum_alg() -> AnyStr:
        alg_list: List = ["NORMAL", "FASTER"]  # [signature algorithms here...]
        choice_alg = random.choice(alg_list)
        return choice_alg
