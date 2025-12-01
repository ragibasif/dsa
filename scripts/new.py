#!/usr/bin/env python3

import os

LC = "leetcode"
LC_DIF = {"easy", "medium", "hard"}

AOC = "advent_of_code"
AOC_DAYS = [n + 1 for n in range(25)]


HELP = """
=== DSA Solution Organizer ===

PLATFORMS:
    - LeetCode (lc)
    - Codeforces (cf)
    - Advent of Code (aoc)
    - Code Submission Evaluation System (cses)

DIFFICULTY LEVELS BY PLATFORM:

    LeetCode (lc):
        - easy (e)
        - medium (m)
        - hard (h)

    Codeforces (cf):
        - A, B, C, D, E, F (or custom rating)

    Advent of Code (aoc):
        - part_1
        - part_2

    Code Submission Evaluation System (cses):
        - unk (unknown/unrated)
        - introductory
        - graph
        - dp
        - range_queries
        - trees
        - advanced

PROBLEM NAME:

PROBLEM ID:

URL:

EXAMPLE USAGE:
    Platform: lc
    Difficulty: medium
    Problem name: two_sum
    Problem ID: 1
    URL: https://leetcode.com/problems/two-sum/

    Result: lc/medium/1_two_sum.py

NOTES:
    - Problem names should be lowercase with underscores
    - Directory structure: platform/difficulty/id_problem.py
    - Each solution file includes a header with metadata
"""


def create_solution_file(platform, difficulty, problem, problem_id, url):
    """Create directory structure and file for solution"""
    dir_path = os.path.join(platform, difficulty)
    os.makedirs(dir_path, exist_ok=True)

    filename = os.path.join(dir_path, f"{problem_id}_{problem}.py")

    # Create file with template
    with open(filename, "w") as f:
        f.write(f"# Problem: {problem}\n")
        f.write(f"# ID: {problem_id}\n")
        f.write(f"# URL: {url}\n\n")


def main():
    print(HELP)

    platform = input("Platform (lc/cf/aoc/cses): ")
    difficulty = input("Difficulty: ")
    problem = input("Problem name: ")
    problem_id = input("Problem ID: ")
    url = input("URL: ")

    # create_solution_file(platform, difficulty, problem, problem_id, url)
    print(platform, difficulty, problem, problem_id, url)


if __name__ == "__main__":
    main()
