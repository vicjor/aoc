import time
from typing import Tuple
boarding_passes = []
with open("input5.txt", "r") as file:
    for line in file:
        boarding_passes.append(line.replace("\n", ""))


# Binary search for row. Convert string to binary numbers, then convert to deci
def row(string) -> int:
    row = string[:-3]
    binary_row = ""
    for char in row:
        if (char == "F"):
            binary_row += "0"
        else:
            binary_row += "1"
    return int(binary_row, 2)  # Returns deci value of a binary number


# Binary search for row
def col(string) -> int:
    col = string[-3:]
    binary_col = ""
    for char in col:
        if (char == "L"):
            binary_col += "0"
        else:
            binary_col += "1"
    return int(binary_col, 2)


highest_id = 0
for string in boarding_passes:
    # ID = row * 8 + col
    id = row(string)*8 + col(string)
    if (id > highest_id):
        highest_id = id
print("{} is the highest seat ID on a boarding pass".format(highest_id))


# Part 2
# Rule: Multiply row by 8 and add col number to find id
# ID = row*8 + col
ids = sorted([row(s)*8 + col(s) for s in boarding_passes])

# Find the missing ID
for index in range(len(ids)):
    if (index > 0 and index < len(ids)-1):
        if (ids[index+1] != ids[index]+1):
            print("Your missing ID is {}".format(ids[index] + 1))
            break
