def heaps_algorithm(arr):
    """Generate every possible ordering of a list (Heap's algorithm).

    This goes through all n! permutations by swapping just two elements
    at each step — no extra memory needed.

    Parameters
    ----------
    arr : list
        The list you want to permute.

    Yields
    ------
    tuple
        The next permutation of the input list.

    Examples
    --------
    >>> list(heaps_algorithm([1, 2, 3]))
    [(1, 2, 3), (2, 1, 3), (3, 1, 2), (1, 3, 2), (2, 3, 1), (3, 2, 1)]
    """
    n = len(arr)
    c = [0] * n

    yield tuple(arr)

    i = 1
    while i < n:
        if c[i] < i:
            if i & 1 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]

            yield tuple(arr)

            c[i] += 1
            i = 1
        else:
            c[i] = 0
            i += 1
