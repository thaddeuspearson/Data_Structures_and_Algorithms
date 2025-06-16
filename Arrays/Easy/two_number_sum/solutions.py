from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


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
    run_tests()
