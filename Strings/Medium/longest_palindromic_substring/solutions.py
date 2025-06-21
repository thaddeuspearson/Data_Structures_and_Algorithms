from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(string):
    """
    Time Complexity: O(n^2) - n is the length of string
    Space Complexity: O(n)
    """
    longest_pal_sub = ""

    for i in range(len(string)):
        candidate = max(
            get_longest_pal_sub(i-1, i+1, string),
            get_longest_pal_sub(i-1, i, string),
            key=len
        )
        longest_pal_sub = max(longest_pal_sub, candidate, key=len)
    return longest_pal_sub


def get_longest_pal_sub(start, end, string):
    while start >= 0 and end < len(string) and string[start] == string[end]:
        start -= 1
        end += 1
    return string[start+1: end]


if __name__ == "__main__":
    run_tests()
