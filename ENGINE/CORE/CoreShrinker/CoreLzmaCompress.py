from typing import *
import lzma
from lzma import FORMAT_XZ
from lzma import CHECK_NONE


class Compressor(object):
    """This class is concerned with compression and decompression:"""

    def __init__(self):
        pass

    # Compress Small Files:
    @staticmethod
    def compress_big_file(raw_data: bytes) -> bytes:
        lzmaObj = lzma.LZMACompressor(format=FORMAT_XZ, check=CHECK_NONE, filters=None)
        comp_data: bytes = lzmaObj.compress(__data=raw_data)
        lzmaObj.flush()  # to clear the internal buffer...
        return comp_data

    # Decompress Small Files:
    @staticmethod
    def decompress_big_file(comp_data: bytes) -> bytes:
        lzmaObj = lzma.LZMADecompressor(format=FORMAT_XZ, memlimit=None, filters=None)
        decomp_data: bytes = lzmaObj.decompress(data=comp_data, max_length=-1)
        return decomp_data

    # Compress Small Files:
    @staticmethod
    def compress_small_file(raw_data: bytes) -> bytes:
        lzma_comp = lzma.compress(data=raw_data, format=FORMAT_XZ, check=CHECK_NONE, filters=None)
        return lzma_comp

    # Decompress Small Files:
    @staticmethod
    def decompress_small_file(comp_data: bytes) -> bytes:
        lzma_decomp = lzma.decompress(data=comp_data, format=FORMAT_XZ, memlimit=None, filters=None)
        return lzma_decomp
