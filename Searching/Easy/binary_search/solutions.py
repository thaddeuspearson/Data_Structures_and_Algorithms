from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(array, target):
    """
    Time Complexity: O(log n) - n is the length of array
    Space Complexity: O(1)
    """
    return recursive_helper(array, target, 0, len(array))


def recursive_helper(array, target, left, right):
    mid = (left + right) // 2

    if left >= right:
        return -1
    elif array[mid] == target:
        return mid
    else:
        if array[mid] <= target:
            left = mid+1
        else:
            right = mid
    return recursive_helper(array, target, left, right)


def solution_2(array, target):
    """
    Time Complexity: O(log n) - n is the length of array
    Space Complexity: O(1)
    """
    left = 0
    right = len(array)

    while left < right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        else:
            if array[mid] <= target:
                left = mid+1
            else:
                right = mid
    return -1

# This is a test for GHA workflow

if __name__ == "__main__":
    run_tests()
