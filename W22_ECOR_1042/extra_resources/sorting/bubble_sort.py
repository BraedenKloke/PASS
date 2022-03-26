from typing import List, Any

"""
Implementation of bubble sort.

Iterates over the provided list and compares
each pair of adjacent elements. If a pair is
in the wrong order, they're swapped until no
more swaps occur - indicates we're done.

Time complexity: high [O(n^2)] -> slow.
"""

__author__ = "yousef"


def bubble_sort(lst: List[Any]) -> List[Any]:
    """
        Sorts the specified list lst in place in ascending order.

        "in place": since lists are mutable, modifying a list inside
        a function modifies the list argument that was passed in (which is
        outside the function). Meaning, we don't *need* to return the list.
    """

    swaps = True        # Flag that tracks if we made a swap

    # Keep iterating until no swaps occur. If
    # we pass through the entire list without swapping
    # that mean's it's sorted.
    while swaps:
        swaps = False

        # Go through each pair in the list. We have - 1
        # since we compare lst[i] and **lst[i + 1]**
        for i in range(len(lst) - 1):
            # Compare a pair
            if lst[i] > lst[i + 1]:
                # They're out of order is element i is bigger
                # than element i + 1. Swap them
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swaps = True

    return lst.copy()


def bubble_sort2(lst: List[Any]) -> List[Any]:
    """
        This is the version in the lectures.
        Sorts the specified list lst in place in ascending order.

        In bubble sort, the highest element is always
        "bubbled" up to the end of the list so after iteration i,
        the highest i elements are in their correct sorted positions. This means
        we only need to consider the remaining (n - i) elements for a list of size n.

        Example: Consider [1, 4, 2, 2, 3, 2]. Applying bubble sort...
        -> [1, 2, 4, 2, 3, 2]   swap 4 and 2
        -> [1, 2, 2, 4, 3, 2]   swap 4 and 2
        -> [1, 2, 2, 3, 4, 2]   swap 4 and 3
        -> [1, 2, 2, 3, 2, 4]   swap 4 and 2

        Notice how 4 bubbled to its sorted position. On the next iteration 3
        would be in its correct position and so on...
    """

    # After the ith iteration, the highest i elements are sorted.
    # So we're guaranteed to have a sorted list after the nth iteration (n = len(lst))
    for i in range(len(lst)):
        # Go through each pair in the list. We have - 1
        # since we compare lst[j] and **lst[j + 1]**
        # -i since the top i elements are sorted.
        for j in range(len(lst) - 1 - i):
            if (lst[j] > lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst.copy()
