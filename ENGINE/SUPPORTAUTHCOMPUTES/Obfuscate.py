from typing import *
import codecs


class Obfuscate(object):
    """This class obfuscates strings passed into it using the ROT-13 Algorithm:"""

    def __init__(self, rotate_alg: Optional[str] = None) -> None:
        self.rotate_alg = rotate_alg

    # convert bytes to utf-str
    @staticmethod
    def bytes_to_str(in_bytes: bytes) -> str:
        return str(in_bytes, "utf8")

    # convert utf-str to bytes:
    @staticmethod
    def str_to_bytes(in_str: str) -> bytes:
        return bytes(in_str)

    # read choice obfuscate algorithm at random:
    def rotate(self, byte_str: str) -> AnyStr:
        global obf_str
        if self.rotate_alg is None or self.rotate_alg == "ROT-13":
            obf_str: bytes = self.rotate_built_in(byte_str)
        elif self.rotate_alg == "CUSTOM":
            # obf_str = self.rotate_custom(byte_str)
            pass
        return obf_str

    def reverse(self, obf_str: str) -> str:
        global rev_str
        if self.rotate_alg is None or self.rotate_alg == "ROT-13":
            rev_str = self.reverse_built_in(obf_str)
        elif self.rotate_alg == "CUSTOM":
            # rev_str = self.reverse_custom(obf_str)
            pass

    @staticmethod
    def rotate_built_in(byte_str: str) -> bytes:
        return codecs.encode(byte_str, "rot13")

    @staticmethod
    def reverse_built_in(obf_str: str) -> str:
        return codecs.decode(obf_str, "rot13")

    @staticmethod
    def rotate_custom(byte_str: str):
        # call custom obs algorithm here...
        pass

    @staticmethod
    def reverse_custom(byte_str: str):
        # call custom obs algorithm here...
        pass
