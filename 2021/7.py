from time import perf_counter
from utils.filereader import file_reader
from typing import List


def cheapest_alignment(positions: List[int]) -> int:
    _max = max(positions)
    _min = min(positions)
    cheapest = 99999999999999999
    for i in range(_min, _max):
        temp = 0
        for pos in positions:
            temp += abs(pos-i)
        if temp < cheapest:
            cheapest = temp
        temp = 0
    return cheapest


def cheapest_alignment_2(positions: List[int]) -> int:
    _max = max(positions)
    _min = min(positions)
    cheapest = 99999999999999999
    for i in range(_max):
        temp = 0
        for pos in positions:
            # n'th triangle number as a binomial coeffisient
            n = abs(pos-i)
            temp += (n*(n+1))/2
        if temp < cheapest:
            cheapest = temp
        temp = 0
    return cheapest


def main():
    start = perf_counter()  # Start time

    data = file_reader("data/input7.txt")
    positions = [int(x) for x in data[0].split(",")]
    print(cheapest_alignment_2(positions))  # 328187

    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"Total runtime: {time} seconds.")


if __name__ == "__main__":
    main()
