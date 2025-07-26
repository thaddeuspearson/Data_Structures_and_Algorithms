from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(n):
    """
    Time Complexity: O(n) - n is the number to proces fibonacci up to
    Space Complexity: O(1)
    """
    if n == 0 or n == 1:
        return n
    else:
        return solution_1(n-2) + solution_1(n-1)


if __name__ == "__main__":
    run_tests()
