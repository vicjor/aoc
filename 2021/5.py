from collections import defaultdict
from time import perf_counter
from utils.filereader import file_reader, file_reader_int
from typing import List


def is_vertical_or_horizontal(x1, y1, x2, y2):
    """687,692 -> 57,692"""
    return x1 == x2 or y1 == y2


def is_vertical(x1: int, x2: int) -> bool:
    return x1 == x2


def is_horizontal(y1: int, y2: int) -> bool:
    return y1 == y2


def is_diagonal(x1: int, y1: int, x2: int, y2: int) -> bool:
    if is_horizontal(y1, y2):
        return False
    if is_vertical(x1, x2):
        return False
    return True


def line_to_coordinates(line):
    """941,230 -> 322,849"""
    x1y1, x2y2 = line.split("->")[0], line.split("->")[1]
    x1, y1 = int(x1y1.split(",")[0]), int(x1y1.split(",")[1])
    x2, y2 = int(x2y2.split(",")[0]), int(x2y2.split(",")[1])
    return x1, y1, x2, y2


def aggregate_overlaps(lines, include_diagonals=False):
    coordinates = defaultdict(int)
    for line in lines:
        x1, y1, x2, y2 = line_to_coordinates(line)
        if is_horizontal(y1, y2):
            if x1 > x2:
                for i in range(x2, x1 + 1):
                    coordinates[(i, y1)] += 1
            else:
                for i in range(x1, x2 + 1):
                    coordinates[(i, y1)] += 1
        elif is_vertical(x1, x2):
            if y1 > y2:
                for i in range(y2, y1 + 1):
                    coordinates[(x1, i)] += 1
            else:
                for i in range(y1, y2 + 1):
                    coordinates[(x1, i)] += 1
        elif include_diagonals and is_diagonal(x1, y1, x2, y2):
            if x1 > x2 and y1 > y2:
                for i in range(x2, x1 + 1):
                    for j in range(y2, y1 + 1):
                        coordinates[(i, j)] += 1
            elif x1 < x2 and y1 < y2:
                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        coordinates[(i, j)] += 1
            elif x1 > x2 and y1 < y2:
                for i in range(x2, x1 + 1):
                    for j in range(y1, y2 + 1):
                        coordinates[(i, j)] += 1
            elif x1 < x2 and y1 > y2:
                for i in range(x1, x2 + 1):
                    for j in range(y2, y1 + 1):
                        coordinates[(i, j)] += 1
    print(coordinates)
    return coordinates


def count_overlaps(coordinates: defaultdict(int)) -> int:
    """Number of points with at least two overlaps."""
    values = list(coordinates.values())
    number_of_coords = len(values)  # Number of values in grid
    number_of_ones = values.count(1)  # Count number of 1's in grid
    return number_of_coords - number_of_ones


def main():
    start = perf_counter()  # Start time

    lines = file_reader("data/test5.txt")
    coordinates = aggregate_overlaps(lines, True)
    overlaps = count_overlaps(coordinates)
    print(f"Number of points with minimum two overlaps: {overlaps}")  # 5585
    # 948637 too high

    print(is_diagonal(941, 230, 322, 849))
    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"Total runtime: {time} seconds.")


if __name__ == "__main__":
    main()
