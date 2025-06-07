import sys
from pathlib import Path
from inspect import getmembers, isfunction
utils_path = Path(__file__).resolve().parents[3] / "utils"
sys.path.append(str(utils_path))
from run_tests import run_tests  # noqa: E402


def solution_1(array: list, sequence: list) -> bool:
    """
    Time Complexity: O(n) - n is the length of array
    Space Complexity: O(1)
    """
    arr_idx = 0
    sub_seq_idx = 0
    arr_len = len(array)
    sub_seq_len = len(sequence)

    while arr_idx < arr_len and sub_seq_idx < sub_seq_len:

        if array[arr_idx] == sequence[sub_seq_idx]:
            sub_seq_idx += 1

        arr_idx += 1

    return sub_seq_idx == sub_seq_len


def solution_2(array: list, sequence: list) -> bool:
    """
    Time Complexity: O(n) - n is the length of array
    Space Complexity: O(1)
    """
    sub_seq_idx = 0
    seq_len = len(sequence)

    for elem in array:
        if sub_seq_idx == seq_len:
            break

        if elem == sequence[sub_seq_idx]:
            sub_seq_idx += 1

    return sub_seq_idx == seq_len


if __name__ == "__main__":
    solutions = [
        f for _, f in getmembers(sys.modules[__name__], isfunction)
        if "solution" in f.__name__
    ]
    for func in solutions:
        run_tests(func, "tests.json")
