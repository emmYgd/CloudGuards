from typing import *
import bz2


class Compressor(object):
    """This class is concerned with compression and decompression:"""

    def __init__(self):
        pass

    # Compress Small Files:
    @staticmethod
    def compress_big_file(raw_data: bytes) -> bytes:
        bz2Obj = bz2.BZ2Compressor(compresslevel=9)
        comp_data = bz2Obj.compress(__data=raw_data)
        bz2Obj.flush()
        return comp_data

    # Decompress Small Files:
    @staticmethod
    def decompress_big_file(comp_data: bytes) -> bytes:
        bz2Obj = bz2.BZ2Decompressor()
        decomp_data: bytes = bz2Obj.decompress(comp_data, max_length=- 1)
        return decomp_data

    # Compress Small Files:
    @staticmethod
    def compress_small_file(raw_data: bytes) -> bytes:
        bz2_comp = bz2.compress(data=raw_data, compresslevel=9)
        return bz2_comp

    # Decompress Small Files:
    @staticmethod
    def decompress_small_file(comp_data: bytes) -> bytes:
        bz2_decomp = bz2.decompress(data=comp_data)
        return bz2_decomp
