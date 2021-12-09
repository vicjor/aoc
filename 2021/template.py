from time import perf_counter
from utils.filereader import file_reader, file_reader_int
from typing import List


def main():

    data = file_reader("data/input.txt")


if __name__ == "__main__":
    start = perf_counter()  # Start time
    main()
    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"Total runtime: {time} seconds.")
