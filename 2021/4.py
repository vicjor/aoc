from time import perf_counter
from utils.filereader import file_reader
from typing import List


def create_bingo_boards(bingo_board_numbers: List[int]):
    # List of all bingo board numbers
    bingo_boards = []
    board = []
    for index, row in enumerate(bingo_board_numbers):
        number_row = list(filter(lambda x: x != '', row.split(" ")))
        number_row_int = [int(x) for x in number_row]
        if len(board) < 5:
            # All boards are 5x5
            board.append(number_row_int)
        if len(board) == 5:
            # When a board reaches 5x5, add board to list of all boards and clear current board
            bingo_boards.append(board)
            board = []
    return bingo_boards


def bingo(bingo_board, numbers_drawn):
    # Check horizontally
    for row in bingo_board:
        is_bingo = True
        for num in row:
            if num not in numbers_drawn:
                is_bingo = False
        if (is_bingo):
            print(f"Bingo! (Horizontal)")
            return is_bingo
    # Check vertically
    for col in range(5):
        is_bingo = True
        for row in bingo_board:
            if row[col] not in numbers_drawn:
                is_bingo = False
        if (is_bingo):
            print(f"Bingo! (Vertical)")
            return is_bingo


def play_bingo(bingo_boards, numbers):
    numbers_drawn = []
    for number in numbers:
        numbers_drawn.append(number)
        for board in bingo_boards:
            if (bingo(board, numbers_drawn)):
                return board, numbers_drawn


def play_bingo_2(bingo_boards, numbers):
    numbers_drawn = []
    for number in numbers:
        numbers_drawn.append(number)
        boards_to_remove = []
        for board in bingo_boards:
            if (bingo(board, numbers_drawn)):
                if len(bingo_boards) == 1:
                    print("Last board:", bingo_boards)
                    return board, numbers_drawn
                boards_to_remove.append(board)
        for b in boards_to_remove:
            bingo_boards.remove(b)


def calculate_final_score(board: List[List[int]], numbers_drawn: List[int]) -> int:
    """
    Sum all unmarked numbers and multiply by last drawn number.

    :param board: Winning bingo board
    :param numbers_drawn: List of all numbers drawn before bingo
    """
    flat_list = [num for row in board for num in row]
    filtered = []
    for number in flat_list:
        if number in numbers_drawn:
            continue
        else:
            filtered.append(number)
    sum_unmarked = sum(filtered)
    final_score = sum_unmarked * numbers_drawn[-1]
    return final_score


def main():
    start = perf_counter()  # Start time
    print("## PART 1 ##")
    data = file_reader("data/input4.txt")
    numbers = [int(x) for x in data[0].split(",")]
    bingo_board_numbers = list(
        filter(lambda x: x != '', [x for x in data[1::]]))
    bingo_boards = create_bingo_boards(bingo_board_numbers)
    board, numbers_drawn = play_bingo(bingo_boards, numbers)
    final_score = calculate_final_score(board, numbers_drawn)
    print(f"Final score: {final_score}.\n")  # 35670

    print("## PART 2 ##")

    # play_bingo_3(bingo_boards, numbers)

    board_2, numbers_drawn_2 = play_bingo_2(bingo_boards, numbers)

    winning_number = numbers_drawn_2[-1]
    winning_number_index = numbers_drawn_2.index(winning_number)
    print(f"Winning number: {winning_number}, index {winning_number_index}")
    print("Last board: ", board_2)
    final_score_2 = calculate_final_score(board_2, numbers_drawn_2)
    print(numbers_drawn_2)
    # 25110 too high, 15928 too low. 23892 wrong.
    print(f"Final score: {final_score_2}.\n")

    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"Total runtime: {time} seconds.")


if __name__ == "__main__":
    main()
