import sys
from pathlib import Path
utils_path = Path(__file__).resolve().parents[3] / "utils"
sys.path.append(str(utils_path))
from run_tests import run_tests
from inspect import getmembers, isfunction


def solution_1():
    pass


if __name__ == "__main__":
    solutions = [
        f for _,
        f in getmembers(sys.modules[__name__], isfunction)
        if "solution" in f.__name__
    ]
    for func in solutions:
        run_tests(func, "tests.json")