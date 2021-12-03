from typing import List


def file_reader(filename) -> List[str]:
    """
    Function used to read a file and strip newlines.

    filename : str

    returns : list[str]
    """
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line.strip("\n"))
    return lines


def file_reader_int(filename) -> List[int]:
    """
    Function used to read a file and turn each line into a integer.

    filename : str

    returns : list[int]
    """
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(int(line.strip("\n")))
    return lines
