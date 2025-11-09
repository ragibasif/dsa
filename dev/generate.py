"""
* File: main.py
* Author: Ragib Asif
* Email: ragibasif@tuta.io
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
"""

import heapq
import logging
import math
import os
import random
import sys
import time

TEST_CASES: int = 100
RANDOM_SEED: None = None


def factorial(n: int) -> int:
    return math.factorial(n)


def n_choose_k(n: int, k: int) -> int:
    return math.comb(n, k)


def matrix(
    rows: int,
    cols: int,
    fill: int | float | str | bool | bytes | bytearray | None = None,
) -> list[list[int | float | str | bool | bytes | bytearray | None]]:
    grid = [[fill for _ in range(cols)] for _ in range(rows)]
    return grid


def pascal_triangle(n: int, k: int) -> list[list[int]]:
    grid: list[list[int]] = matrix(n, k, 0)
    for row in range(n):
        for col in range(k):
            grid[row][col] = n_choose_k(row, col)
    return grid


def list_str(arr: list[object]) -> str:
    _string = [str(arr[x]) for x in range(len(arr))]
    _string = " ".join(_string)
    return _string


def list_head(arr: list[object]) -> list[object]:
    *_head, _ = arr
    return _head


def list_tail(arr: list[object]) -> list[object]:
    _, *_tail = arr
    return _tail


def int_str(
    i: int,
    representation: str = "d",
    prefix: bool = False,
    delimiter: str = "",
    sign: bool = False,
) -> str:
    representations = ["d", "n", "b", "o", "x", "X"]
    _representation = representation if representation in representations else "d"
    _prefix = "#" if prefix else ""
    delimiters = [",", "_"]
    _delimiter = delimiter if delimiter in delimiters else ""
    _sign = "+" if sign else "-"

    _string = f"{i:{_sign}{_prefix}{_delimiter}{_representation}}"
    return _string


def nlargest(n: int, nums: list[object]) -> list[object]:
    _nlargest = heapq.nlargest(n, nums)
    return _nlargest


def nsmallest(n: int, nums: list[object]) -> list[object]:
    _nsmallest = heapq.nsmallest(n, nums)
    return _nsmallest


def solve(src: object) -> None:
    # YOUR CODE HERE
    pass


class Input:
    def file_open(self) -> None:
        if os.path.exists("input.txt"):
            sys.stdin = open("input.txt", "r")
            sys.stdout = open("output.txt", "w")

    def file_close(self) -> None:
        if os.path.exists("input.txt"):
            sys.stdin.close()
            sys.stdout.close()

    def read(self) -> sys:
        return sys.stdin.readline().strip()


def test() -> None:
    input = Input()
    input.file_open()
    t = 1  # single test case
    # t = int(input.read())  # multiple test case
    for _ in range(t):
        src = input.read()  # inputs in an array
        solve(src)
    input.file_close()


def main() -> None:
    f = open("test.in", "w")
    f.write(str(TEST_CASES) + "\n")
    for _ in range(TEST_CASES // 10):
        num = random.randrange(1, TEST_CASES + 1, 1)
        nums = [x * num for x in range(1, TEST_CASES + 1)]
        f.write(str(num) + "\n")
        random.shuffle(nums)
        print(nlargest(3, nums))
        print(nsmallest(3, nums))
    f.close()


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

    main()

    # performance
    wall_clock_end = time.perf_counter()
    cpu_time_end = time.process_time()
    wall_clock_time = wall_clock_end - wall_clock_start
    cpu_time_time = cpu_time_end - cpu_time_start
    # logging
    logging.info(f"wall_clock_time: {wall_clock_time}")
    logging.info(f"cpu_time_time: {cpu_time_time}")
