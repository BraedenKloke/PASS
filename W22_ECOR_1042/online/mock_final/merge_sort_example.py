from typing import List, Any

def merge_sort(lst: List[Any]) -> List[Any]:
    """
        Sorts the specified lst in ascending order (in place).
        >>> merge_sort([4, 3, 1, 2])
        >>> [1, 2, 3, 4]
    """
    # There's nothing to do if the list is a
    # single element -> this is our base case (when to stop recursing).
    # A single element list is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Otherwise, split the list into two
    # halves and merge sort both.

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    print("Now merging:", left, right)

    """
        Now merge the two sorted lists - left and right
        into one sorted list.
        i : index of next element to insert from left list
        j : index of next element to insert from right list
        k : index to insert into the "sorted" list.
    """

    i = j = k = 0

    """
        Left and right are sorted. Iterate over both
        and keep inserting the smaller "current" element from
        either list into the "sorted" list.
    """
    while i < len(left) and j < len(left):
        if left[i] < right[j]:                  # Left has the smaller element
            lst[k] = left[i]
            i += 1
        else:                                   # Right has the smaller element
            lst[k] = right[j]
            j += 1

        k += 1

    # We can finish inserting all the elements of one list (left or right)
    # into the sorted list but not the other. So, just ensure
    # that we insert the remaining elements (which will already be in sorted order)

    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1

    return lst.copy()


if __name__ == "__main__":
    lst = [18, 2, 9, 3, 4, 5, 5]
    merge_sort(lst)
    print(lst)