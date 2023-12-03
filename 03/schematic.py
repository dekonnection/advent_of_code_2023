#!/usr/bin/env python3
import logging


## part 1 start ##
def part1():
    logging.info("Starting part 1")
    part_numbers = []
    symbols = {}
    with open("payload.txt") as f:
        logging.info("Payload reading: start.")
        part_number_in_progress = ""
        part_number_in_progress_coordinates = []
        # we iterate on each line of the payload
        for y, raw_line in enumerate(f):
            line = raw_line.strip()  # some cleaning just in case
            logging.debug(f"Payload reading new line: `{line}`")

            # we read all characters from a line
            for x, character in enumerate(line):
                try:
                    number = int(character)
                    logging.debug(f"Found new integer: {number}.")
                    if part_number_in_progress:
                        logging.debug(
                            "We are already building a part number, adding the char and updating end coordinates"
                        )
                        part_number_in_progress += str(number)
                        part_number_in_progress_coordinates[1] = [x, y]
                    else:
                        logging.debug(
                            "We are beginning a new part number, storing char and initial coordinates"
                        )
                        part_number_in_progress = str(character)
                        part_number_in_progress_coordinates = [[x, y], [x, y]]
                except ValueError:
                    # if we get here, we do not have an int
                    logging.debug(
                        "Not an integer, we have a dot or a special character."
                    )
                    if part_number_in_progress:
                        logging.debug(
                            "The dot/special character marks the end of a part number, storing it to the index."
                        )
                        part_numbers.append(
                            [
                                int(part_number_in_progress),
                                part_number_in_progress_coordinates,
                            ]
                        )
                        part_number_in_progress = ""
                        part_number_in_progress_coordinates = []
                    if character == ".":
                        logging.debug("Character is a dot, nothing else to do.")
                    else:
                        logging.debug(f"We have a symbol: {character}.")
                        if not symbols.get(x):
                            symbols[x] = {}
                        symbols[x][y] = character
            if part_number_in_progress:
                logging.debug(
                    "The dot/special character marks the end of a part number, storing it to the index."
                )
                part_numbers.append(
                    [
                        int(part_number_in_progress),
                        part_number_in_progress_coordinates,
                    ]
                )
                part_number_in_progress = ""
                part_number_in_progress_coordinates = []
        logging.debug(f"Found potential part numbers {part_numbers}")
        logging.debug(f"Found symbols: {symbols}")

    logging.info("Starting analysis to found out real part numbers")
    real_part_numbers = []
    for part in part_numbers:
        part_number = part[0]
        coordinates = part[1]
        logging.debug(f"Starting analysis of {part_number} ({coordinates})")
        part_number_is_real = False
        y = coordinates[0][1]
        start = coordinates[0][0]
        end = coordinates[1][0]
        logging.debug(
            f"{part_number} is at line {y} with start at {start} and end at {end}"
        )
        for y in range(y - 1, y + 2):
            for x in range(start - 1, end + 2):
                logging.debug(f"Looking for symbol at {x},{y}")
                if symbols.get(x):
                    if symbol := symbols[x].get(y):
                        logging.info(f"Found {symbol} at {x},{y}")
                        part_number_is_real = True
        if part_number_is_real:
            real_part_numbers.append(part_number)

    logging.info(f"Real part numbers: {real_part_numbers}")
    result = sum(real_part_numbers)
    logging.debug(f"Result for part 1 is: {result}")
    return result


## part 1 end ##
## part 2 start ##
def part2():
    logging.info("Starting part 2")
    part_numbers = []
    stars = {}
    with open("payload.txt") as f:
        logging.info("Payload reading: start.")
        part_number_in_progress = ""
        part_number_in_progress_coordinates = []
        # we iterate on each line of the payload
        for y, raw_line in enumerate(f):
            line = raw_line.strip()  # some cleaning just in case
            logging.debug(f"Payload reading new line: `{line}`")

            # we read all characters from a line
            for x, character in enumerate(line):
                try:
                    number = int(character)
                    logging.debug(f"Found new integer: {number}.")
                    if part_number_in_progress:
                        logging.debug(
                            "We are already building a part number, adding the char and updating end coordinates"
                        )
                        part_number_in_progress += str(number)
                        part_number_in_progress_coordinates[1] = [x, y]
                    else:
                        logging.debug(
                            "We are beginning a new part number, storing char and initial coordinates"
                        )
                        part_number_in_progress = str(character)
                        part_number_in_progress_coordinates = [[x, y], [x, y]]
                except ValueError:
                    # if we get here, we do not have an int
                    logging.debug(
                        "Not an integer, we have a dot or a special character."
                    )
                    if part_number_in_progress:
                        logging.debug(
                            "The dot/special character marks the end of a part number, storing it to the index."
                        )
                        part_numbers.append(
                            [
                                int(part_number_in_progress),
                                part_number_in_progress_coordinates,
                            ]
                        )
                        part_number_in_progress = ""
                        part_number_in_progress_coordinates = []
                    if character == "*":
                        logging.debug(f"We have a star.")
                        if type(stars.get(x)) != dict:
                            stars[x] = {}
                        stars[x][y] = []
            if part_number_in_progress:
                logging.debug(
                    "The dot/special character marks the end of a part number, storing it to the index."
                )
                part_numbers.append(
                    [
                        int(part_number_in_progress),
                        part_number_in_progress_coordinates,
                    ]
                )
                part_number_in_progress = ""
                part_number_in_progress_coordinates = []
        logging.debug(f"Found potential part numbers {part_numbers}")
        logging.debug(f"Found stars: {stars}")

    logging.info("Starting analysis to found out part numbers connected to gears")
    for part in part_numbers:
        part_number = part[0]
        coordinates = part[1]
        logging.debug(f"Starting analysis of {part_number} ({coordinates})")
        y = coordinates[0][1]
        start = coordinates[0][0]
        end = coordinates[1][0]
        logging.debug(
            f"{part_number} is at line {y} with start at {start} and end at {end}"
        )
        for y in range(y - 1, y + 2):
            for x in range(start - 1, end + 2):
                logging.debug(f"Looking for star at {x},{y}")
                try:
                    stars[x][y].append(part_number)
                    logging.debug(f"Star found at {x},{y} !")
                except KeyError:
                    pass

    logging.info(
        "Starting last analysis to found out gears with exactly 2 parts connected"
    )
    result = 0
    for x, x_values in stars.items():
        for y, parts in x_values.items():
            if len(parts) == 2:
                logging.debug(f"Star at ({x},{y}) is connected to 2 parts: {parts}")
                result += parts[0] * parts[1]

    logging.debug(f"Result for part 2 is: {result}")
    return result


## part 2 end ##


if __name__ == "__main__":
    # logging configuration
    # log_level = "INFO"
    log_level = "DEBUG"
    logging.basicConfig(
        level=logging.getLevelName(log_level),
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    result_part_1 = part1()
    result_part_2 = part2()

    print(f"Result for part 1: {result_part_1}")
    print(f"Result for part 2: {result_part_2}")
