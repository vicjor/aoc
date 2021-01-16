import time

with open("input11.txt", "r") as file:
    data = [line.strip("\n") for line in file]


# First solution. Much redundant checks.
def numberOfOccupiedAdjacentSeats(seats, row, col) -> int:
    up = 0
    down = 0
    right = 0
    left = 0

    # Diagonals
    downright = 0
    upright = 0
    upleft = 0
    downleft = 0

    # First four if's to check for all corner cases
    if (row == 0 and col == 0):  # Seat in top left corner
        if (seats[row+1][col] == "#"):
            down += 1
        if (seats[row][col+1] == "#"):
            right += 1
        if (seats[row+1][col+1] == "#"):
            downright += 1

    elif (row == 90 and col == 94):  # Seat in lower right corner
        if (seats[row-1][col] == "#"):
            up += 1
        if (seats[row][col-1] == "#"):
            left += 1
        if (seats[row-1][col-1] == "#"):
            upleft += 1

    elif (row == 90 and col == 0):  # Seat in lower left corner
        if (seats[row-1][col] == "#"):
            up += 1
        if (seats[row][col+1] == "#"):
            right += 1
        if (seats[row-1][col+1] == "#"):
            upright += 1

    elif (row == 0 and col == 94):  # Seat in top right corner
        if (seats[row+1][col] == "#"):
            down += 1
        if (seats[row][col-1] == "#"):
            left += 1
        if (seats[row+1][col-1] == "#"):
            downleft += 1

    # All corners handled

    elif (row == 0 and col != 0 and col != 94):  # First row
        if (seats[row+1][col] == "#"):
            down += 1
        if (seats[row][col-1] == "#"):
            left += 1
        if (seats[row][col+1] == "#"):
            right += 1
        if (seats[row+1][col-1] == "#"):
            downleft += 1
        if (seats[row+1][col+1] == "#"):
            downright += 1
    elif (row == 90 and col != 0 and col != 94):  # Final row
        if (seats[row][col-1] == "#"):
            left += 1
        if (seats[row][col+1] == "#"):
            right += 1
        if (seats[row-1][col] == "#"):
            up += 1
        if (seats[row-1][col+1] == "#"):
            upright += 1
        if (seats[row-1][col-1] == "#"):
            upleft += 1
    elif(col == 0 and row != 0 and row != 90):  # Leftmost column
        if (seats[row+1][col] == "#"):
            down += 1
        if (seats[row-1][col] == "#"):
            up += 1
        if (seats[row][col+1] == "#"):
            right += 1
        if (seats[row-1][col+1] == "#"):
            upright += 1
        if (seats[row+1][col+1] == "#"):
            downright += 1
    elif(col == 94 and row != 0 and row != 90):  # Rightmost column
        if (seats[row+1][col] == "#"):
            down += 1
        if (seats[row][col-1] == "#"):
            left += 1
        if (seats[row-1][col] == "#"):
            up += 1
        if (seats[row+1][col-1] == "#"):
            downleft += 1
        if (seats[row-1][col-1] == "#"):
            upleft += 1

    # All edges handled

    # If neither row or col is an edge
    elif (row != 0 and row != 90 and col != 0 and col != 94):
        if (seats[row+1][col] == "#"):
            down += 1
        if (seats[row][col-1] == "#"):
            left += 1
        if (seats[row-1][col] == "#"):
            up += 1
        if (seats[row][col+1] == "#"):
            right += 1
        if (seats[row+1][col-1] == "#"):
            downleft += 1
        if (seats[row-1][col+1] == "#"):
            upright += 1
        if (seats[row-1][col-1] == "#"):
            upleft += 1
        if (seats[row+1][col+1] == "#"):
            downright += 1
    else:  # If this line executes, all possible cases has not been handled
        print(row, col)

    count = up + down + right + left + downleft + downright + upright + upleft
    return count


# Revised solution. Less redundant, probably still much room for improvement.
def numberOfOccupiedAdjacentSeatsRevised(seats, row, col) -> int:
    up = 0
    down = 0
    right = 0
    left = 0
    downright = 0
    upright = 0
    upleft = 0
    downleft = 0

    # First cover all cases when row is 0
    if (row == 0):  # Seat in top left corner
        if (col == 0):
            if (seats[row+1][col] == "#"):
                down += 1
            if (seats[row][col+1] == "#"):
                right += 1
            if (seats[row+1][col+1] == "#"):
                downright += 1
        elif (col == 94):
            if (seats[row+1][col] == "#"):
                down += 1
            if (seats[row][col-1] == "#"):
                left += 1
            if (seats[row+1][col-1] == "#"):
                downleft += 1
        else:
            if (seats[row+1][col] == "#"):
                down += 1
            if (seats[row][col-1] == "#"):
                left += 1
            if (seats[row][col+1] == "#"):
                right += 1
            if (seats[row+1][col-1] == "#"):
                downleft += 1
            if (seats[row+1][col+1] == "#"):
                downright += 1

    # Then cover all cases if row is 90
    elif (row == 90):  # Seat in lower right corner
        if (col == 94):
            if (seats[row-1][col] == "#"):
                up += 1
            if (seats[row][col-1] == "#"):
                left += 1
            if (seats[row-1][col-1] == "#"):
                upleft += 1
        elif (col == 0):
            if (seats[row-1][col] == "#"):
                up += 1
            if (seats[row][col+1] == "#"):
                right += 1
            if (seats[row-1][col+1] == "#"):
                upright += 1
        else:
            if (seats[row][col-1] == "#"):
                left += 1
            if (seats[row][col+1] == "#"):
                right += 1
            if (seats[row-1][col] == "#"):
                up += 1
            if (seats[row-1][col+1] == "#"):
                upright += 1
            if (seats[row-1][col-1] == "#"):
                upleft += 1

    # All cases where row is 0 or 90, and col 0 or 94 is handled.
    # Safe to assume each remaining seat have 8 adjacents something
    else:
        if (col == 0):
            if (seats[row+1][col] == "#"):
                down += 1
            if (seats[row-1][col] == "#"):
                up += 1
            if (seats[row][col+1] == "#"):
                right += 1
            if (seats[row-1][col+1] == "#"):
                upright += 1
            if (seats[row+1][col+1] == "#"):
                downright += 1
        elif (col == 94):
            if (seats[row+1][col] == "#"):
                down += 1
            if (seats[row][col-1] == "#"):
                left += 1
            if (seats[row-1][col] == "#"):
                up += 1
            if (seats[row+1][col-1] == "#"):
                downleft += 1
            if (seats[row-1][col-1] == "#"):
                upleft += 1

        else:
            if (seats[row+1][col] == "#"):
                down += 1
            if (seats[row][col-1] == "#"):
                left += 1
            if (seats[row-1][col] == "#"):
                up += 1
            if (seats[row][col+1] == "#"):
                right += 1
            if (seats[row+1][col-1] == "#"):
                downleft += 1
            if (seats[row-1][col+1] == "#"):
                upright += 1
            if (seats[row-1][col-1] == "#"):
                upleft += 1
            if (seats[row+1][col+1] == "#"):
                downright += 1

    return up + down + right + left + downleft + downright + upright + upleft


# Return true if no adjacent seats is occupied
def noOccupiedAdjacents(seats, row, col) -> bool:
    return numberOfOccupiedAdjacentSeatsRevised(seats, row, col) == 0


# Returns true if a occupied seat will become available. # -> L
def willSeatBecomeEmpty(seats, row, col) -> bool:
    return numberOfOccupiedAdjacentSeatsRevised(seats, row, col) >= 4


def part1():
    old_data = data  # Point to original data
    new_data = []  # New struct for reordered seatings

    iteration_counter = 0

    # If the data don't change after applying the rule to all seats, terminate
    while (new_data != old_data):
        # After each iteration except the first, update pointers
        if (iteration_counter > 0):
            old_data = new_data
        iteration_counter += 1
        new_data = []  # Refresh new_data

        for row in range(len(old_data)):
            new_row = ""
            for col in range(len(old_data[row])):
                if (old_data[row][col] == "L"):
                    # Becomes occupied when no adjacent seats are occupied
                    if (noOccupiedAdjacents(old_data, row, col)):
                        new_row += "#"
                    else:
                        new_row += old_data[row][col]
                elif (old_data[row][col] == "#"):
                    if (willSeatBecomeEmpty(old_data, row, col)):
                        # Becomes empty if four or more adjacents are occupied
                        new_row += "L"
                    else:
                        new_row += old_data[row][col]
                # If neither, the seat's state does not change
                else:
                    new_row += old_data[row][col]
            # Append new seatings of row to new_data for each row
            new_data.append(new_row)

    occupied_seats = 0
    # Count number of occupied seats
    for row in new_data:
        occupied_seats += row.count("#")

    print("{} occupied seats after {} iterations".format(
        occupied_seats, iteration_counter))


# start = time.perf_counter()
# part1()
# end = time.perf_counter()
# print("Time: {}".format(end-start))
# END PART 1

# START PART 2
# Solutions inspired by: https://github.com/stereoabuse/Advent-of-Code-2020/blob/main/solutions/day_11.py


EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."


def seating(seats, threshold, mode):
    grid = seats
    while True:
        new_seats = []
        for row in range(len(grid)):
            new_row = []
            for col in range(len(grid[row])):
                seat = grid[row][col]
                adjacent = [i for i in mode(row, col, grid)]
                if (seat == EMPTY and adjacent.count(OCCUPIED) == 0):
                    new_row.append(OCCUPIED)

                elif (seat == OCCUPIED and adjacent.count(OCCUPIED) >= threshold):
                    new_row.append(EMPTY)
                else:
                    new_row.append(seat)
            new_seats.append(new_row)
        if grid == new_seats:
            return sum(i.count(OCCUPIED) for i in new_seats)
        grid = new_seats
# yield: https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
# TLDR: Yield; iterate over a function as a generator. Yield returns a sequence of values


def visible(row, col, seats):
    # x,y directions to move from current seat
    # E.g. (-1, -1) up to left, (0, 1) right
    for x in range(-1, 2):
        for y in range(-1, 2):
            i = 1
            # Check that index is in bounds of the seating grid and that its not the current seat.
            # Multiply with i until out of bounds, then check new direction
            while 0 <= row + i * x < len(seats) and 0 <= col + i*y < len(seats[0]) and not x == y == 0:
                if (seats[row + i*x][col + i*y] != "."):
                    # yield visible seat that is not floor
                    # next execution/iteration over generator will resume here, returning next visible seat
                    yield seats[row + i*x][col + i*y]
                    break
                i += 1


def part2():
    print(seating(data, 5, visible))


start = time.perf_counter()
part2()
end = time.perf_counter()
print("Solved in {} seconds".format(round(float(end-start), 4)))
