from random import random
from typing import *
import zlib
from zlib import *


class Compressor(object):
    """This class is concerned with compression and decompression:"""

    def __init__(self, level: int, method: Any, wbits: int, mem_level: int, bufsize: int):
        self.level = level
        self.method = method
        self.wbits = wbits
        self.mem_level = mem_level
        self.bufsize = bufsize

    # Compress Small File:
    def compress_small_file_at_once(self, raw_small_file: bytes) -> bytes:
        comp_small_file: bytes = zlib.compress(__data=raw_small_file, level=self.level)
        return comp_small_file

    # Decompress Small Files:
    def decompress_small_file_at_once(self, comp_small_file: bytes) -> bytes:
        # 100 is not compulsory, just an initial performance tuning:
        raw_small_file: bytes = zlib.decompress(__data=comp_small_file, wbits=self.wbits, bufsize=self.bufsize)
        return raw_small_file

    # Compress Big File: comp_file_obj: Any = zlib.compressobj(level=-1, method=DEFLATED, wbits=0, memLevel=10,
    # strategy=selected_str, zdict=dict_value_bytes)
    def big_file_compress_object(self, dict_value_bytes: Optional[bytes, None] = None) -> Any:
        # put all compression strategies in a list:
        comp_str: List = [Z_DEFAULT_STRATEGY, Z_FILTERED, Z_HUFFMAN_ONLY, Z_RLE, Z_FIXED]
        # select any random choice from the list:
        selected_str = random.choice(comp_str)  # check this out later: random object choice method:
        comp_file_obj: Any = zlib.compressobj(self.level, self.method, self.wbits, self.mem_level, selected_str,
                                              dict_value_bytes)
        return comp_file_obj

    @classmethod
    def compress_big_files(cls, compress_object: Any, raw_big_file: bytes) -> bytes:
        # put all flush strategies in a list:
        flush_str: List = [Z_NO_FLUSH, Z_PARTIAL_FLUSH, Z_SYNC_FLUSH, Z_FULL_FLUSH, Z_BLOCK]
        # select any random choice from the list:
        selected_flush_str = random.choice(flush_str)
        # now,use the compression object:
        comp_big_file: bytes = compress_object.compress(raw_big_file)
        # flush after compression:
        compress_object.flush(selected_flush_str)
        while True:
            compress_object.flush(Z_FINISH)
            break
        return comp_big_file

    # DeCompress Big File: comp_file_obj: Any = zlib.compressobj(level=-1, method=DEFLATED, wbits=0, memLevel=10,
    # strategy=selected_str, zdict=dict_value_bytes)
    def big_file_decompress_object(self, dict_value_bytes: Optional[bytes, None] = None) -> Any:
        decomp_file_obj: Any = zlib.decompressobj(wbits=self.wbits, zdict=dict_value_bytes)
        return decomp_file_obj

    @classmethod
    # might set init buffer length to 100
    def decompress_big_files(cls, decomp_object: Any, comp_big_file: bytes,
                             init_buffer_length: Optional[int] = None) -> bytes:
        # put all flush strategies in a list:
        flush_str: List = [Z_NO_FLUSH, Z_PARTIAL_FLUSH, Z_SYNC_FLUSH, Z_FULL_FLUSH, Z_BLOCK]
        # select any random choice from the list:
        selected_flush_str = random.choice(flush_str)
        # now,use the compression object:
        decomp_big_file: bytes = decomp_object.decompress(data=comp_big_file, max_length=0)
        # flush after decompression:
        while True:
            decomp_object.flush(init_buffer_length)
            break
        return decomp_big_file
