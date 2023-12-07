#!/usr/bin/env python3
import logging
import re
import math
import sys
import collections

PAYLOAD = sys.argv[1]


def part1():
    hands = []
    with open(PAYLOAD) as f:
        for _line in f:
            # numbers.append(re.findall("[0-9]+", line))
            line = _line.strip().split(" ")
            hands.append((line[0], int(line[1])))
    logging.debug(f"Cards: {hands}")

    ordered_hands = sorted([[*identify_hand(hand[0]), hand[1]] for hand in hands])
    final_score = sum(
        [(rank + 1) * values[2] for rank, values in enumerate(ordered_hands)]
    )
    return final_score


def identify_hand(raw_hand):
    logging.debug(f"Identifying {raw_hand}")
    cards_strengths = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    counts = collections.Counter(raw_hand).most_common()
    if counts[0][1] == 5:
        score = 6
        # type = "five_of_a_kind"
    elif counts[0][1] == 4:
        score = 5
        # type = "four_of_a_kind"
    elif counts[0][1] == 3:
        if counts[1][1] == 2:
            score = 4
            # type = "full_house"
        else:
            score = 3
            # type = "three_of_a_kind"
    elif counts[0][1] == 2:
        if counts[1][1] == 2:
            score = 2
            # type = "two_pairs"
        else:
            score = 1
            # type = "one_pair"
    else:
        score = 0
    strengths = [cards_strengths.index(card) for card in raw_hand]
    logging.debug(f"{raw_hand}: {score} {strengths}")
    return (score, strengths)


def part2():
    hands = []
    with open(PAYLOAD) as f:
        for _line in f:
            # numbers.append(re.findall("[0-9]+", line))
            line = _line.strip().split(" ")
            hands.append((line[0], int(line[1])))
    logging.debug(f"Cards: {hands}")

    ordered_hands = sorted(
        [[*identify_hand_with_joker(hand[0]), hand[1]] for hand in hands]
    )
    final_score = sum(
        [(rank + 1) * values[2] for rank, values in enumerate(ordered_hands)]
    )
    return final_score


def identify_hand_with_joker(raw_hand):
    logging.debug(f"Identifying {raw_hand}")
    jokerized_hand = joker_treatment(raw_hand)
    cards_strengths = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    counts = collections.Counter(jokerized_hand).most_common()
    if counts[0][1] == 5:
        score = 6
        # type = "five_of_a_kind"
    elif counts[0][1] == 4:
        score = 5
        # type = "four_of_a_kind"
    elif counts[0][1] == 3:
        if counts[1][1] == 2:
            score = 4
            # type = "full_house"
        else:
            score = 3
            # type = "three_of_a_kind"
    elif counts[0][1] == 2:
        if counts[1][1] == 2:
            score = 2
            # type = "two_pairs"
        else:
            score = 1
            # type = "one_pair"
    else:
        score = 0
    strengths = [cards_strengths.index(card) for card in raw_hand]
    logging.debug(f"{raw_hand} ({jokerized_hand}): {score} {strengths}")
    return (score, strengths)


def joker_treatment(hand):
    cards_strengths = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    if hand == "JJJJJ":
        logging.debug("Hand is JJJJJ => AAAAA")
        return "AAAAA"
    elif "J" in hand:
        counts = collections.Counter(hand).most_common()
        # returns a list of the top most common cards, without returning J nor counting J as the most common to be equal with
        top_cards = [
            count[0]
            for count in counts
            if count[1] == max([count[1] for count in counts if count[0] != "J"])
            and count[0] != "J"
        ]
        logging.debug(f"Top cards for {hand}: {top_cards}")
        # returns the single most valued card from the previous list
        top_card = cards_strengths[
            max([cards_strengths.index(card) for card in top_cards])
        ]
        logging.debug(f"Most valued top card is {top_card}")
        new_hand = hand.replace("J", top_card)
        logging.debug(f"{hand} is now {new_hand}")
        return new_hand
    else:
        logging.debug(f"No joker in {hand}.")
        return hand


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
