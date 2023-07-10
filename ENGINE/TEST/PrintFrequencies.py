from typing import *
from collections import *


# argument can be either str or list containing string
def print_frequencies(word_to_consider: Union[str, List[str]]) -> Dict:

    global map_of_occurence, all_joined_words

    if isinstance(word_to_consider, List):
        # join all the words together before consideration:
        for each_word in word_to_consider:
            # init:
            all_joined_words = all_joined_words + each_word
    else:
        all_joined_words = word_to_consider

    # now start running the algorithm:
    word_count_len: int = len(all_joined_words)

    # init:
    # occurrence_register: Deque = Deque()
    map_of_occurrence: Dict = {}
    # current_elem = 0
    times_of_occurrence: int = 0
    pos_of_occurrence: List = []

    # add total length in consideration to the register:
    # occurrence_register.append({"total_byte_length": word_count_len})

    # contains unique elements that will be searched for occurrences:
    all_considered_elems: Set = set(all_joined_words)
    # now, search each element in the considered set above in the file_byte_array:
    for each_considered_elem in all_considered_elems:
        pos_observer_counter = -1  # set position counter as the sublist is looped:
        for each_elem in all_joined_words:
            # step position observer:
            pos_observer_counter += 1
            # get the position of the elem and append to a List:
            if each_considered_elem == each_elem:
                times_of_occurrence += 1
                # pos_of_occurrence.append(pos_observer_counter)

                # get all observables:
                '''{
                    # "considered_elem": each_considered_elem,
                    # "pos_of_occurrence": pos_of_occurrence,
                    # "times_of_occurrence": times_of_occurrence
                }'''
                map_of_occurrence[each_considered_elem] = times_of_occurrence

        # init:
        sorted_occurrence_map = {}

        # sort dictionary:
        sorted_values: List = sorted(map_of_occurrence.values())

        for each_sorted_value in reversed(sorted_values):
            for each_key in map_of_occurrence.keys():
                if map_of_occurrence[each_key] == each_sorted_value:
                    # insert:
                    sorted_occurrence_map[each_key] = map_of_occurrence[each_key]

        return sorted_occurrence_map


if __name__ == '__main__':
    occurrence_frequency = print_frequencies('PPPyCCCChaaaaaarrrrmmmmmymmmmmmMMM')
    print(occurrence_frequency)
