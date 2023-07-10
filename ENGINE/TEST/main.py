# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import deque

from ENGINE.CUSTOMEMMA.CustomEmmaAbstraction import EmmaByteAbstraction
from ENGINE.CUSTOMEMMA.CustomEmmaReverseAbstraction import EmmaByteReverseAbstraction


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # print(EmmaByteAbstraction.byte_to_emma_rep_register(bytearray([2, 2, 3, 4, 5, 7, 3, 7, 5, 5, 5])))
    print(EmmaByteReverseAbstraction.emma_rep_register_to_byte(deque([
        {'total_byte_length': 11},
        {'considered_elem': 2, 'pos_of_occurrence': [0, 1, 2, 6, 3, 4, 8, 9, 10, 5, 7], 'times_of_occurrence': 2},
        {'considered_elem': 3, 'pos_of_occurrence': [0, 1, 2, 6, 3, 4, 8, 9, 10, 5, 7], 'times_of_occurrence': 4},
        {'considered_elem': 4, 'pos_of_occurrence': [0, 1, 2, 6, 3, 4, 8, 9, 10, 5, 7], 'times_of_occurrence': 5},
        {'considered_elem': 5, 'pos_of_occurrence': [0, 1, 2, 6, 3, 4, 8, 9, 10, 5, 7], 'times_of_occurrence': 9},
        {'considered_elem': 7, 'pos_of_occurrence': [0, 1, 2, 6, 3, 4, 8, 9, 10, 5, 7], 'times_of_occurrence': 11}
    ])))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
