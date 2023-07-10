from typing import *
# use PyCryptoDome here:
from binascii import *
from Crypto.Protocol.SecretSharing import Shamir
from Crypto.Random import get_random_bytes


class SharedAccess(object):
    """This class deals with limiting access to a file system to a certain
    number of selected people using the Shamir's secret sharing algorithm

    For instance, One use case is this :
    one may want to grant 16 people the ability to access a system with a pass code,
    based on the condition that at least 3 of them are present at the same time.
    As they join their shares, the pass code is revealed. In that case, n=16 and k=3."""

    # some constants for hexlify:
    SINGLE_SEPERATOR = b"S"
    BYTES_PER_SEPARATION = 2

    def __init__(self, at_least: int, at_most: int, secret_key: Union[bytes, str]):
        self.secretKey = secret_key
        self.at_least = at_least
        self.at_most = at_most

    # Convert from string to bytes:
    def convert_string_to_bytes(self) -> bytes:
        if type(self.secretKey) == str:
            self.secretKey = bytes(self.secretKey)
        return self.secretKey

    # Use Shamir's Key splitting:
    def share_access_secret(self):
        key_shares: List[Tuple[int, bytes]] = Shamir.split(
                                                k=self.at_least,
                                                n=self.at_most,
                                                secret=self.secretKey,
                                                ssss=True)
        # returns a list of key shares that contain:
        # (each_share_index, each_share_secret)
        return key_shares

    @staticmethod
    # to form a list which contains a tuple:
    # each_index, each_secret_share = [each_index_share_tuple for each_index_share_tuple in all_secret_tuples_in_list]
    def combine_access_secret(all_secret_tuples_in_list: List[Tuple[int, bytes]]) -> bytes:
        secretkey: bytes = Shamir.combine(all_secret_tuples_in_list, ssss=True)
        return secretkey

    @staticmethod
    def hexlify(cls, raw_secret: bytes) -> bytes:
        hexed_secret: bytes = hexlify(raw_secret)
        return hexed_secret

    @classmethod
    def unhexlify(cls, hexed_secret: bytes) -> bytes:
        raw_secret: bytes = unhexlify(hexed_secret)
        return raw_secret
