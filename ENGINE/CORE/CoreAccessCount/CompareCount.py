from datetime import *


class CompareCount(object):
    '''This class handles count comparism'''

    # Cloud type: Amazon_S3, Google_Cloud, Microsoft_Azure
    def __init__(self) -> None:
        pass

    # get current system time:
    @classmethod
    def compare_for_equality(cls, access_count: int, max_count: int) -> bool:
        if access_count == max_count:
            return True
