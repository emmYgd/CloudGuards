from typing import *

'''ALGORITHM:
            Get the length of the bytes
            Divide it by the number of segments you want
            If it produced a decimal, round it up to a whole number digit
            Read in encrypted bytes whose number is determined by the result obtained above(labelled as each segment)
            Decrypt based on the number of preferred segments access specified before by the vendor
            (e.g. the user must not have access to more than x segments)'''


class PartitionBytes(object):
    '''This class handles byte partisioning'''

    def __init__(self, file_bytes: bytes, file_byte_length: int, vendor_segment_pref) -> None:
        self.file_bytes = file_bytes
        self.file_byte_length = file_byte_length
        self.vendor_segment_pref = vendor_segment_pref

    def get_file_byte_length(self) -> int:
        file_byte_length: int = len(self.file_bytes)
        return file_byte_length

    # get each byte length for specific segment:
    def get_segment_specific_byte_length(self) -> int:
        segment_specific_byte_length: int = round(self.file_byte_length / self.vendor_segment_pref)
        return segment_specific_byte_length

    def get_byte_chunk_for_segments(self, segment_specific_byte_length: int) -> List[List[int, bytes, Any]]:
        all_partition_lists: List = []
        for each_byte in bytearray(self.file_bytes):
            # init a sub_list
            sub_list = [each_byte]
            if len(sub_list) == segment_specific_byte_length:
                # add sublist to the general list:
                all_partition_lists.append(sub_list)
                # call the function all over again
            '''else:
                # all_partition_lists.append(sub_list)
                self.get_byte_chunk_for_segments()'''
        return all_partition_lists

    def join_specific_byte_array_segments(self, all_partition_lists: List[List[int, bytes, Any]]) -> bytes:
        # init:

        # get segment based on user defined preference:
        auth_access_segment = all_partition_lists[0:self.vendor_segment_pref]
        # combine all the segment sub-lists into a unified list:
        for each_segment in auth_access_segment:
            # use list comprehension:
            single_sublist: List = [each_byte_int for each_byte_int in each_segment]

            # convert to byte-array:
            single_sublist_byte_array: bytearray = bytearray(single_sublist)

            # convert to bytes:
            single_sublist_byte: bytes = bytes(single_sublist_byte_array)

            # then:
            return single_sublist_byte
