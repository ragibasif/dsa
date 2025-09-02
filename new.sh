#!/bin/sh
# File: new.sh
# Author: Ragib Asif
# GitHub: https://github.com/ragibasif
# LinkedIn: https://www.linkedin.com/in/ragibasif/
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Ragib Asif

# set -Ceuvx
# set -n # debugging

RED='\033[0;91m'
GREEN='\033[92m'
CYAN='\033[96m'
BOLD='\033[1m'
RESET='\033[0m' # No Color
ERROR="${BOLD}${RED}ERROR${RESET}"
SUCCESS="${BOLD}${GREEN}SUCCESS${RESET}"

# gum: https://github.com/charmbracelet/gum
if ! command -v gum >/dev/null 2>&1; then
    msg1="This script requires gum but gum is not installed."
    msg2="To learn more about gum, visit 'https://github.com/charmbracelet/gum'."
    msg3="Aborting."
    echo "$ERROR $msg1"
    printf '%s\n' "$msg2"
    echo "$msg3" >&2
    exit 1
fi

PLATFORM=""
PROBLEM_ID=""
PROBLEM_NAME=""
DIFFICULTY=""
LANGUAGE=""
URL=""

PLATFORM_DIR=""
CATEGORY_DIR=""
FILE_DIR=""
FILE_PATH=""
TEMPLATE_DIR=""
TEMPLATE_FILE=""
TEMPLATE_BUILD=""

QUES_PLAT="What is the platform?"
QUES_DIFF="What is the difficulty?"
QUES_PID="What is the problem ID?"
QUES_PNAME="What is the problem name?"
QUES_PLANG="What is the programming language used?"
QUES_PURL="What is the problem URL?"

set_platform() {
    echo "$QUES_PLAT"
    PLATFORM=$(gum choose codeforces cses leetcode)
}

set_language() {
    echo "$QUES_PLANG"
    LANGUAGE=$(gum choose cpp py)
}

set_url() {
    echo "$QUES_PURL"
    URL=$(gum input)
}

leetcode() {
    echo "$QUES_DIFF"
    DIFFICULTY=$(gum choose easy medium hard)
    echo "$QUES_PID"
    PROBLEM_ID=$(gum input --placeholder "0001, 0173, 1129, 2000, etc.")
    echo "$QUES_PNAME"
    PROBLEM_NAME=$(gum input --placeholder "two_sum, 3sum, spiral_matrix, etc.")
}

codeforces() {
    echo "$QUES_DIFF"
    DIFFICULTY=$(gum choose 0800 0900 1000 1100 1200 1300 1400 1500 1600 1700 1800 1900 2000 2100 2200 2300 2400 2500 2600 2700 2800 2900 3000 3100 3200 3300 3400 3500 3600 3700 3800 3900 4000)
    echo "$QUES_PID"
    PROBLEM_ID=$(gum input --placeholder "2116B, 1110C, 0001A, 0249D, etc.")
    echo "$QUES_PNAME"
    PROBLEM_NAME=$(gum input --placeholder "vanya_and_fence, faculty, melody, racing, etc.")
}

cses() {
    echo "$QUES_DIFF"
    DIFFICULTY=$(gum choose "introductory" "sorting_and_searching" "dynamic_programming" "graph_algorithms" "range_queries" "tree_algorithms" "mathematics" "string_algorithms" "geometry" "advanced_techniques" "sliding_window" "interactive" "bitwise_operations" "construction" "advanced_graph" "counting" "additional_1" "additional_2")
    echo "$QUES_PID"
    PROBLEM_ID=$(gum input --placeholder "1068, 1083, 1069, 1094, etc.")
    echo "$QUES_PNAME"
    PROBLEM_NAME=$(gum input --placeholder "weird_algorithm, missing_number, repetitions, two_sets, etc.")
}

eval_platform() {
    case "$PLATFORM" in
    "leetcode")
        leetcode
        ;;
    "codeforces")
        codeforces
        ;;
    "cses")
        cses
        ;;
    *)
        gum log --time kitchen --structured --level error "Platform is not supported." name "$PLATFORM"
        exit 1
        ;;
    esac
}

edit_file() {
    $EDITOR "$FILE_PATH"
}

create_path() {
    PLATFORM_DIR="$PWD/${PLATFORM}"
    CATEGORY_DIR="${PLATFORM_DIR}/${DIFFICULTY}"
    FILE_DIR="${CATEGORY_DIR}/${PROBLEM_ID}_${PROBLEM_NAME}/${LANGUAGE}"
    FILE_PATH="${FILE_DIR}/main.${LANGUAGE}"
    if [ -e "$FILE_PATH" ]; then
        edit_file
    fi
    TEMPLATE_DIR="$PWD/template.${LANGUAGE}"
    TEMPLATE_FILE="${TEMPLATE_DIR}/main.${LANGUAGE}"
    TEMPLATE_BUILD="${TEMPLATE_DIR}/Makefile"
}

metadata() {
    cat >>"$FILE_PATH" <<EOF
 * File: main.${LANGUAGE}
 * Author: Ragib Asif
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 *
 * Problem: ${PROBLEM_ID} - ${PROBLEM_NAME}
 * Platform: ${PLATFORM}
 * Difficulty: ${DIFFICULTY}
 * URL: ${URL}
EOF
}

py() {
    echo "\"\"\"" >>"$FILE_PATH"
    metadata
    echo "\"\"\"" >>"$FILE_PATH"
}

cpp() {
    echo "/*" >>"$FILE_PATH"
    metadata
    echo " */" >>"$FILE_PATH"
}

create_file() {
    mkdir -p "$FILE_DIR"
    touch "$FILE_PATH"
    if [ "$LANGUAGE" = "py" ]; then
        py
    else
        cpp
    fi
    if [ "$PLATFORM" = "leetcode" ]; then
        return
    fi
    cat "$TEMPLATE_FILE" >>"$FILE_PATH"
    cp "$TEMPLATE_BUILD" "$FILE_DIR"

    gum spin --spinner dot --title "Creating $FILE_PATH" -- sleep 1
    echo "$SUCCESS $CYAN$FILE_PATH$RESET is created!"
}

main() {
    set_platform
    eval_platform
    set_language
    set_url
    create_path
    create_file
    edit_file
}

main

exit 0
