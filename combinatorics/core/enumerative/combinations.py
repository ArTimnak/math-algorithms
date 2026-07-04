def lexicographic_combinations(n, k):
    """Generate every k-element subset of {0, 1, ..., n-1}.

    This goes through all C(n,k) combinations in sorted order by
    figuring out the next combination from the current one — no
    recursion or backtracking needed.

    Parameters
    ----------
    n : int
        The size of the set to choose from.
    k : int
        The size of each subset.

    Yields
    ------
    tuple
        The next k-combination in lexicographic order.

    Examples
    --------
    >>> list(lexicographic_combinations(5, 3))
    [(0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4),
     (0, 3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
    """
    if k < 0 or k > n:
        return

    comb = list(range(k))
    yield tuple(comb)

    while True:
        i = k - 1
        while i >= 0 and comb[i] == n - k + i:
            i -= 1

        if i < 0:
            break

        comb[i] += 1

        for j in range(i + 1, k):
            comb[j] = comb[j - 1] + 1

        yield tuple(comb)
