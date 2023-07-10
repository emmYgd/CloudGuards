import ipaddress
from typing import *


class GeoValidCountry(object):
    """Access based on country, probably will have to work with a python geo-ip library
    # Get Device IPaddress
    # Get Location from IPaddress
    # Also will have to work with a database"""

    def __init__(self):
        pass

    def all_country_list(self):
        # all_country_list: List = []
        # not proper here, modelled after a database model
        pass

    def allowed_country_list(self):
        # allowed_country_list: List = []
        # not proper here, modelled after a database model
        pass

    # deduce current location from IP:
    @classmethod
    def deduce_current_location(cls, current_user_ip: ipaddress) -> AnyStr:
        # deduce user location from user_ip
        pass

    @classmethod
    def compare_location(cls, current_user_location: str) -> Union[True, PermissionError]:
        # if this current location deduced is equal to
        # one of the allowed locations to open this file: then open..
        # .else: raise Error
        pass
