"""
* File: utils.py
* Author: Ragib Asif
* Email: ragibasif@tuta.io
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
"""

import logging
import math
import os
import random
import sys
import time
import collections
import itertools

################################################################################
# CONSTANTS
################################################################################

TEST_CASES: int = 100
RANDOM_SEED: None = None

ROMAN_NUMERALS: dict[int, tuple[str, str]] = {
    1: ("I", "i"),
    4: ("IV", "iv"),
    5: ("V", "v"),
    9: ("IX", "ix"),
    10: ("X", "x"),
    40: ("XL", "xl"),
    50: ("L", "l"),
    90: ("XC", "xc"),
    100: ("C", "c"),
    400: ("CD", "cd"),
    500: ("D", "d"),
    900: ("CM", "cm"),
    1000: ("M", "m"),
}

ROMAN_NUMERALS_UPPER: dict[int, str] = {
    key: value[0] for key, value in ROMAN_NUMERALS.items()
}

ROMAN_NUMERALS_LOWER: dict[int, str] = {
    key: value[1] for key, value in ROMAN_NUMERALS.items()
}

ALPHABET_FULL: dict[int, tuple[dict[int, str], dict[int, str]]] = {
    i: ({ord("A") + i: chr(ord("A") + i)}, {ord("a") + i: chr(ord("a") + i)})
    for i in range(26)
}

ALPHABET_LOWER: dict[int, str] = {ord("a") + i: chr(ord("a") + i) for i in range(26)}
ALPHABET_UPPER: dict[int, str] = {ord("A") + i: chr(ord("A") + i) for i in range(26)}

UINT8_MIN: int = 0
UINT8_MAX: int = (1 << 8) - 1
UINT16_MIN: int = 0
UINT16_MAX: int = (1 << 16) - 1
UINT32_MIN: int = 0
UINT32_MAX: int = (1 << 32) - 1
UINT64_MIN: int = 0
UINT64_MAX: int = (1 << 64) - 1
UINT128_MIN: int = 0
UINT128_MAX: int = (1 << 128) - 1
INT8_MIN: int = -1 << 7
INT8_MAX: int = (1 << 7) - 1
INT16_MIN: int = -1 << 15
INT16_MAX: int = (1 << 15) - 1
INT32_MIN: int = -1 << 31
INT32_MAX: int = (1 << 31) - 1
INT64_MIN: int = -1 << 63
INT64_MAX: int = (1 << 63) - 1
INT128_MIN: int = -1 << 127
INT128_MAX: int = (1 << 127) - 1

ZERO: int = 0
SIZE: int = 1 << 7
HALF: float = 0.5


###############################################################################
# HELPERS
###############################################################################


def int_to_roman(n: int) -> str:
    values = sorted(
        [key for key, _ in ROMAN_NUMERALS.items()], reverse=True
    )  # descending order
    roman = ""
    _n = n
    for i in range(len(values)):
        while _n >= values[i]:
            roman += ROMAN_NUMERALS_UPPER[values[i]]
            _n -= values[i]
    return roman


def combinations(iterable, k):
    _map = {"iterable": iterable, "n": len(iterable), "k": k}
    _combinations = [c for c in itertools.combinations(iterable, k)]
    return [_map] + _combinations


def permutations(iterable, k=None):
    _map = {"iterable": iterable, "n": len(iterable), "k": k}
    __permutations = [p for p in itertools.permutations(iterable, k)]
    return [_map] + __permutations


def frequency(iterable):
    _counter = collections.Counter(iterable)
    return _counter


def gen_pascal_triangle(n, k):
    return [[math.comb(row, col) for col in range(k)] for row in range(n)]


def gen_grid(n, m):
    return [[0 for col in range(m)] for row in range(n)]


SIGNED = [x for x in range(INT8_MIN, INT8_MAX)]
UNSIGNED = [x for x in range(UINT8_MIN, UINT8_MAX)]
UPPERS = [chr(x) for x in range(ord("A"), ord("Z") + 1)]
LOWERS = [chr(x) for x in range(ord("a"), ord("z") + 1)]
DIGITS = [chr(x) for x in range(ord("0"), ord("9") + 1)]

_squares = lambda size: [n * n for n in range(size)]
_sqrt = lambda size: [math.sqrt(n) for n in range(size)]
_odds = lambda size: [x for x in range(size) if (lambda x: x & 1)(x)]
_evens = lambda size: [x for x in range(size) if (lambda x: not x & 1)(x)]
_nums = lambda size: [n for n in range(size)]
_complement = lambda size: [~n for n in range(size)]
_even = lambda n: n & 0 == 0
_odd = lambda n: n & 1 == 1
_sum = lambda *a: sum(a)
# _grid = lambda row, col, fill: [[fill for _ in range(col)] for _ in range(row)]


print(gen_pascal_triangle(10, 10))


def int_str(
    i,
    specifier="d",
    prefix=False,
    delimiter="",
    sign=False,
):
    specifiers = ["d", "n", "b", "o", "x", "X"]
    _specifier = specifier if specifier in specifiers else "d"
    _prefix = "#" if prefix else ""
    delimiters = [",", "_"]
    _delimiter = delimiter if delimiter in delimiters else ""
    _sign = "+" if sign else "-"

    _string = f"{i:{_sign}{_prefix}{_delimiter}{_specifier}}"
    return _string


def gen_random_int_list(
    seed=RANDOM_SEED, a: int = INT32_MIN, b: int = INT32_MAX
) -> list[int]:
    random.seed(seed)
    _len = gen_random_int(seed, ZERO, SIZE)
    _list: list[int] = [(gen_random_int(seed, a, b)) for _ in range(_len)]
    return _list


def gen_random_int(seed=RANDOM_SEED, a: int = INT32_MIN, b: int = INT32_MAX):
    random.seed(seed)
    return random.randint(a, b)


def gen_random_float(seed=RANDOM_SEED) -> float:
    random.seed(seed)
    return random.random()


def gen_random_bool(seed=RANDOM_SEED) -> bool:
    random.seed(seed)
    return random.choice([True, False])


def gen_random_graph(
    seed=RANDOM_SEED,
    vertices: int = SIZE,
    probability: float = HALF,
    directed: bool = False,
):
    """
    Generate a random graph
    @input: vertices_number (number of vertices),
            probability (probability that a generic edge (u,v) exists),
            directed (if True: graph will be a directed graph,
                      otherwise it will be an undirected graph)
    @examples:
    >>> gen_random_graph(1,4, 0.5)
    {0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}
    >>> gen_random_graph(1,4, 0.5, True)
    {0: [1], 1: [2, 3], 2: [3], 3: []}
    """
    random.seed(seed)
    _graph: dict[int, list[int]] = {v: [] for v in range(vertices)}
    # if probability is greater or equal than 1, then generate a complete graph
    if probability >= 1:
        return gen_complete_graph(vertices)
    # if probability is lower or equal than 0, then return a graph without edges
    if probability <= 0:
        return _graph

    # for each couple of nodes, add an edge from u to v
    # if the number randomly generated is greater than probability probability
    for i in range(vertices):
        for j in range(i + 1, vertices):
            if random.random() < probability:
                _graph[i].append(j)
                if not directed:
                    # if the graph is undirected, add an edge in from j to i, either
                    _graph[j].append(i)
    return _graph


def gen_complete_graph(vertices: int) -> dict[int, list[int]]:
    """
    Generate a complete graph with vertices_number vertices.
    @input: vertices_number (number of vertices),
            directed (False if the graph is undirected, True otherwise)
    @example:
    >>> gen_complete_graph(3)
    {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    """
    _graph: dict[int, list[int]] = {
        i: [j for j in range(vertices) if i != j] for i in range(vertices)
    }
    return _graph


def main():
    """
    f = open("test.in", "w")
    f.write(str(TEST_CASES) + "\n")
    for _ in range(TEST_CASES // 10):
        num = random.randrange(1, TEST_CASES//10 + 1, 1)
        nums = [x * num for x in range(1, TEST_CASES//10 + 1)]
        f.write(str(num) + "\n")
        f.write(str(nums) + "\n")
    f.close()
    """
    pass


if __name__ == "__main__":
    # performance
    wall_clock_start = time.perf_counter()
    cpu_time_start = time.process_time()
    # logging
    logging.basicConfig(
        level=logging.INFO,
        style="{",
        format="[{levelname}] [{asctime}] {name} {processName}({process}) {message}",
        datefmt="%Y-%m-%d %I:%M:%S %p",
        encoding="utf-8",
    )
    # random
    random.seed(RANDOM_SEED)

    import doctest

    doctest.testmod()

    main()

    # performance
    wall_clock_end = time.perf_counter()
    cpu_time_end = time.process_time()
    wall_clock_time = wall_clock_end - wall_clock_start
    cpu_time_time = cpu_time_end - cpu_time_start
    # logging
    logging.info(f"wall_clock_time: {wall_clock_time}")
    logging.info(f"cpu_time_time: {cpu_time_time}")
