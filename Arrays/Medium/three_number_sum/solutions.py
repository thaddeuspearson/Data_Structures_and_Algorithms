from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(array, target):
    """
    Time Complexity: O(n^2) - n is the len of array
    Space Complexity: O(n)
    """
    triplets = []
    array_len = len(array)
    array.sort()

    for l, _ in enumerate(array[:-2]):  # noqa E741
        mid = l + 1
        r = array_len - 1

        while mid < r and r < array_len:
            triplet = [array[l], array[mid], array[r]]
            candidate_sum = sum(triplet)

            if candidate_sum == target:
                triplets.append(triplet)
                mid += 1
                r -= 1
            elif candidate_sum < target:
                mid += 1
            else:
                r -= 1

    return triplets


if __name__ == "__main__":
    run_tests()
