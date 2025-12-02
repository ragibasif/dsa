#!/usr/bin/env python3

import os

LEETCODE = "leetcode"
LEETCODE_URL = "https://leetcode.com/problemset/"

LEETCODE_DIFFICULTY = ["easy", "medium", "hard"]

DEFAULT_FILE = "README.md"


def leetcode_dir():
    for diff in LEETCODE_DIFFICULTY:
        dir_path = os.path.join(LEETCODE, diff)
        os.makedirs(dir_path, exist_ok=True)
        filename = os.path.join(dir_path, DEFAULT_FILE)
        url = f"{LEETCODE_URL}"
        with open(filename, "w") as f:
            f.write(f"# {dir_path}\n\n")
            f.write(f"Link: [{url}]({url})\n\n")


def main():
    leetcode_dir()


if __name__ == "__main__":
    main()
