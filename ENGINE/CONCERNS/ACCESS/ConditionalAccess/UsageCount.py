from typing import *


class Count(object):
    """Access based on usage count"""

    def __init__(self):
        pass

    # access based on number of times opened:
    @classmethod
    def compare_usage_count(cls, current_count: int, max_count: int) -> Union[bool, PermissionError]:
        if current_count <= max_count:
            return True
        else:
            raise PermissionError
