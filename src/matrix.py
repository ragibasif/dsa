#!/usr/bin/env python3

import sys
from utils import trace, benchmark, report, inspect

ROWS = 5
COLS = 5

matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
dist = [[float("inf") for _ in range(COLS)] for _ in range(ROWS)]
grid = [[(r * COLS + c) for c in range(COLS)] for r in range(ROWS)]
table = [[(i + 1) * (j + 1) for j in range(COLS)] for i in range(ROWS)]


@benchmark
def debug_matrix(matrix, width=5):
    if not matrix or not matrix[0]:
        print("Empty", file=sys.stderr)
        return

    R = len(matrix)
    C = len(matrix[0])

    print(f"\n({R}x{C})", file=sys.stderr)

    # Create Column Header (0, 1, 2...)
    col_header = " " * 4 + "".join(f"{c:>{width}}" for c in range(C))
    print(col_header, file=sys.stderr)
    print(" " * 3 + "+" + "-" * (C * width), file=sys.stderr)

    for r in range(R):
        row_str = f"{r:2d} |"
        for c in range(C):
            val = matrix[r][c]
            char = "." if val is None else str(val)
            if len(char) > width - 1:
                char = char[: width - 2] + "+"
            row_str += f"{char:>{width}}"
        print(row_str, file=sys.stderr)
    print(" " * 3 + "+" + "-" * (C * width) + "\n", file=sys.stderr)


def main():
    debug_matrix(matrix)
    debug_matrix(visited, 8)
    debug_matrix(dist)
    debug_matrix(grid)
    debug_matrix(table)


if __name__ == "__main__":
    main()
