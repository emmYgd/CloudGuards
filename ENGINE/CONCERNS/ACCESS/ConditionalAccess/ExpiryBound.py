from typing import *
from datetime import datetime


class Validate(object):
    """Access based on activation datetime"""

    def __init__(self):
        pass

    # access based on number of times opened:
    @classmethod
    def validate_asset(cls,
                       current_date_time: datetime,
                       expiry_date_time: datetime
                       ) -> Union[bool, PermissionError]:
        if current_date_time <= expiry_date_time:
            return True
        else:
            raise PermissionError
