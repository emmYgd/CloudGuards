from typing import *
import uuid
import ipaddress
import zlib


class SingleAccess(object):
    """This class deals with limiting access to a file system to only one person:
    Files that only "you" can access (current user uuid, ip address or browser(with unique fingerprint))"""

    def __init__(self):
        pass

    @classmethod
    def check_uuid(cls, given_uuid: Union[uuid, bytes, str], computed_uuid: Union[uuid, bytes, str]) -> None:
        if given_uuid != computed_uuid:
            raise TypeError

    @classmethod
    def check_fingerprint(cls, given_finger_print: Union[str, bytes], computed_finger_print: Union[str, bytes]) -> None:
        if given_finger_print != computed_finger_print:
            raise TypeError

    @classmethod
    def check_ipaddress(cls, given_ip: Union[ipaddress, bytes, str], computed_ip: Union[ipaddress, str, bytes]) -> None:
        if given_ip != computed_ip:
            raise TypeError

    @classmethod
    def check_checksum(cls, given_checksum: Union[int, str, bytes], computed_checksum: Union[int, str, bytes]) -> None:
        if given_checksum != computed_checksum:
            raise TypeError

    @classmethod
    def check_hash(cls, given_hash: Union[str, bytes], computed_hash: Union[str, bytes]) -> None:
        if given_hash != computed_hash:
            raise TypeError

    @classmethod
    def check_mac(cls, given_mac: Union[str, bytes], computed_mac: Union[str, bytes]) -> None:
        if given_mac != computed_mac:
            raise TypeError

    @classmethod
    def check_timestamp(cls, given_timestamp: Union[str, bytes], computed_timestamp: Union[str, bytes]) -> None:
        if given_timestamp != computed_timestamp:
            raise TypeError



