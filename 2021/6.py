from time import perf_counter
from utils.filereader import file_reader
from typing import List
import numpy as np
from numpy.linalg import matrix_power


def simulate(initial_state: List[int], days: int = 80) -> int:
    """Naive implementation for exponential growth."""
    lanternfish = initial_state
    for i in range(days):
        temp = []
        for index, fish in enumerate(lanternfish):
            if fish == 0:
                temp.append(8)
                lanternfish[index] = 6
            else:
                lanternfish[index] -= 1
        lanternfish += temp
    return len(lanternfish)


def simulate_2(lanternfish: List[int]) -> int:
    """
    Matrix operation to simulate exponential growth for 256 days.
    2^8 = 256
    1D-array fish_count represents number of fish with each possible state
    2D-array A transition matrix
    sum(A^256 * fish_count) gives number of fish after 256 days.
    """
    A = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [1, 0, 0, 0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0, 0, 0, 0, 0]])
    fish_count = []
    for i in range(9):
        fish_count.append(lanternfish.count(i))
    return np.sum(matrix_power(A, 256).dot(np.array(fish_count)))


def main():
    start = perf_counter()  # Start time

    data = file_reader("data/input6.txt")
    initial_state = [int(x) for x in data[0].split(",")]
    print("## PART 1 ##")
    part1 = simulate(initial_state)
    print(f"There are {part1} lanternfish after 80 days.\n")  # 373378

    print("## PART 2 ##")
    part2 = simulate_2(initial_state)
    print(f"There are {part2} lanternfish after 256 days.")  # 1786011142253081
    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"\nTotal runtime: {time} seconds.")


if __name__ == "__main__":
    main()
