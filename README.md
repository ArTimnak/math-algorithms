# math-algorithms

I'm a student learning math and programming, and this repo is where I implement algorithms and concepts I come across — mostly in **combinatorics**, but I'll throw in anything I find interesting.

## Repository Structure

```
math-algorithms/
├── combinatorics/          # Main focus: combinatorial algorithms
│   ├── core/               # Enumerative combinatorics
│   ├── graph/              # Graph enumeration
│   ├── design/             # Combinatorial designs
│   └── advanced/           # Advanced topics
├── algorithms/             # General algorithms
├── docs/                   # Documentation/Tutorials
├── examples/               # Example scripts
├── notebooks/              # Jupyter notebooks
├── tests/                  # Tests
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

### How I'm Writing Things

- One file per concept — e.g., `permutations.py` for permutation algorithms.
- Use generators for combinatorial generation (lazy evaluation saves memory).
- Prefer dependency-free code; use `sympy` or `numpy` only when it simplifies things.

> All commit messages in this repo are AI-generated.

License: MIT — see [LICENSE](LICENSE).
