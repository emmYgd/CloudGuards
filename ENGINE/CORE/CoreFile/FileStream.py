from ENGINE.CORE.CoreFile.FileBulk import FileIO

from chunk import Chunk
from typing import *


class FileStr(object, FileIO):
    """This class takes care of the streaming scenerio in files use-case:"""

    def __init__(self) -> None:
        pass

    '''Simple class to read IFF chunks.An IFF chunk (used in formats such as AIFF, TIFF, RMFF 
    (RealMedia File Format)) has the following structure:
        ID (4 bytes)
        size (4 bytes)
        data ...
    The ID is a 4-byte string which identifies the type of chunk.
    The size field (a 32-bit value, encoded using big-endian byte order) 
    gives the size of the whole chunk, including the 8-byte header.'''
    @classmethod
    # Read File As Chunk:
    def read_file_as_chunks(cls, file_name: AnyStr, byte_len_per_chunk: int) -> bytes:
        with open(file_name, "rb+") as readFile:
            chunk = Chunk(readFile)
            while True:
                chunkData: bytes = chunk.read(byte_len_per_chunk)
                if not chunkData:
                    raise EOFError
        return chunkData

    @classmethod
    # Write File As Chunk:
    def read_file_as_list(cls, file_name: AnyStr) -> int:
        pass
