"""
A basic testing suite to handle test cases for the challenges
"""
from inspect import getmembers, getmodule, isfunction, stack
from json import load
from sys import exit
from pathlib import Path
from typing import Callable


def load_test_cases(tests_path: str) -> list:
    """
    Load json test cases, expects a list of JSON blobs
    """
    with open(tests_path, 'r', encoding="utf-8") as f:
        return load(f)


def perform_tests(func_to_test: Callable, tests: dict) -> list:
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
    failed_tests = False
    test_num = 1

    for test_case in tests:
        test_input = test_case["input"]
        actual = func_to_test(**test_input)
        expected = test_case["output"]
        passed = actual == expected

        if not passed and failed_tests is False:
            failed_tests = True

        results.append({
            "func_name": func_to_test.__name__,
            "test_num": test_num,
            "passed": passed,
            "input": ", ".join(f"{v}" for v in test_input.values()),
            "expected": expected,
            "actual": actual
        })
        test_num += 1
    return results, failed_tests


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
        f" ({round(total_passed / len(results) * 100, 2):.2f}%)\n\n\n"
    )


def get_caller_module():
    """
    Return the module object of the immediate caller
    """
    current_file = __file__

    for frame_info in stack():
        module = getmodule(frame_info.frame)
        if module and getattr(module, "__file__", None) != current_file:
            return module


def get_solutions():
    """
    Returns a list of (name, function) tuples for all solutions given
    """
    return [
        solution
        for name, solution in getmembers(get_caller_module(), isfunction)
        if "solution" in name
    ]


def get_test_cases_path():
    """
    Return the absolute path to the caller's module file
    """
    return Path(get_caller_module().__file__).resolve().parent / "tests.json"


def run_tests(tests_path: str = None) -> None:
    """
    Handler for test case execution and display
    """
    tests_path = tests_path or get_test_cases_path()

    try:
        tests = load_test_cases(tests_path)
    except FileNotFoundError:
        print(f"Missing valid `tests.json` file at {tests_path}.")
        exit(1)

    incorrect_solutions = []

    for solution in get_solutions():
        results, failed_tests = perform_tests(solution, tests)
        display_results(results)

        if failed_tests:
            incorrect_solutions.append(results[0]["func_name"])

    if incorrect_solutions:
        incorrect = ", ".join(solution for solution in incorrect_solutions)
        print(f"Tests Failed for: {incorrect}\n")
        exit("❌ Some solution test cases failed!")
    else:
        exit(0)
