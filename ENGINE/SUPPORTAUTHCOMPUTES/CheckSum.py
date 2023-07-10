from typing import *
import zlib


class CheckSum(object):
    """Computes File Checksum"""

    def __init__(self):
        pass

    @staticmethod
    def compute_checksum(asset: Any) -> int:
        checksum: int = zlib.crc32(asset)
        return checksum

    @staticmethod
    def compute_faster_checksum(asset: Any) -> int:
        checksum: int = zlib.adler32(asset)
        return checksum
