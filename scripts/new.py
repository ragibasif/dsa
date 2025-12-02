#!/usr/bin/env python3

import os
import datetime

LC = "lc"
CF = "cf"
AOC = "aoc"
CSES = "cses"


PLATFORMS = {LC, CF, AOC, CSES}

README = "README.md"

DATE_TIME = datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p")


def leetcode():
    lc_diff = {"easy", "medium", "hard"}
    prob_diff = input("Difficulty (easy/medium/hard): ")
    while prob_diff not in lc_diff:
        print("Must be one of:")
        for item in lc_diff:
            print(item)
        prob_diff = input("Difficulty (easy/medium/hard): ")
    prob_name = input("Problem name (two_sum/3sum/remove_element): ")
    pid = int(input("Problem ID (1,423,23): "))
    pid_str = f"{pid:04d}"
    url = input("Problem URL: ")

    prob_dir_title = f"{pid_str}_{prob_name}"
    dir_path = os.path.join("leetcode", prob_diff, prob_dir_title)
    os.makedirs(dir_path, exist_ok=True)
    filename = os.path.join(dir_path, README)

    if os.path.exists(filename):
        with open(filename, "a") as f:
            f.write(f"- {DATE_TIME}\n")
    else:
        with open(filename, "a") as f:
            f.write(f"# {pid_str}_{prob_name}\n\n")
            f.write(f"Link: [{pid_str}_{prob_name}]({url})\n\n")
            f.write(f"- {DATE_TIME}\n")
    print(f"{filename}")


def aoc():
    aoc_start_year = 2015
    aoc_current_year = datetime.datetime.now().year
    aoc_days_total = 25

    aoc_years = set([n for n in range(aoc_start_year, aoc_current_year + 1)])
    aoc_days = set([n for n in range(1, aoc_days_total + 1)])

    year = int(input("Problem year: "))
    while year not in aoc_years:
        print(f"Must be one of {sorted(list(aoc_years))}")
        year = int(input("Problem year: "))

    day = int(input("Problem day: "))
    while day not in aoc_days:
        print(f"Must be one of {sorted(list(aoc_days))}")
        day = int(input("Problem day: "))

    url = input("Problem URL: ")

    dir_path = os.path.join(AOC, str(year), f"{day:02d}")
    os.makedirs(dir_path, exist_ok=True)
    filename = os.path.join(dir_path, README)

    if os.path.exists(filename):
        with open(filename, "a") as f:
            f.write(f"- {DATE_TIME}\n")
    else:
        with open(filename, "a") as f:
            f.write(f"# {year}_{day}\n\n")
            f.write(f"Link: [{year}_{day}]({url})\n\n")
            f.write(f"- {DATE_TIME}\n")
    print(f"{filename}")


def cses():
    cses_cats = set(
        [
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
    )

    category = input("Problem category: ")
    while category not in cses_cats:
        print("Must be one of:")
        for row in cses_cats:
            print(row)
        category = input("Problem category: ")
    title = input("Problem title: ")

    url = input("Problem URL: ")

    dir_path = os.path.join(CSES, category, title)
    os.makedirs(dir_path, exist_ok=True)
    filename = os.path.join(dir_path, README)

    if os.path.exists(filename):
        with open(filename, "a") as f:
            f.write(f"- {DATE_TIME}\n")
    else:
        with open(filename, "a") as f:
            f.write(f"# {category}_{title}\n\n")
            f.write(f"Link: [{category}_{title}]({url})\n\n")
            f.write(f"- {DATE_TIME}\n")
    print(f"{filename}")


def codeforces():
    levels = set([chr(i) for i in range(ord("A"), ord("Z") + 1)])
    level = input("Problem level: ")
    while level not in levels:
        print(f"Must be one of {sorted(list(levels))}")
        level = input("Problem level: ")
    prob_name = input("Problem title: ")
    pid = int(input("Problem ID: "))
    pid_str = f"{pid:05d}"
    url = input("Problem URL: ")

    prob_dir_title = f"{pid_str}_{prob_name}"
    dir_path = os.path.join("codeforces", level, prob_dir_title)
    os.makedirs(dir_path, exist_ok=True)
    filename = os.path.join(dir_path, README)

    if os.path.exists(filename):
        with open(filename, "a") as f:
            f.write(f"- {DATE_TIME}\n")
    else:
        with open(filename, "a") as f:
            f.write(f"# {prob_dir_title}\n\n")
            f.write(f"Link: [{prob_dir_title}]({url})\n\n")
            f.write(f"- {DATE_TIME}\n")
    print(f"{filename}")


def main():
    platform = input("Platform (lc/cf/aoc/cses): ")
    while platform not in PLATFORMS:
        platform = input("Platform (lc/cf/aoc/cses): ")
    if platform == LC:
        leetcode()
    elif platform == CF:
        codeforces()
    elif platform == AOC:
        aoc()
    elif platform == CSES:
        cses()
    else:
        exit(1)


if __name__ == "__main__":
    main()
