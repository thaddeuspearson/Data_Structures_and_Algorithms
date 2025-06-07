"""
A basic testing suite to handle testing for the challenges
"""
import sys
import json
from typing import Callable


def load_test_cases(tests_path: str) -> list:
    """
    Load json test cases, expects a list of JSON blobs
    """
    with open(tests_path, 'r', encoding="utf-8") as f:
        return json.load(f)


def perform_tests(func_to_test: Callable, tests: dict):
    """
    Runs the given test cases with the given function

    Expects JSON, a list of test cases in this format:
    [
      {
        "input": {
          "arg_1": value,
          "arg_2: value
        },
        "output": value
      }
    ]
    """
    results = []
    test_num = 1

    for test_case in tests:
        test_input = test_case["input"]
        actual = func_to_test(**test_input)
        expected = test_case["output"]
        passed = actual == expected

        results.append({
            "func_name": func_to_test.__name__,
            "test_num": test_num,
            "passed": passed,
            "input": ", ".join(f"{v}" for v in test_input.values()),
            "expected": expected,
            "actual": actual
        })

        test_num += 1

    return results


def display_results(results: list) -> None:
    """
    Prints the test results
    """
    line = f"\n  *{'-' * 50}*"
    total_passed = 0

    for result in results:
        print(line)
        print(
            f"   [{'+' if result['passed'] else '-'}] {result['func_name']}:"
            f" Test {result['test_num']}\n\n"
        )

        if not result['passed']:
            print(f"\t   input: {(result['input'])}\n")
            print(f"\texpected: {result['expected']}\n")
            print(f"\t  actual: {result['actual']}\n")
        else:
            total_passed += 1
    print(line)
    print(
        f"   Total Tests Passed: {total_passed} out of {len(results)}"
        f" ({round(total_passed / len(results), 2) * 100}%)\n\n\n"
    )


def run_tests(func_to_test: Callable, tests_path: str) -> None:
    """
    Handler for test case execution and display
    """
    try:
        tests = load_test_cases(tests_path)
    except FileNotFoundError:
        print("Missing valid `tests.json` file in the working directory.")
        sys.exit(1)

    results = perform_tests(func_to_test, tests)
    display_results(results)
