from typing import *
from datetime import datetime


class Activate(object):
    """Access based on activation datetime"""

    def __init__(self):
        pass

    # access based on number of times opened:
    @classmethod
    def activate_asset_after(cls,
                             current_date_time: datetime,
                             activation_date_time: datetime
                             ) -> Union[bool, PermissionError]:
        if current_date_time >= activation_date_time:
            return True
        else:
            raise PermissionError
