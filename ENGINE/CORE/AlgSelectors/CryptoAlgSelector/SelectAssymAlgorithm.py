from typing import *
import random


class SelectEncAlg(object):
    """This class implements custom byte representation algorithms in .emma files"""

    def __init__(self) -> None:
        pass

    # read choice enc alg at random:
    @staticmethod
    def select_choice_enc_alg() -> AnyStr:
        alg_list: List = ["EC", "RSA"]
        choice_alg = random.choice(alg_list)
        return choice_alg

    # if rsa is selected above, select one of the two RSA alg:
    @staticmethod
    def select_choice_rsa() -> AnyStr:
        alg_list = ["PKCS1_v1_5", "PKCS1_OAEP"]
        choice_alg = random.choice(alg_list)
        return choice_alg

