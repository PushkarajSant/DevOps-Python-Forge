"""
Output Comparator — compares actual program output against expected output
using various comparison modes.
"""
import json
import re
from typing import Tuple


def compare_output(actual: str, expected: str, mode: str = "exact") -> Tuple[bool, str]:
    """
    Compare actual vs expected output.

    Modes:
        exact    — Exact string match (after stripping trailing whitespace)
        contains — Expected must appear somewhere in actual
        json     — Parse both as JSON and compare objects
        regex    — Expected is a regex pattern matched against actual
        lines    — Compare line-by-line, ignoring trailing whitespace per line

    Returns:
        (passed, feedback_message)
    """
    actual_stripped = actual.strip()
    expected_stripped = expected.strip()

    comparators = {
        "exact": _compare_exact,
        "contains": _compare_contains,
        "json": _compare_json,
        "regex": _compare_regex,
        "lines": _compare_lines,
    }

    comparator = comparators.get(mode, _compare_exact)
    return comparator(actual_stripped, expected_stripped)


def _compare_exact(actual: str, expected: str) -> Tuple[bool, str]:
    """Exact match after stripping."""
    if actual == expected:
        return True, ""

    # Helpful feedback
    if actual.lower() == expected.lower():
        return False, "Case mismatch — check uppercase/lowercase."
    if actual.replace(" ", "") == expected.replace(" ", ""):
        return False, "Spacing differs — check whitespace in your output."

    return False, f"Expected:\n{expected}\n\nGot:\n{actual}"


def _compare_contains(actual: str, expected: str) -> Tuple[bool, str]:
    """Expected string must appear in actual output."""
    if expected in actual:
        return True, ""
    return False, f"Output should contain: '{expected}'"


def _compare_json(actual: str, expected: str) -> Tuple[bool, str]:
    """Parse both as JSON and do deep comparison."""
    try:
        actual_obj = json.loads(actual)
    except json.JSONDecodeError:
        return False, "Your output is not valid JSON."

    try:
        expected_obj = json.loads(expected)
    except json.JSONDecodeError:
        return False, "Internal error: expected output is not valid JSON."

    if actual_obj == expected_obj:
        return True, ""

    # Check if difference is just key ordering
    if json.dumps(actual_obj, sort_keys=True) == json.dumps(expected_obj, sort_keys=True):
        return True, ""

    return False, f"JSON mismatch.\nExpected: {json.dumps(expected_obj, indent=2)}\nGot: {json.dumps(actual_obj, indent=2)}"


def _compare_regex(actual: str, expected: str) -> Tuple[bool, str]:
    """Expected is a regex pattern; actual must match."""
    try:
        if re.search(expected, actual, re.MULTILINE):
            return True, ""
        return False, f"Output did not match pattern: {expected}"
    except re.error as e:
        return False, f"Internal error: invalid regex pattern — {e}"


def _compare_lines(actual: str, expected: str) -> Tuple[bool, str]:
    """Compare line-by-line, trimming each line."""
    actual_lines = [line.rstrip() for line in actual.splitlines()]
    expected_lines = [line.rstrip() for line in expected.splitlines()]

    if len(actual_lines) != len(expected_lines):
        return False, f"Expected {len(expected_lines)} line(s) but got {len(actual_lines)}."

    for i, (a, e) in enumerate(zip(actual_lines, expected_lines)):
        if a != e:
            return False, f"Line {i + 1} differs.\nExpected: '{e}'\nGot:      '{a}'"

    return True, ""
