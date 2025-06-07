import sys
from pathlib import Path
from inspect import getmembers, isfunction
utils_path = Path(__file__).resolve().parents[3] / "utils"
sys.path.append(str(utils_path))
from run_tests import run_tests  # noqa E402


def solution_1(array: list) -> list:
    """
    Time Complexity: O(n) - n is the size of the input array
    Space Complexity: O(n)
    """
    l_idx = 0
    r_idx = 0
    array_len = len(array)
    sorted_squared = []

    while r_idx < array_len and array[r_idx] < 0:
        r_idx += 1
    l_idx = r_idx - 1

    while 0 <= l_idx and r_idx < array_len:

        if array[r_idx] <= abs(array[l_idx]):
            sorted_squared.append(array[r_idx]**2)
            r_idx += 1
        else:
            sorted_squared.append(array[l_idx]**2)
            l_idx -= 1

    if l_idx < 0:
        for r_idx in range(r_idx, array_len):
            sorted_squared.append(array[r_idx]**2)
    else:
        for l_idx in range(l_idx, -1, -1):
            sorted_squared.append(array[l_idx]**2)

    return sorted_squared


def solution_2(array: list) -> list:
    """
    Time Complexity: O(n) - n is the size of the input array
    Space Complexity: O(n)
    """
    array_len = len(array)
    l_idx = 0
    r_idx = array_len - 1
    sorted_squared = [0 for _ in range(array_len)]

    for idx in range(array_len - 1, -1, -1):
        if abs(array[l_idx]) >= abs(array[r_idx]):
            sorted_squared[idx] = array[l_idx]**2
            l_idx += 1
        else:
            sorted_squared[idx] = array[r_idx]**2
            r_idx -= 1

    return sorted_squared


if __name__ == "__main__":
    solutions = [
        f for _, f in getmembers(sys.modules[__name__], isfunction)
        if "solution" in f.__name__
    ]
    for func in solutions:
        run_tests(func, "tests.json")
