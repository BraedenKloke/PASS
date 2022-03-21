from bisection_sqrt import bisection_sqrt
from exhaustive_sqrt import exhaustive_sqrt
from heron_sqrt import heron_sqrt
from typing import Any

EPSILON = 0.01


def unit_test(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, type(expected)):
        print("The types of actual and expected mismatch!")
        print(f"type actual={type(actual)}, type expected={type(expected)}")

    if abs(actual - expected) > EPSILON:
        print(f"FAILURE: results aren't equal. Got: {actual}, Expected: {expected}")
        return False
    else:
        print("PASS")
        return True


if __name__ == "__main__":
    unit_test(5.0, exhaustive_sqrt(25))
    unit_test(5.0, bisection_sqrt(25))
    unit_test(5.0, heron_sqrt(25))
