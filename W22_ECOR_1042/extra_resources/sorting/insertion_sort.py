from typing import List, Any

"""
Insertion Sort
Virtually splits the array into a sorted and unsorted portion.
Takes and element from the unsorted region and
iterates until it can be placed in its correct positonin the sorted region.

For ascending order sorting, we'll use the left portion to be 
sorted, the right portion as unsorted.

1. Iterate from arr[1] to arr[n] (arr[0] is the initial sorted region).
2. Denote the next element we'd like to insert into the sorted region as 
current.
2. Compare the current to its predecessor (the element before it).
3. If current is smaller than its predecessor, compare it to
the previous predecessor. Swap current with the original predecessor.
4. Keep going until current is larger than the predecessor, indicating that
it's in the correct position.
5. Repeat for all elements in the unsorted region.
"""

__author__ = "yousef"


def insertion_sort(lst: List[Any]) -> List[Any]:
    """
        Sorts the specified lst in ascending order (in place).
    """

    # For each element of the unsorted region
    for i in range(1, len(lst)):
        current = lst[i]

        # Compare to predecessors to find correct position
        # to insert current into the sorted region. predecessor = lst[j]
        j = i - 1

        # Keep going until current >= predecessor or
        # we're at the first element of the array
        while j >= 0 and current < lst[j]:
            lst[j + 1] = lst[j]     # swap current (j + 1) and predecessor (j).
            j -= 1                  # current is now in position j, predecessor at j-1 (relative to original j)

        # Either j = 0 (first index) or current > lst[j] meaning
        # lst[j + 1] is current's correct position.
        lst[j + 1] = current

    return lst.copy()
