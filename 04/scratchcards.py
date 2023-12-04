#!/usr/bin/env python3
import logging
import re


def scratchcards():
    part1_pile_points = 0
    part2_scratchcards = []
    with open("payload.txt") as f:
        for line in f:
            numbers = line.split(":")[1].strip().split("|")
            winning_numbers = re.findall("[0-9]+", numbers[0])
            drawn_numbers = re.findall("[0-9]+", numbers[1])
            wins = len(
                [number for number in drawn_numbers if number in winning_numbers]
            )

            # part 1
            card_points = 0
            if wins:
                card_points = pow(2, wins - 1)

            part1_pile_points += card_points
            part2_scratchcards.append({"count": 1, "wins": wins})

    for index, card in enumerate(part2_scratchcards):
        for card_to_copy in range(index + 1, index + 1 + card["wins"]):
            part2_scratchcards[card_to_copy]["count"] += card["count"]

    part2_total_cards = sum([card["count"] for card in part2_scratchcards])

    logging.debug(f"Result for part 1 is: {part1_pile_points}")
    logging.debug(f"Result for part 2 is: {part2_total_cards}")
    return (part1_pile_points, part2_total_cards)


if __name__ == "__main__":
    # logging configuration
    log_level = "DEBUG"
    logging.basicConfig(
        level=logging.getLevelName(log_level),
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    results = scratchcards()

    print(f"Result for part 1: {results[0]}")
    print(f"Result for part 2: {results[1]}")
