import os
import sys


def solve(src: any) -> None:
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
