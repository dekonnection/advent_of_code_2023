#!/usr/bin/env python3
import logging
import re
import math
import sys
import collections

PAYLOAD = sys.argv[1]


values = []
with open(PAYLOAD) as f:
    for _line in f:
        values.append([int(value) for value in re.findall("[\-0-9]+", _line)])


def part1(values):
    return sum([find_next_number(history) for history in values])


def find_next_number(suite):
    derivative = [suite[n + 1] - suite[n] for n in range(len(suite) - 1)]
    if len(list(collections.Counter(derivative))) == 1:
        return suite[-1] + derivative[0]
    else:
        return suite[-1] + find_next_number(derivative)


def part2(values):
    return sum([find_previous_number(history) for history in values])


def find_previous_number(suite):
    derivative = [suite[n + 1] - suite[n] for n in range(len(suite) - 1)]
    if len(list(collections.Counter(derivative))) == 1:
        return suite[0] - derivative[0]
    else:
        return suite[0] - find_previous_number(derivative)


if __name__ == "__main__":
    # logging configuration
    # log_level = "INFO"
    log_level = "DEBUG"
    logging.basicConfig(
        level=logging.getLevelName(log_level),
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    part1_result = part1(values)
    part2_result = part2(values)

    print(f"Result for part 1: {part1_result}")
    print(f"Result for part 2: {part2_result}")
