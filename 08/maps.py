#!/usr/bin/env python3
import logging
import re
import math
import sys
import collections

PAYLOAD = sys.argv[1]


def part1():
    network = {}
    # steps = ""
    with open(PAYLOAD) as f:
        for _line in f:
            values = re.findall("[A-Z]+", _line)
            if len(values) == 3:
                network[values[0]] = (values[1], values[2])
            elif len(values) == 1:
                directions = values[0]
    step = "AAA"
    step_count = 0
    while step != "ZZZ":
        if directions[step_count % len(directions)] == "L":
            step = network[step][0]
        else:
            step = network[step][1]
        step_count += 1
    return step_count


def test():
    network = {}
    # steps = ""
    with open(PAYLOAD) as f:
        for _line in f:
            values = re.findall("[0-9A-Z]+", _line)
            if len(values) == 3:
                network[values[0]] = (values[1], values[2])
            elif len(values) == 1:
                directions = values[0]

    current_steps = [step for step in network.keys() if step[-1] == "A"]
    paths = len(current_steps)
    step_count = 0
    past_steps = []
    step = (current_steps[0], directions[0])
    print(step)
    while step not in past_steps:
        past_steps.append(step)
        direction = directions[step_count % len(directions)]
        if direction == "L":
            step = (network[step[0]][0], direction)
        else:
            step = (network[step[0]][1], direction)
        print(step)
        step_count += 1
    print(past_steps)


def part2():
    network = {}
    # steps = ""
    with open(PAYLOAD) as f:
        for _line in f:
            values = re.findall("[0-9A-Z]+", _line)
            if len(values) == 3:
                network[values[0]] = (values[1], values[2])
            elif len(values) == 1:
                directions = values[0]

    lengths = []
    for step in [step for step in network.keys() if step[-1] == "A"]:
        steps = []
        while step[-1] != "Z":
            steps.append(step)
            if directions[(len(steps) - 1) % len(directions)] == "L":
                step = network[step][0]
            else:
                step = network[step][1]
        lengths.append(len(steps))
    return int(
        math.gcd(*lengths)
        * math.prod([length / math.gcd(*lengths) for length in lengths])
    )


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
