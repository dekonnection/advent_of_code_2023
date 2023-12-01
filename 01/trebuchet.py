#!/usr/bin/env python3
import logging


## part 1 start ##
def part1():
    # list that will hold final "calibration values" for each line of the payload
    calibration_values = []
    with open("payload.txt") as f:
        logging.info("Payload reading: start.")
        # we iterate on each line of the payload
        for raw_line in f:
            line = raw_line.strip()  # some cleaning just in case
            logging.debug(f"Payload reading new line: {line}")

            # this list will hold all numbers we encounter in the current line
            raw_calibration_line = []
            for char in line:
                # we lazily try to convert to int every character and handle success or fail
                try:
                    number = int(char)
                    # if we get here, we have an int, we add it
                    logging.debug(
                        f"Found new integer: {char}, adding it to raw calibration line"
                    )
                    raw_calibration_line.append(number)
                except ValueError:
                    # if we get here, we do not have an int, we go to the next character
                    logging.debug(f"Not an integer: {char}, will pass.")
                    continue

            logging.debug(
                f"Line finished, raw calibration line: {raw_calibration_line}."
            )
            # final value for the line is the concatenation of first and last number, then converted to int
            calibration_value = int(
                f"{raw_calibration_line[0]}{raw_calibration_line[-1]}"
            )
            logging.debug(f"Final line calibration value: {calibration_value}.")
            # we store this in the main list, and we go to the next line of payload
            calibration_values.append(calibration_value)

    result = sum(calibration_values)
    logging.debug(f"Result for part 1 is: {result}")
    return result


## part 1 end ##

## part 2 start ##

ENGLISH_NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


## first working implementation, but not very smart, I then realized that `word == line[position : position + len(word)]` returns the same thing
# # function that returns True if a word is at a given position in a string, False instead.
# def is_word_at_position(word, line, position):
#     index = 0
#     while index < len(word):
#         try:
#             if word[index] != line[position + index]:
#                 return False
#         except IndexError:
#             return False
#         index += 1
#     return True


def part2():
    # list that will hold final "calibration values" for each line of the payload
    calibration_values = []
    with open("payload.txt") as f:
        logging.info("Payload reading: start.")
        # we iterate on each line of the payload
        for raw_line in f:
            line = raw_line.strip()  # some cleaning just in case
            logging.debug(f"Payload reading new line: {line}")

            # this list will hold all numbers we encounter in the current line
            raw_calibration_line = []
            for index, char in enumerate(line):
                # we lazily try to convert to int every character and handle success or fail
                try:
                    number = int(char)
                    # if we get here, we have an int, we add it
                    logging.debug(
                        f"Found new integer: {char}, adding it to raw calibration line"
                    )
                    raw_calibration_line.append(number)
                except ValueError:
                    # if we get here, we have a char, so we will now check this position in the line with our function for english words for numbers
                    logging.debug(
                        f"Not an integer: {char}, will try to get an english number."
                    )
                    # we check this position for all english numbers
                    for english_number in ENGLISH_NUMBERS:
                        # we crop the line at the current position and with the same amount of characters as the english word, and we compare
                        if english_number == line[index : index + len(english_number)]:
                            logging.debug(
                                f"Found new english number: {english_number} at {index} in {line}, adding it to raw calibration line"
                            )
                            # we store the corresponding int value
                            raw_calibration_line.append(ENGLISH_NUMBERS[english_number])

            logging.debug(
                f"Line finished, raw calibration line: {raw_calibration_line}."
            )
            # final value for the line is the concatenation of first and last number, then converted to int
            calibration_value = int(
                f"{raw_calibration_line[0]}{raw_calibration_line[-1]}"
            )
            logging.debug(f"Final line calibration value: {calibration_value}.")
            # we store this in the main list, and we go to the next line of payload
            calibration_values.append(calibration_value)

    result = sum(calibration_values)
    logging.debug(f"Result for part 2 is: {result}")
    return result


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
