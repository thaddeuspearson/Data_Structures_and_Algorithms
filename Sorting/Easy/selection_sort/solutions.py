from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(array):
    """
    Time Complexity: O(n^2) - n is the length of array
    Space Complexity: O(1)
    """
    for i in range(len(array)):
        swap_idx = i

        for j in range(i+1, len(array)):
            if array[j] < array[swap_idx]:
                swap_idx = j

        array[i], array[swap_idx] = array[swap_idx], array[i]

    return array


if __name__ == "__main__":
    run_tests()
