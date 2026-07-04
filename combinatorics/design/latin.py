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


def backtrack_latin_squares(n):
    """Generate all Latin squares of order n via backtracking.

    Parameters
    ----------
    n : int
        Size of the square (must be positive)

    Yields
    ------
    list[list[int]]
        Complete Latin squares

    Examples
    --------
    >>> list(backtrack_latin_squares(2))
    [[[1, 2], [2, 1]], [[2, 1], [1, 2]]]
    """

    square = [[0] * n for _ in range(n)]

    def is_valid(row, col, num):
        for i in range(n):
            if square[row][i] == num or square[i][col] == num:
                return False
        return True

    def solve(row, col):
        if row == n:
            yield [[cell for cell in row] for row in square]
            return

        if col == n:
            yield from solve(row + 1, 0)
            return

        for num in range(1, n + 1):
            if is_valid(row, col, num):
                square[row][col] = num
                yield from solve(row, col + 1)
                square[row][col] = 0

    yield from solve(0, 0)
