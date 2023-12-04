#!/usr/bin/env python3
import logging
import re


## part 1 start ##
def part1():
    pile_points = 0
    with open("payload.txt") as f:
        for line in f:
            numbers = line.split(":")[1].strip().split("|")
            winning_numbers = re.findall("[0-9]+", numbers[0])
            drawn_numbers = re.findall("[0-9]+", numbers[1])
            wins = len(
                [number for number in drawn_numbers if number in winning_numbers]
            )
            card_points = 0
            if wins:
                card_points = pow(2, wins - 1)

            pile_points += card_points

    logging.debug(f"Result for part 1 is: {pile_points}")
    return pile_points


## part 1 end ##


## part 2 start ##
def part2():
    scratchcards = []
    with open("payload.txt") as f:
        for line in f:
            numbers = line.split(":")[1].strip().split("|")
            winning_numbers = re.findall("[0-9]+", numbers[0])
            drawn_numbers = re.findall("[0-9]+", numbers[1])

            wins = len(
                [number for number in drawn_numbers if number in winning_numbers]
            )
            scratchcards.append({"count": 1, "wins": wins})

    for index, card in enumerate(scratchcards):
        for _ in range(0, card["count"]):
            for card_to_copy in range(index + 1, index + 1 + card["wins"]):
                scratchcards[card_to_copy]["count"] += 1

    total_cards = sum([card["count"] for card in scratchcards])

    logging.debug(f"Result for part 2 is: {total_cards}")
    return total_cards


## part 2 end ##


if __name__ == "__main__":
    # logging configuration
    log_level = "DEBUG"
    logging.basicConfig(
        level=logging.getLevelName(log_level),
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    result_part_1 = part1()
    result_part_2 = part2()

    print(f"Result for part 1: {result_part_1}")
    print(f"Result for part 2: {result_part_2}")
