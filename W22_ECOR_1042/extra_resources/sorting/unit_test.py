from bubble_sort import bubble_sort, bubble_sort2
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort

from typing import Any
import random


def unit_test(actual: Any, expected: Any) -> bool:
    if not isinstance(actual, type(expected)):
        print("The types of actual and expected mismatch!")
        print(f"type actual={type(actual)}, type expected={type(expected)}")

    if actual != expected:
        print(f"FAILURE: results aren't equal. Got: {actual}, Expected: {expected}")
        return False
    else:
        print("PASS")
        return True


if __name__ == "__main__":
    # Create a random list of 7 ints in between 1 and 50
    test_list = [random.randrange(1, 50, 1) for i in range(7)]  # type: ignore

    # We'll use python's built-in sort() to define our
    # expected behaviour (not great but convenient -> if sort() has a bug, we might too).
    expected = test_list.copy()
    expected.sort()

    unit_test(bubble_sort(test_list), expected)
    unit_test(bubble_sort2(test_list), expected)
    unit_test(selection_sort(test_list), expected)
    unit_test(insertion_sort(test_list), expected)
    unit_test(merge_sort(test_list), expected)
