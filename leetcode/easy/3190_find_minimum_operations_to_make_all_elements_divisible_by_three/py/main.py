"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 3190 - find_minimum_operations_to_make_all_elements_divisible_by_three
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/
"""

import functools
import itertools
import math
import operator
import random
import re
import string
import sys
from bisect import bisect_left, bisect_right, insort
from collections import Counter, defaultdict, deque, namedtuple
from heapq import heapify, heappop, heappush, nlargest, nsmallest
from os import path
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            count += min(i % 3, abs(3 - (i % 3)))
        return count
