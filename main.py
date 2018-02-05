#!/usr/bin/env python3

import sys


def get_info(file):
    with open(file, "r") as fd:
        content = fd.read()
    print(content)


def main():
    get_info(sys.argv[1])
    return 1

if __name__ == "__main__":
    if (len(sys.argv) == 2):
		main()
