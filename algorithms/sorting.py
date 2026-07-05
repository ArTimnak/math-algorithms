def binary_insertion_sort(arr, left, right):
    """
    Insertion sort optimized with binary search for the insertion point.

    This is used within Timsort for small chunks of data.

    Parameters
    ----------
    arr : list
        The list to be sorted.
    left : int
        Left index of the subarray to sort.
    right : int
        Right index of the subarray to sort (exclusive).
    """
    for i in range(left + 1, right):
        key = arr[i]
        j = i - 1

        low, high = left, i - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1

        while j >= low:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, left, mid, right):
    """
    Merge two sorted subarrays.

    Parameters
    ----------
    arr : list
        The array containing the subarrays.
    left : int
        Start index of the first subarray.
    mid : int
        End index of the first subarray (start of the second).
    right : int
        End index of the second subarray.
    """
    n1 = mid - left
    n2 = right - mid

    L = arr[left:mid]
    R = arr[mid:right]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def timsort(arr, min_run=64):
    """
    Sort an array using Timsort algorithm.

    Timsort is a hybrid sorting algorithm derived from merge sort and insertion sort,
    designed to perform well on many kinds of real-world data.

    Parameters
    ----------
    arr : list
        The list to be sorted.
    min_run : int, optional
        The minimum size of runs to use (default: 64).
        Performance may be tuned by adjusting this parameter.

    Returns
    -------
    list
        The sorted list.

    Examples
    --------
    >>> timsort([5, 2, 9, 1, 5, 6])
    [1, 2, 5, 5, 6, 9]
    >>> timsort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    n = len(arr)

    min_run = max(
        16, min(min_run, n)
    )

    for start in range(0, n, min_run):
        end = min(start + min_run, n)
        binary_insertion_sort(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n, left + size)
            right = min(n, left + 2 * size)

            merge(arr, left, mid, right)

        size *= 2

    return arr
