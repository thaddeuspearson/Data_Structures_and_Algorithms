from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(array):
    """
    Time Complexity: O(n) - n is the length of array
    Space Complexity: O(1)
    """
    if len(array) < 3:
        return True

    direction = None
    prev = array[0]

    for curr in array[1:]:
        if curr == prev:
            continue
        if not direction:
            direction = curr - prev
        elif direction < 0 and curr > prev:
            return False
        elif direction > 0 and curr < prev:
            return False
        prev = curr
    return True


if __name__ == "__main__":
    run_tests()
