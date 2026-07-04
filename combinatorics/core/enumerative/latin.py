def cyclic_latin_square(n):
    """Return a generator that yields rows of an n×n cyclic Latin square.

    Each row is generated using: row i = [(i + 0) % n + 1, ..., (i + (n-1)) % n + 1]

    Parameters
    ----------
    n : int
        Size of the square (must be positive)

    Yields
    ------
    list[int]
        One row of the Latin square

    Examples
    --------
    >>> list(cyclic_latin_square(3))
    [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    """
    if n <= 0:
        return

    for i in range(n):
        yield [(i + j) % n + 1 for j in range(n)]
