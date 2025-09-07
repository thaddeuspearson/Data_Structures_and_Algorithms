from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(array: int, depth: int = 1):
    """
    Time Complexity: O(n) - n is the length of the input array
    Space Complexity: O()
    """
    product_sum = 0

    for elem in array:
        if isinstance(elem, list):
            product_sum += solution_1(elem, depth+1)
        else:
            product_sum += elem

    return product_sum * depth


if __name__ == "__main__":
    run_tests()
