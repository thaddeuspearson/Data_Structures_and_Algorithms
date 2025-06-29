from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(array):
    """
    Time Complexity: O(n) - n is length of array
    Space Complexity: O(1)
    """
    greatest, greater, great = float('-inf'), float('-inf'), float('-inf')
    
    for curr in array:
        if curr >= greatest:
            great = greater
            greater = greatest
            greatest = curr
        elif curr >= greater:
            great = greater
            greater = curr
        elif curr >= great:
            great = curr
    return [great, greater, greatest]


def solution_2(array):
    """
    Time Complexity: O(n) - n is length of array
    Space Complexity: O(1)
    """
    def shift_and_update(array, num, idx):
        for i in range(idx+1):
            array[i] = num if i == idx else array[i+1]

    largest_3 = [None, None, None]

    for num in array:
        for i in range(2, -1, -1):
            if largest_3[i] is None or num > largest_3[i]:
                shift_and_update(largest_3, num, i)
                break
    return largest_3


if __name__ == "__main__":
    run_tests()
