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


def ensure_str_collection(collection):
    """Convert all elements in a collection to strings."""
    if isinstance(collection, dict):
        return {str(k): str(v) for k, v in collection.items()}
    elif isinstance(collection, set):
        return {str(item) for item in collection}
    elif isinstance(collection, (list, tuple)):
        return [str(item) for item in collection]
    return collection


def validate_input(prompt, valid_options, display_name="options"):
    """Get and validate user input against a set of valid options."""
    valid_options = ensure_str_collection(valid_options)
    user_input = input(prompt)
    while user_input not in valid_options:
        print(f"Must be one of {sorted(list(valid_options))}")
        user_input = input(prompt)
    return user_input


def write_readme(filepath, header, link_text, url):
    """Write or append to a README file."""
    if os.path.exists(filepath):
        with open(filepath, "a") as f:
            f.write(f"- {DATE_TIME}\n")
    else:
        with open(filepath, "a") as f:
            f.write(f"# {header}\n\n")
            f.write(f"Link: [{link_text}]({url})\n\n")
            f.write(f"- {DATE_TIME}\n")


def create_problem_dir(base_path, problem_info):
    """Create problem directory and README file."""
    dir_path = os.path.join(base_path, *problem_info["path_parts"])
    os.makedirs(dir_path, exist_ok=True)
    filename = os.path.join(dir_path, README)

    write_readme(
        filename, problem_info["header"], problem_info["link_text"], problem_info["url"]
    )
    print(filename)


def leetcode():
    difficulties = {"easy", "medium", "hard"}
    difficulty = validate_input("Difficulty (easy/medium/hard): ", difficulties)
    prob_name = input("Problem name (two_sum/3sum/remove_element): ")
    pid = int(input("Problem ID (1,423,23): "))
    pid_str = f"{pid:04d}"
    url = input("Problem URL: ")

    problem_info = {
        "path_parts": [difficulty, f"{pid_str}_{prob_name}"],
        "header": f"{pid_str}_{prob_name}",
        "link_text": f"{pid_str}_{prob_name}",
        "url": url,
    }
    create_problem_dir("leetcode", problem_info)


def codeforces():
    levels = {chr(i) for i in range(ord("A"), ord("Z") + 1)}
    level = validate_input("Problem level: ", levels)
    prob_name = input("Problem title: ")
    pid = int(input("Problem ID: "))
    pid_str = f"{pid:05d}"
    url = input("Problem URL: ")

    prob_dir_title = f"{pid_str}_{prob_name}"
    problem_info = {
        "path_parts": [level, prob_dir_title],
        "header": prob_dir_title,
        "link_text": prob_dir_title,
        "url": url,
    }
    create_problem_dir("codeforces", problem_info)


def aoc():
    start_year = 2015
    current_year = datetime.datetime.now().year
    years = set(range(start_year, current_year + 1))
    days = set(range(1, 26))

    year = int(validate_input("Problem year: ", years))
    day = int(validate_input("Problem day: ", days))
    url = input("Problem URL: ")

    problem_info = {
        "path_parts": [str(year), f"{day:02d}"],
        "header": f"{year}_{day}",
        "link_text": f"{year}_{day}",
        "url": url,
    }
    create_problem_dir("aoc", problem_info)


def cses():
    categories = {
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
    }

    category = validate_input("Problem category: ", categories)
    title = input("Problem title: ")
    url = input("Problem URL: ")

    problem_info = {
        "path_parts": [category, title],
        "header": f"{category}_{title}",
        "link_text": f"{category}_{title}",
        "url": url,
    }
    create_problem_dir("cses", problem_info)


def main():
    platform_map = {LC: leetcode, CF: codeforces, AOC: aoc, CSES: cses}

    platform = validate_input("Platform (lc/cf/aoc/cses): ", PLATFORMS)
    platform_map[platform]()


if __name__ == "__main__":
    main()
