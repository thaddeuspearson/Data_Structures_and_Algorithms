from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(nums):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(1, len(nums)):
        curr_idx = i

        while curr_idx > 0:
            curr = nums[curr_idx]
            prev = nums[curr_idx-1]

            if curr < prev:
                nums[curr_idx], nums[curr_idx-1] = prev, curr
                curr_idx -= 1
            else:
                break
    return nums


def solution_2(nums):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(1, len(nums)):
        curr_idx = i

        while curr_idx > 0 and nums[curr_idx] < nums[curr_idx-1]:
            nums[curr_idx], nums[curr_idx-1] = nums[curr_idx-1], nums[curr_idx]
            curr_idx -= 1
    return nums


if __name__ == "__main__":
    run_tests()
