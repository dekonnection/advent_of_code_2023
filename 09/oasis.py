#!/usr/bin/env python3
import logging
import re
import math
import sys
import collections

PAYLOAD = sys.argv[1]


def part1():
    values = []
    with open(PAYLOAD) as f:
        for _line in f:
            values.append([int(value) for value in re.findall("[\-0-9]+", _line)])

    return sum([do_stuff(history) for history in values])


def do_stuff(suite):
    derivative = [suite[n + 1] - suite[n] for n in range(len(suite) - 1)]
    unique_elements = list(collections.Counter(derivative))
    if len(unique_elements) == 1:
        return suite[-1] + derivative[0]
    else:
        return suite[-1] + do_stuff(derivative)


def part2():
    values = []
    with open(PAYLOAD) as f:
        for _line in f:
            values.append([int(value) for value in re.findall("[\-0-9]+", _line)])

    return sum([do_stuff_backwards(history) for history in values])


def do_stuff_backwards(suite):
    derivative = [suite[n + 1] - suite[n] for n in range(len(suite) - 1)]
    unique_elements = list(collections.Counter(derivative))
    if len(unique_elements) == 1:
        return suite[0] - derivative[0]
    else:
        return suite[0] - do_stuff_backwards(derivative)


if __name__ == "__main__":
    # logging configuration
    # log_level = "INFO"
    log_level = "DEBUG"
    logging.basicConfig(
        level=logging.getLevelName(log_level),
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    part1_result = part1()
    part2_result = part2()

    print(f"Result for part 1: {part1_result}")
    print(f"Result for part 2: {part2_result}")
