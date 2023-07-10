from typing import *
import random
import barcode


class BarcodeRandomAlg(object):
    """This class picks barcode algorithm at random:"""

    def __init__(self) -> None:
        pass

    @classmethod
    def pick_random_barcode_format(cls) -> AnyStr:
        alg_list: List = barcode.PROVIDED_BARCODES
        choice_alg = random.choice(alg_list)
        return choice_alg

    # read choice enc alg at random:
    @classmethod
    def pick_random_code_tool(cls) -> AnyStr:
        alg_list: List = ["QR-CODE", "BARCODE"]
        choice_alg = random.choice(alg_list)
        return choice_alg
