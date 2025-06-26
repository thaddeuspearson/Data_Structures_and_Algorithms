from sys import path
from pathlib import Path
path.append(str(Path(__file__).resolve().parents[3]))
from utils.run_tests import run_tests  # noqa E402


def solution_1(string1, string2):
    """
    Time Complexity: O(n) - n is length of longer string
    Space Complexity: O(n)
    """
    if len(string1) <= len(string2):
        first = string1
        second = string2
    else:
        first = string2
        second = string1

    diff_lens = abs(len(second) - len(first))
    if diff_lens > 1:
        return False

    i = 0
    j = 0
    edit_found = False

    while i < len(first) and j < len(second):
        if first[i] != second[j]:
            if diff_lens:
                if j == i+1:
                    return False
            else:
                if edit_found:
                    return False
                else:
                    edit_found = True
                    i += 1
        else:
            i += 1
        j += 1
    return True


def solution_2(string1, string2):
    """
    Time Complexity: O(n) - n is length of longer string
    Space Complexity: O(1)
    """
    diff_lens = abs(len(string1) - len(string2))
    if diff_lens > 1:
        return False

    i = 0
    j = 0
    editted = False

    while i < len(string1) and j < len(string2):
        if string1[i] != string2[j]:
            if editted:
                return False
            else:
                editted = True

            if diff_lens:
                if len(string1) < len(string2):
                    j += 1
                else:
                    i += 1
                continue
        i += 1
        j += 1
    return True


if __name__ == "__main__":
    run_tests()
