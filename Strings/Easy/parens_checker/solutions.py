import sys
from pathlib import Path
from inspect import getmembers, isfunction
utils_path = Path(__file__).resolve().parents[3] / "utils"
sys.path.append(str(utils_path))
from run_tests import run_tests  # noqa E402


def solution_1(string):
    """
    Time Complexity: O(n) - n is the length of string
    Space Complexity: O(n)
    """
    brace_pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    closing_braces = set(brace_pairs.values())
    closings_stack = []

    for char in string:

        if char in closing_braces:
            if not closings_stack or char != closings_stack.pop():
                return False

        elif char in brace_pairs:
            closings_stack.append(brace_pairs[char])

    return not closings_stack


if __name__ == "__main__":
    test_cases_path = Path(__file__).parent / "tests.json"
    solutions = [
        f for _, f in getmembers(sys.modules[__name__], isfunction)
        if "solution" in f.__name__
    ]
    for solution in solutions:
        run_tests(solution, test_cases_path)
