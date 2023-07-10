from typing import *
import os


class FileIO(object):
    """This class his class takes care of the batch File IO:"""

    def __init__(self) -> None:
        pass

    @classmethod
    # Read File:
    def read_file_as_bytes(cls, file_name: AnyStr) -> bytes:
        with open(file_name, "rb+") as readFile:
            return readFile.read()

    @classmethod
    # Write File As Bytes:
    def write_file_as_bytes(cls, file_name: AnyStr, byte_chunk: bytes) -> int:
        with open(file_name, "wb+") as writeFile:
            return writeFile.write(byte_chunk)

    @classmethod
    # Write File As Chunk:
    def write_file_as_chunks(cls, file_name: AnyStr, byte_chunk: bytes) -> int:
        pass

    @classmethod
    # Write File As String:
    def read_file_as_string(cls, file_name: AnyStr) -> AnyStr:
        with open(file_name, "r") as readFile:
            return readFile.read()

    @classmethod
    # Write File As String:
    def write_file_as_string(cls, file_name: AnyStr, char_string: AnyStr) -> int:
        with open(file_name, "w") as writeFile:
            return writeFile.write(char_string)

    @classmethod
    # delete file:
    def delete_file(cls, file_name: AnyStr) -> bool:
        os.remove(file_name)
        return True
