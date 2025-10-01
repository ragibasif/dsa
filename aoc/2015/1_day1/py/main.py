"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 1 - day1
* Platform: aoc
* Difficulty: 2015
* URL: https://adventofcode.com/2015/day/1
"""

import bisect  # bisect_left, bisect_right, insort
import collections  # Counter, defaultdict, deque, namedtuple
import functools
import heapq  # heapify, heappop, heappush, nlargest, nsmallest
import itertools
import math
import operator
import os
import random
import re
import string
import sys


def solve(src: any) -> None:
    # ( - add 1
    # ) - sub 1
    floor = 0
    for item in src:
        if item == "(":
            floor += 1
        else:
            floor -= 1
    print(floor)


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


def main() -> None:
    input = Input()
    input.file_open()
    t = 1  # single test case
    # t = int(input.read())  # multiple test case
    for _ in range(t):
        src = input.read()  # inputs in an array
        solve(src)
    input.file_close()


if __name__ == "__main__":
    main()
