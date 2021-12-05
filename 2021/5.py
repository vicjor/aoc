from collections import defaultdict
from time import perf_counter
from utils.filereader import file_reader, file_reader_int
from typing import List, Tuple


def is_vertical(x1: int, x2: int) -> bool:
    return x1 == x2


def is_horizontal(y1: int, y2: int) -> bool:
    return y1 == y2


def is_diagonal(x1: int, y1: int, x2: int, y2: int) -> bool:
    return not is_vertical(x1, x2) and not is_horizontal(y1, y2)


def line_to_coordinates(line) -> Tuple[int, int, int, int]:
    x1y1, x2y2 = line.split("->")[0], line.split("->")[1]
    x1, y1 = int(x1y1.split(",")[0]), int(x1y1.split(",")[1])
    x2, y2 = int(x2y2.split(",")[0]), int(x2y2.split(",")[1])
    return (x1, y1, x2, y2)


def aggregate_overlaps(lines, include_diagonals=False):
    """Aggregate all points in grid crossed by lines."""
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
                for i in range(x1-x2+1):
                    # for j in range(y1-y2):
                    coordinates[(x1-i, y1-i)] += 1
            elif x1 < x2 and y1 < y2:
                for i in range(x2-x1+1):
                    # for j in range(y1, y2 + 1):
                    coordinates[(x1+i, y1+i)] += 1
            elif x1 > x2 and y1 < y2:
                for i in range(x1-x2+1):
                    # for j in range(y1, y2 + 1):
                    coordinates[(x1-i, y1+i)] += 1
            elif x1 < x2 and y1 > y2:
                for i in range(x2-x1+1):
                    # for j in range(y2, y1 + 1):
                    coordinates[(x1+i, y1-i)] += 1
    return coordinates


def count_overlaps(coordinates: defaultdict(int)) -> int:
    """Number of points with at least two overlaps."""
    values = list(coordinates.values())
    number_of_coords = len(values)  # Number of values in grid
    number_of_ones = values.count(1)  # Count number of 1's in grid
    return number_of_coords - number_of_ones


def main():
    start = perf_counter()  # Start time

    lines = file_reader("data/input5.txt")
    coordinates = aggregate_overlaps(lines)
    coordinates_2 = aggregate_overlaps(lines, True)
    overlaps = count_overlaps(coordinates)
    overlaps_2 = count_overlaps(coordinates_2)
    print(f"Number of points with minimum two overlaps: {overlaps}")  # 5585
    print(
        f"Number of points with minimum two overlaps including diagonals: {overlaps_2}")  # 17193
    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"\nTotal runtime: {time} seconds.")


if __name__ == "__main__":
    main()
