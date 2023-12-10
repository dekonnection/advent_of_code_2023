#!/usr/bin/env python3
import logging
import sys

PAYLOAD = sys.argv[1]

pipes_types = {
    "|": {
        "N": "N",
        "S": "S",
    },
    "-": {
        "W": "W",
        "E": "E",
    },
    "L": {
        "S": "E",
        "W": "N",
    },
    "J": {
        "S": "W",
        "E": "N",
    },
    "7": {
        "E": "S",
        "N": "W",
    },
    "F": {
        "N": "E",
        "W": "S",
    },
    "S": {},
}

map = []
with open(PAYLOAD) as f:
    for _line in f:
        for index, char in enumerate(_line.strip()):
            if index >= len(map):
                map.append([])
            map[index].append(char)
            if char == "S":
                starting_point = (index, len(map[index]) - 1)


def part1(map, starting_point):
    path = [starting_point]
    path.append(connected_pipes(map, starting_point)[0][1])
    while next_pipe := [
        pipe for pipe in connected_pipes(map, path[-1]) if pipe[1] not in path
    ]:
        path.append(next_pipe[0][1])
    logging.info(path)
    return len(path) / 2


def connected_pipes(map, coordinates):
    logging.debug(f"Searching pipes connected to {coordinates}")
    x = coordinates[0]
    y = coordinates[1]
    connected_pipes = []
    neighborhood = {}
    # we append all possible neighbors if:
    ## they're not out of bounds
    ## they're on a side on which our current pipe has an output
    ## (special case for S, we don't check it for that)
    if y - 1 >= 0 and ("N" in pipes_types.get(map[x][y]).values() or map[x][y] == "S"):
        neighborhood["N"] = (x, y - 1)
    if x - 1 >= 0 and ("W" in pipes_types.get(map[x][y]).values() or map[x][y] == "S"):
        neighborhood["W"] = (x - 1, y)
    if x + 1 < len(map) and (
        "E" in pipes_types.get(map[x][y]).values() or map[x][y] == "S"
    ):
        neighborhood["E"] = (x + 1, y)
    if y + 1 < len(map[0]) and (
        "S" in pipes_types.get(map[x][y]).values() or map[x][y] == "S"
    ):
        neighborhood["S"] = (x, y + 1)
    for side, new_coordinates in neighborhood.items():  # checking each side (NSEW)
        neighbor_type = map[new_coordinates[0]][
            new_coordinates[1]
        ]  # getting the neighbor at the current side
        if pipe := pipes_types.get(neighbor_type):  # the neighbor is a pipe
            logging.debug(f"Found pipe in side {side}")
            if pipe.get(side):  # the neighbor accept flow from this side
                logging.debug(f"side {side} is ok")
                connected_pipes.append((side, new_coordinates))
            else:
                logging.debug(f"side {side} is not ok")
    logging.debug(
        f"Current pipe: {map[x][y]} ({x},{y}) is connected to {connected_pipes}"
    )
    return connected_pipes


if __name__ == "__main__":
    # logging configuration
    log_level = "INFO"
    # log_level = "DEBUG"
    logging.basicConfig(
        level=logging.getLevelName(log_level),
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    part1_result = part1(map, starting_point)
    # part2_result = part2(values)

    print(f"Result for part 1: {part1_result}")
    # print(f"Result for part 2: {part2_result}")
