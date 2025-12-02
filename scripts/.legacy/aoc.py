#!/usr/bin/env python3

import os
import datetime

AOC_BASE = "adventofcode"
AOC_ABBR = "aoc"
AOC_START_YEAR = 2015
AOC_CURRENT_YEAR = datetime.datetime.now().year
AOC_DAYS = 25
AOC_URL = "https://adventofcode.com"

DEFAULT_FILE = "README.md"


def aoc_dir():
    for year in range(AOC_START_YEAR, AOC_CURRENT_YEAR + 1):
        year_str = str(year)
        parent_dir_path = os.path.join(AOC_ABBR, year_str)
        os.makedirs(parent_dir_path, exist_ok=True)
        parent_filename = os.path.join(parent_dir_path, DEFAULT_FILE)
        parent_url = f"{AOC_URL}/{year}"
        with open(parent_filename, "w") as f:
            f.write(f"# {parent_dir_path}\n\n")
            f.write(f"Link: [{parent_url}]({parent_url})\n\n")
            f.write("## Stars\n\n")
            for i in range(AOC_DAYS):
                f.write(f"{i + 1}. Day {i + 1}\n")
                f.write("\t- [ ] part_one\n")
                f.write("\t- [ ] part_two\n")
        for day in range(1, AOC_DAYS + 1):
            day_str = f"{day:02d}"
            dir_path = os.path.join(AOC_ABBR, year_str, day_str)
            os.makedirs(dir_path, exist_ok=True)
            filename = os.path.join(dir_path, DEFAULT_FILE)
            url = f"{AOC_URL}/{year}/day/{day}"
            with open(filename, "w") as f:
                f.write(f"# {dir_path}\n\n")
                f.write(f"Link: [{url}]({url})\n\n")


def main():
    aoc_dir()


if __name__ == "__main__":
    main()
