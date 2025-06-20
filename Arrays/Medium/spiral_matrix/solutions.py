from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(array):
    """
    Time Complexity: O(n) - where n is total # of elems in the flattened array
    Space Complexity: O(n)
    """
    flattened = []

    x_start = 0
    x_end = len(array[0])
    y_start = 0
    y_end = len(array)

    while x_start < x_end and y_start < y_end:

        for idx in range(x_start, x_end):
            flattened.append(array[y_start][idx])
        y_start += 1

        for idx in range(y_start, y_end):
            flattened.append(array[idx][x_end-1])
        x_end -= 1

        if not (x_start < x_end and y_start < y_end):
            break

        for idx in range(x_end-1, x_start-1, -1):
            flattened.append(array[y_end-1][idx])
        y_end -= 1

        for idx in range(y_end-1, y_start-1, -1):
            flattened.append(array[idx][x_start])
        x_start += 1

    return flattened


if __name__ == "__main__":
    run_tests()
