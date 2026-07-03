# math-algorithms

I'm a student learning math and programming, and this repo is where I implement algorithms and concepts I come across — mostly in **combinatorics**, but I'll throw in anything I find interesting.

## What's where in combinatorics

| Sub-package       | Stuff I've been playing with                                      |
|-------------------|-------------------------------------------------------------------|
| `enumerative`     | Permutations, combinations, partitions, special numbers, tableaux |
| `graph_theory`    | Trees, matchings, colorings, Ramsey theory, network flows         |
| `design_theory`   | BIBDs, projective planes, Latin squares, Sudoku                   |

### How I'm writing things

- One file per concept — `permutations.py` has permutation stuff, `primes.py` has prime stuff.
- Generators for combinatorial generation (lazy, saves memory).
- I try to keep it dependency-free where I can, but I'll use `sympy` or `numpy` when it makes life easier.
- Tests go in `tests/` following the same folder structure.

## License

See [LICENSE](LICENSE).
