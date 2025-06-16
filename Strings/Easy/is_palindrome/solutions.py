from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(string):
    """
    Time Complexity: O(n) - n is the length of the input array
    Space Complexity: O(n)
    """
    string = ''.join(c for c in string if c.isalnum())
    string = string.lower()
    back = len(string) - 1

    for front in range(len(string) // 2):
        if not string[front] == string[back]:
            return False
        back -= 1
    return True


if __name__ == "__main__":
    run_tests()
