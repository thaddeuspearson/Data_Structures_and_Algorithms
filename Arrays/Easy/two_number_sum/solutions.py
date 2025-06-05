import sys
from pathlib import Path
utils_path = Path(__file__).resolve().parents[3] / "utils"
sys.path.append(str(utils_path))
from run_tests import run_tests
from inspect import getmembers, isfunction


def solution_1(array: list, target: int) -> list:
    """
    Time Complexity: O(nlog(n))
    Space Complexity: O(1)
    """
    array.sort()
    front, back = 0, len(array) - 1

    while front < back:
        curr_sum = array[front] + array[back]

        if curr_sum == target:
            return [array[front], array[back]]
        elif curr_sum < target:
            front += 1
        else:
            back -= 1
    return []


def solution_2(array: list, target: int) -> list:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    checked_nums = set()

    for num in array:
        candidate = target - num
        if candidate in checked_nums:
            return [candidate, num]
        else:
            checked_nums.add(num)
    return []


if __name__ == "__main__":
    solutions = [
        f for _,
        f in getmembers(sys.modules[__name__], isfunction)
        if "solution" in f.__name__
    ]
    for func in solutions:
        run_tests(func, "tests.json")
