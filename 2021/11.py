from time import perf_counter
from utils.filereader import file_reader_grid_int
from typing import List, Set, Tuple


def next_step(grid: List[List[int]]) -> List[List[int]]:
    """
    - Increase energy level of each octopus by one.
    - Any octopus with energy level greater than 9 flashes, and increases energy level of all adjacent octopi by 1. If this causes another octopus to have a value > 9, it also flashes.
    - Finally, any octopus that flashed have its energy set to 0.
    """
    new_grid = grid
    # Increase all energy levels by one
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col <= 9:
                new_grid[i][j] = col + 1

    return flashing(new_grid)


def flashing(grid: List[List[int]]) -> List[List[int]]:
    """
    Any octopus with a value of 9 flashes.
    Continue flashing if other octopi flash as a results.
    At most one flash per octopus per step.
    """
    flashed = set()
    _any_flash = True
    while _any_flash:
        _any_flash = False
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col > 9:
                    flashed.add((i, j))
                    adjacent = get_adjacent(grid, i, j)
                    increase_adjacent(grid, adjacent, i, j, flashed)
                    grid[i][j] = 0
                    _any_flash = True
    return len(flashed)


def increase_adjacent(grid: List[List[int]], adjacent: List[Tuple[int, int]], row: int, col: int, flashed: Set[Tuple[int, int]]) -> List[List[int]]:
    """Increase all adjacent octopi by 1."""
    for coord in adjacent:
        i, j = coord
        if (i, j) not in flashed and grid[i][j] <= 9:
            grid[i][j] += 1


def get_adjacent(grid: List[List[int]], row: int, col: int) -> List[Tuple[int, int]]:
    """Return list of all coordinates for all adjacent octopi, including diagonals."""
    adjacent = []
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[row]):
                adjacent.append((i, j))
    # Remove self from list of adjacent
    adjacent.remove((row, col))
    return adjacent


def simulate_steps(grid: List[List[int]], steps: int = 100) -> int:
    """Return total number of flashes."""
    flashes = 0
    for _ in range(steps):
        flashes += next_step(grid)

    return flashes


def get_first_synchronized_flash(grid: List[List[int]]) -> int:
    """Return the first step to cause all octopi to flash simultaneously"""
    count = 0
    while True:
        count += 1
        flashes = next_step(grid)
        if flashes == 100:
            return count


def main():
    grid = file_reader_grid_int("data/input11.txt")
    grid_2 = file_reader_grid_int("data/input11.txt")  # For part 2.
    flashes = simulate_steps(grid)
    print("## PART 1 ##")
    print(f"Total number of flashes after 100 steps: {flashes}")
    step = get_first_synchronized_flash(grid_2)
    print("\n## PART 2 ##")
    print(f"All octopi will flash simultaneously at step {step}")


if __name__ == "__main__":
    start = perf_counter()  # Start time
    main()
    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"\nTotal runtime: {time} seconds.")
