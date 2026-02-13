#!/usr/bin/env python3

import random
import string
import re
from typing import List, Tuple, Set


class TestCaseGenerator:
    """Generate test cases for DSA problems."""

    def __init__(self, seed: int | None = None):
        """Initialize with optional random seed for reproducibility."""
        if seed is not None:
            random.seed(seed)

    # Numeric sequences
    def random_integers(self, n: int, a: int, b: int) -> List[int]:
        """Generate n random integers in range [a, b]."""
        return [random.randint(a, b) for _ in range(n)]

    def random_floats(self, n: int, a: float, b: float) -> List[float]:
        """Generate n random floats in range [a, b]."""
        return [random.uniform(a, b) for _ in range(n)]

    def random_permutation(self, n: int) -> List[int]:
        """Generate random permutation of numbers 1 to n."""
        seq = list(range(1, n + 1))
        random.shuffle(seq)
        return seq

    # Matrices
    def random_matrix(
        self, n: int, m: int | None = None, a: int = 1, b: int = 10
    ) -> List[List[int]]:
        """Generate n x m (or n x n) matrix with random integers in [a, b]."""
        m = m or n
        return [[random.randint(a, b) for _ in range(m)] for _ in range(n)]

    def random_matrix_zero_diagonal(
        self, n: int, a: int = 1, b: int = 10
    ) -> List[List[int]]:
        """Generate n x n matrix with zeros on diagonal, random integers elsewhere."""
        return [
            [0 if r == c else random.randint(a, b) for c in range(n)] for r in range(n)
        ]

    def random_symmetric_matrix(
        self, n: int, a: int = 1, b: int = 10
    ) -> List[List[int]]:
        """Generate symmetric n x n matrix."""
        matrix = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(r + 1):
                value = random.randint(a, b)
                matrix[r][c] = matrix[c][r] = value
        return matrix

    # Graphs and Trees
    def random_tree(self, n: int, depth: str = "shallow") -> List[Tuple[int, int]]:
        """
        Generate random tree on n vertices (0 to n-1).
        depth: "shallow" (default), "deep", or "path"
        """
        if n <= 1:
            return []

        if depth == "path":
            alpha = 0
        elif depth == "deep":
            alpha = 3
        else:  # shallow
            alpha = n  # effectively random

        return [(random.randint(max(0, i - alpha), i), i + 1) for i in range(n - 1)]

    def random_graph(self, n: int, connected: bool = False) -> Set[Tuple[int, int]]:
        """
        Generate random graph on n vertices (0 to n-1).
        If connected=True, guarantees connectivity by including a random tree.
        """
        graph = {(i, j) for i in range(n) for j in range(i) if random.randint(0, 1)}

        if connected and n > 1:
            tree = set((min(u, v), max(u, v)) for u, v in self.random_tree(n))
            graph |= tree

        return graph

    # Strings
    def random_string(self, n: int, charset: str = "ABCabc123") -> str:
        """Generate random string of length n from given charset."""
        return "".join(random.choice(charset) for _ in range(n))

    def random_string_uppercase(self, n: int) -> str:
        """Generate random uppercase string."""
        return "".join(random.choice(string.ascii_uppercase) for _ in range(n))

    def random_string_lowercase(self, n: int) -> str:
        """Generate random lowercase string."""
        return "".join(random.choice(string.ascii_lowercase) for _ in range(n))

    def random_string_alphanumeric(self, n: int) -> str:
        """Generate random alphanumeric string."""
        return "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(n)
        )

    def random_string_regex(self, n: int, pattern: str) -> str:
        """
        Generate random string matching regex pattern.
        Example: pattern = r"[A-Za-z0-9]"
        """
        regex = re.compile(pattern)
        charset = "".join(chr(c) for c in range(256) if regex.match(chr(c)))
        if not charset:
            raise ValueError(f"No characters match pattern: {pattern}")
        return "".join(random.choice(charset) for _ in range(n))

    # Output formatting
    @staticmethod
    def format_matrix(matrix: List[List[int]], separator: str = " ") -> str:
        """Format matrix as string with rows on separate lines."""
        return "\n".join(separator.join(map(str, row)) for row in matrix)


if __name__ == "__main__":
    gen = TestCaseGenerator(seed=42)
    print(gen.random_integers(10, 1, 10))
