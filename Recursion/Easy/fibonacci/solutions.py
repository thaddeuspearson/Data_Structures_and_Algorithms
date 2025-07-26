from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(n):
    """
    Time Complexity: O()
    Space Complexity: O()
    """


if __name__ == "__main__":
    run_tests()
