from time import perf_counter
from utils.filereader import file_reader, file_reader_int
from typing import List


def main():
    start = perf_counter()  # Start time

    data = file_reader("data/input.txt")

    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"Total runtime: {time} seconds.")


if __name__ == "__main__":
    main()
