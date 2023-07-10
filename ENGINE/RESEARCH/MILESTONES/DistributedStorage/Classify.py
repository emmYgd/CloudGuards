'''Dot emma file classification before storage and retrieval'''
import uuid
from typing import *


class Classify(object):

    def __init__(self) -> None:
        pass

    @staticmethod
    def classify_through_uuid(from_storage_map: Dict, select_uuid: uuid):
        if from_storage_map["uuid"] == select_uuid:
            # return from_storage_map
            pass
        pass

    @staticmethod
    def add_returned_map_to_registered_list(from_storage_map: Dict):
        register_list = [].append(from_storage_map)
        # return register_list
        pass




