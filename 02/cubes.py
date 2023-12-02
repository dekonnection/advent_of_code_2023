#!/usr/bin/env python3
import logging


## part 1 start ##
REAL_COLORS_COUNTS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def part1():
    possible_games = 0
    with open("payload.txt") as f:
        logging.info("Payload reading: start.")
        # we iterate on each line of the payload
        for game_id, raw_line in enumerate(f):
            colors_counts = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            line = raw_line.strip()  # some cleaning just in case
            logging.debug(f"Payload reading new line: `{line}`")
            logging.debug(f"Game ID is {game_id+1}")
            game = line.split(":")
            draws = game[1].strip().split(";")
            for draw in draws:
                colors = draw.strip().split(",")
                for raw_color in colors:
                    color = raw_color.strip().split(" ")
                    colors_counts[color[1]] = max(
                        colors_counts[color[1]], int(color[0])
                    )
            logging.debug(f"Counts for game {game_id+1} is {colors_counts}")
            possible = True
            for color, real_count in REAL_COLORS_COUNTS.items():
                if colors_counts[color] > real_count:
                    logging.debug(
                        f"Not possible: drew {colors_counts[color]} of {color} instead of {real_count} possible."
                    )
                    possible = False
                    break
                else:
                    logging.debug(
                        f"Possible: drew {colors_counts[color]} of {color} for {real_count} possible."
                    )
            if possible:
                logging.debug(f"Game {game_id+1} is possible")
                possible_games += game_id + 1
            else:
                logging.debug(f"Game {game_id+1} is impossible")
    logging.debug(f"Result for part 1 is: {possible_games}")
    return possible_games


## part 1 end ##

## part 2 start ##


def part2():
    sum_of_power = 0
    with open("payload.txt") as f:
        logging.info("Payload reading: start.")
        # we iterate on each line of the payload
        for game_id, raw_line in enumerate(f):
            colors_counts = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            line = raw_line.strip()  # some cleaning just in case
            logging.debug(f"Payload reading new line: `{line}`")
            logging.debug(f"Game ID is {game_id+1}")
            game = line.split(":")
            draws = game[1].strip().split(";")
            for draw in draws:
                colors = draw.strip().split(",")
                for raw_color in colors:
                    color = raw_color.strip().split(" ")
                    colors_counts[color[1]] = max(
                        colors_counts[color[1]], int(color[0])
                    )
            logging.debug(f"Counts for game {game_id+1} is {colors_counts}")

            power_of_cubes = 1
            for cubes in colors_counts.values():
                power_of_cubes = power_of_cubes * cubes
            logging.debug(f"Power of cubes for game {game_id+1} is {power_of_cubes}")

            sum_of_power += power_of_cubes

    logging.debug(f"Result for part 2 is: {sum_of_power}")
    return sum_of_power


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
