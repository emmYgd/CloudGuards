from typing import *
import random


class SelectEncAlg(object):
    """This class implements custom byte representation algorithms in .emma files"""

    def __init__(self) -> None:
        pass

    # read choice enc alg at random:
    @staticmethod
    def select_choice_block_enc_alg() -> AnyStr:
        alg_list: List = ["AES_EAX", "AES_GCM", "AES_SIV", "AES_CCM", "AES_OCB"]
        choice_alg = random.choice(alg_list)
        return choice_alg

    @staticmethod
    def select_choice_stream_enc_alg() -> AnyStr:
        alg_list: List = ["XSalsa-Poly", "Chacha-Poly"]
        choice_alg = random.choice(alg_list)
        return choice_alg
