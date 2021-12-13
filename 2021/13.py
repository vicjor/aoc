from time import perf_counter
from utils.filereader import file_reader, file_reader_int
from typing import List, Tuple
from functools import reduce
import numpy as np


def prepare_data(data: List[str]) -> Tuple[List[Tuple[int, int]], List[str]]:
    """Return coordinates and instructions."""
    line_shift_index = data.index('')
    coordinates = []
    instructions = data[line_shift_index+1::]
    for i, instruction in enumerate(instructions):
        instructions[i] = instruction.split(" ")[2]
    for _ in data[0: line_shift_index]:
        x = int(_.split(",")[0])
        y = int(_.split(",")[1])
        coordinates.append((x, y))
    return coordinates, instructions


def get_grid(coordinates: List[Tuple[int, int]]):
    """Create a grid and fill inn coordinates"""
    x_max = 0
    y_max = 0
    for x, y in coordinates:
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y

    grid = []
    for i in range(y_max+1):
        row = []
        for j in range(x_max+1):
            row.append(".")
        grid.append(row)
    for x, y in coordinates:
        grid[y][x] = "#"
    return grid


def print_grid(grid: List[List[str]]):
    for _ in grid:
        print(_)


def fold(grid: List[List[str]], instruction: List[str], horizontal: bool = True):
    """Fold paper horizontal/vertical across instruction value. Return new grid."""
    if horizontal:
        upper = grid[0:instruction]
        lower = grid[instruction+1::]
        lower_flipped = np.flip(np.array(lower), axis=0)
        for i, row in enumerate(lower_flipped):
            for j, col in enumerate(row):
                if col == "#":
                    upper[i][j] = "#"
        return upper
        # for _ in upper:
        #     print(_)
        # print("-"*55)
        # for _ in lower:
        #     print(_)
    else:
        left = []
        right = []
        for row in grid:
            left.append(row[0:instruction])
            right.append(row[instruction+1::])
        right_flipped = np.flip(np.array(right), axis=1)
        for i, row in enumerate(right_flipped):
            for j, col in enumerate(row):
                if col == "#":
                    left[i][j] = "#"
        return left


def count_dots(grid: List[List[str]]) -> int:
    """Return number of '#' in grid."""
    count = 0
    for i in grid:
        for j in i:
            if j == "#":
                count += 1
    return count


def perform_instructions(grid: List[List[str]], instructions: List[str]) -> List[List[str]]:
    """Perform all folds according to instructions."""
    for instruction in instructions:
        axis, value = instruction.split("=")[0], int(instruction.split("=")[1])
        if axis == "x":
            horizontal = False
        else:
            horizontal = True
        grid = fold(grid, value, horizontal)
    return grid


def main():
    data = file_reader("data/input13.txt")
    coordinates, instructions = prepare_data(data)
    grid = get_grid(coordinates)
    grid = fold(grid, 655, horizontal=False)
    dots = count_dots(grid)

    print("## PART 1 ##")
    print(f"{dots} visible dots after folding vertical across x = 655.\n")  # 765

    print("## PART 2## ")
    folded_grid = perform_instructions(grid, instructions)
    print_grid(folded_grid)


if __name__ == "__main__":
    start = perf_counter()  # Start time
    main()
    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"Total runtime: {time} seconds.")
