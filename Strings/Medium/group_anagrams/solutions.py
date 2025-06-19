from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(strings):
    """
    Time Complexity: O(n * m * logm) - n is length of strings,
                                       m is length of longest word
    Space Complexity: O(n * m)
    """
    lookup = {}

    for string in strings:
        curr = tuple(sorted(string))
        lookup.setdefault(curr, [])
        lookup[curr].append(string)
    return list(lookup.values())


if __name__ == "__main__":
    run_tests()
