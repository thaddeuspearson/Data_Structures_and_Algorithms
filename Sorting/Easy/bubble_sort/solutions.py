from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(array):
    """
    Time Complexity: O(n^2) - n is the length of the array
    Space Complexity: O(1)
    """
    unsorted_len = len(array)
    is_sorted = False
    curr_largest = float('-inf')

    while unsorted_len > 1 and not is_sorted:
        is_sorted = True

        for i in range(unsorted_len-1):
            if array[i] >= curr_largest:
                curr_largest = array[i]
                if i + 2 == unsorted_len:
                    unsorted_len -= 1
                    curr_largest = float('-inf')

            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                is_sorted = False
    return array


def solution_2(array):
    """
    Time Complexity: O(n^2) - n is the length of array
    Space Complexity: O(1)
    """
    is_sorted = False
    counter = 1

    while not is_sorted:
        is_sorted = True

        for i in range(len(array) - counter):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                is_sorted = False
        counter += 1
    return array


if __name__ == "__main__":
    run_tests()
