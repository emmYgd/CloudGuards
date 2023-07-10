from typing import *
from collections import *


class EmmaByteReverseAbstraction(object):
    """This class implements custom byte representation algorithms in .emma files"""

    def __init__(self) -> None:
        pass

    # byte to byte Array:
    @staticmethod
    # use tuple to read in values for speed:
    def byte_array_to_byte(file_byte_array: bytearray) -> bytes:
        file_byte_array: bytes = bytes(file_byte_array)
        return file_byte_array

    # reverse alg for .emma custom algorithm for rep
    @staticmethod
    def emma_rep_register_to_byte(emma_rep_register: Deque) -> bytearray:
        # init:
        # original_data_byte_array = bytearray()
        global original_data_byte_array

        # start by looping through the register:
        for each_map in emma_rep_register:
            # get the total array length:
            if each_map == emma_rep_register[0]:
                total_byte_length = emma_rep_register[0]["total_byte_length"]
                # now re-construct the arrays and init with 0s: i.e
                original_data_byte_array = bytearray(0 for i in range(total_byte_length))
            else:
                # start deconstructing map of each considered elem:
                for each_elem_info in each_map:
                    each_considered_elem = each_map["considered_elem"]
                    pos_of_occurrence: List = each_map["pos_of_occurrence"]
                    times_of_occurrence: int = each_map["times_of_occurrence"]

                    # loop through the position of occurrence List:
                    for each_pos in pos_of_occurrence:
                        # begin changing the init zero values in the original_data_byte_array by
                        # inserting each considered elem:
                        original_data_byte_array[each_pos] = each_considered_elem

        return original_data_byte_array



