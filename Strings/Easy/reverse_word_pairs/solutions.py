from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(words):
    """
    Time Complexity: O(n) - n is the length of words
    Space Complexity: O(n)
    """
    seen = set()
    reverse_word_pairs = []

    for word in words:
        if word not in seen:
            reversed_word = word[::-1]
            if reversed_word in seen:
                reverse_word_pairs.append([reversed_word, word])
            else:
                seen.add(word)
    return reverse_word_pairs


if __name__ == "__main__":
    run_tests()
