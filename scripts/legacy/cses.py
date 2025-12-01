#!/usr/bin/env python3

import os

CSES = "cses"
CSES_URL = "https://cses.fi/problemset/"

CSES_CAT = [
    "introductory_problems",
    "sorting_and_searching",
    "dynamic_programming",
    "graph_algorithms",
    "range_queries",
    "tree_algorithms",
    "mathematics",
    "string_algorithms",
    "geometry",
    "advanced_techniques",
    "sliding_window_problems",
    "interactive_problems",
    "bitwise_operations",
    "construction_problems",
    "advanced_graph_problems",
    "counting_problems",
    "additional_problems_i",
    "additional_problems_ii",
]

DEFAULT_FILE = "README.md"


def cses_dir():
    for cat in CSES_CAT:
        dir_path = os.path.join(CSES, cat)
        os.makedirs(dir_path, exist_ok=True)
        filename = os.path.join(dir_path, DEFAULT_FILE)
        url = f"{CSES_URL}"
        with open(filename, "w") as f:
            f.write(f"# {dir_path}\n\n")
            f.write(f"Link: [{url}]({url})\n\n")


def main():
    cses_dir()


if __name__ == "__main__":
    main()
