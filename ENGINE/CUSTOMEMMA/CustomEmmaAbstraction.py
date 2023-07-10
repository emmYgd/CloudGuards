from typing import *
from collections import *


class EmmaByteAbstraction(object):
    """This class implements custom byte representation algorithms in .emma files"""

    def __init__(self) -> None:
        pass

    # byte to byte Array:
    @staticmethod
    # use tuple to read in values for speed:
    def byte_to_byte_array(file_byte: tuple) -> bytearray:
        file_byte_array: bytearray = bytearray(file_byte)
        return file_byte_array

    # .emma custom algorithm for int file rep
    @staticmethod
    def byte_to_emma_rep_register(file_byte_array: bytearray) -> Deque:

        global each_considered_elem
        byte_array_len: int = len(file_byte_array)  # file_byte_array.__len__()
        # init:
        emma_byte_rep_register: Deque = Deque()
        # map_of_occurrence: Dict = {}
        # current_elem = 0
        times_of_occurrence: int = 0
        pos_of_occurrence: List = []

        # add total byte length in consideration to the register:
        emma_byte_rep_register.append({"total_byte_length": byte_array_len})

        # contains unique elements that will be searched for occurrence:
        all_considered_elems: Set = set(file_byte_array)
        # now, search each element in the considered set above in the file_byte_array:
        for each_considered_elem in all_considered_elems:
            pos_observer_counter = -1  # set position counter as the sublist is looped:
            for each_byte_elem in file_byte_array:
                # step position observer:
                pos_observer_counter += 1
                # get the position of the elem and append to a List:
                if each_considered_elem == each_byte_elem:
                    times_of_occurrence += 1
                    pos_of_occurrence.append(pos_observer_counter)
                else:
                    continue

            # get all observables:
            map_of_occurrence: Dict = {
                "considered_elem": each_considered_elem,
                "pos_of_occurrence": pos_of_occurrence,
                "times_of_occurrence": times_of_occurrence
            }

            # now, add this map to a unique register:
            emma_byte_rep_register.append(map_of_occurrence)

        return emma_byte_rep_register
