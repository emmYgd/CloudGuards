from typing import *
import random


class SelectEncAlg(object):
    """This class implements custom byte representation algorithms in .emma files"""

    def __init__(self) -> None:
        pass

    # read choice enc alg at random:
    @staticmethod
    def select_choice_shrinker() -> AnyStr:
        alg_list: List = ["ZIP", "LZMA", "BZ2"]
        choice_alg = random.choice(alg_list)
        return choice_alg

