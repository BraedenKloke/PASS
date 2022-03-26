from typing import List, Any

"""
Selection Sort
Selects the current minimum of the list and sets it into its
correct place.

1. Find smallest element and swap with lst[0].
2. Find next smallest and swap with lst[0 + 1].
3. Find the ith smallest and swap with lst[i]
4. Repeat the process...
"""

__author__ = "yousef"


def selection_sort(lst: List[Any]) -> List[Any]:
    """
        Sorts the specified lst in ascending order (in place).
    """

    # For each position in the list (...find the
    # correct element to fill that spot)
    for i in range(len(lst)):
        # Initially set the ith position to the minimum
        # we'll check if there's a smaller number in the remaining list.
        min_idx = i

        # For each remaining number in the list,
        # find the minimum
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:                   # If lst[j] < lst[min_idx], lst[j] is the new minimum.
                min_idx = j

        lst[min_idx], lst[i] = lst[i], lst[min_idx]     # Put the minimum in its sorted position.

    return lst.copy()
