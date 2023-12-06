#!/usr/bin/env python3
import logging
import re
import math


def part1():
    numbers = []
    with open("payload.txt") as f:
        for line in f:
            numbers.append(re.findall("[0-9]+", line))

    wins_product = 1
    for race in range(0, len(numbers[0])):
        time = int(numbers[0][race])
        record_distance = int(numbers[1][race])
        logging.debug(
            f"Doing race {race} with total time {time}ms and record distance {record_distance}mm."
        )
        winning_pushes = 0
        for button_push in range(1, time):
            distance = (time - button_push) * button_push
            if distance > record_distance:
                winning_pushes += 1
            logging.debug(
                f"Race {race}: pushed button for {button_push}ms, reached {distance}mm"
            )
        wins_product = wins_product * winning_pushes

    return wins_product


# worked with the previous brute-force algorithm, but ~18s on a M1 Pro, meh.
# now sub-0.05s using college maths
def part2():
    numbers = []
    with open("payload.txt") as f:
        for line in f:
            numbers.append(int("".join(re.findall("[0-9]+", line))))

    time = numbers[0]
    record_distance = numbers[1]

    # we want the solutions to: (time - x) * x  > record_distance
    # which is equivalent to: -x^2 + time*x - record_distance > 0 (polynomial of degree 2)
    sqrt_delta = math.sqrt(time**2 - 4 * record_distance)
    winning_start = math.ceil((-record_distance + sqrt_delta) / -2)
    winning_end = math.ceil((-record_distance - sqrt_delta) / -2)

    return winning_end - winning_start + 1


if __name__ == "__main__":
    # logging configuration
    log_level = "INFO"
    # log_level = "DEBUG"
    logging.basicConfig(
        level=logging.getLevelName(log_level),
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    print(f"Result for part 1: {part1()}")
    print(f"Result for part 2: {part2()}")
