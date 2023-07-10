from datetime import *

class CompareDateTime(object):
    '''This class handles date time comparism'''

    # Cloud type: Amazon_S3, Google_Cloud, Microsoft_Azure
    def __init__(self) -> None:
        pass

    # get current system time:
    @classmethod
    def get_current_date_time(cls) -> datetime:
        today_date_time: datetime = datetime.today()
        return today_date_time

    # compare for equality:
    @classmethod
    def compare_for_equality(cls, supplied_date_time: datetime, current_date_time: datetime) -> bool:
        if supplied_date_time == current_date_time:
            return True

    @classmethod
    def compare_for_inequality(cls, supplied_date_time: datetime, current_date_time: datetime) -> bool:
        if supplied_date_time < current_date_time:
            return True
