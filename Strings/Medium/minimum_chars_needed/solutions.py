from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(words):
    """
    Time Complexity: O(n*l) - n is the length of the array
    Space Complexity: O(n*l) - l is the length of longest word
    """
    min_char_counts = {}

    for word in words:
        letter_counts = {}

        for char in word:
            letter_counts[char] = letter_counts.get(char, 0) + 1

        for char, count in letter_counts.items():
            min_char_counts[char] = max(min_char_counts.get(char, 0), count)

    return [letter
            for letter, count in min_char_counts.items() for _ in range(count)]


if __name__ == "__main__":
    run_tests()
