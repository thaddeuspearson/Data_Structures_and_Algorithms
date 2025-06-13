import sys
from pathlib import Path
from inspect import getmembers, isfunction
utils_path = Path(__file__).resolve().parents[3] / "utils"
sys.path.append(str(utils_path))
from run_tests import run_tests  # noqa E402


def solution_1(words):
    """
    Time Complexity: O(n) - n is the len of the strings array
    Space Complexity: O(m) - m is the len of the shortest string in the array
    """
    if not words:
        return []

    shortest = words[0]

    for s in words:
        if len(s) < len(shortest):
            shortest = s

    lookup = {c: set() for c in shortest}

    for i, s in enumerate(words):

        for c in s:
            if c in lookup:
                lookup[c].add(i)

    return [c for c in lookup if len(lookup[c]) == len(words)]


if __name__ == "__main__":
    test_cases_path = Path(__file__).parent / "tests.json"
    solutions = [
        f for _, f in getmembers(sys.modules[__name__], isfunction)
        if "solution" in f.__name__
    ]
    for func in solutions:
        run_tests(func, test_cases_path)
