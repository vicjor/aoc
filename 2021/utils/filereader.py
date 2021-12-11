from typing import List


def file_reader(filename: str) -> List[str]:
    """
    Function used to read a file and strip newlines.
    :param filename file to read
    """
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line.strip("\n"))
    return lines


def file_reader_int(filename: str) -> List[int]:
    """
    Function used to read a file and turn each line into a integer.
    :param filename file to read
    """
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(int(line.strip("\n")))
    return lines


def file_reader_grid_int(filename: str) -> List[List[int]]:
    """
    Function used to read a file and turn it into a grid
    :param filename file to read
    """
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            grid.append([int(x) for x in list(line.strip("\n"))])
    return grid
