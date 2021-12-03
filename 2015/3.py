# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location,
# and then an elf at the North Pole calls him via radio and tells him where to move next.
# Moves are always exactly one house to the north (^), south (v), east (>), or west (<).
# After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog,
# and so his directions are a little off, and Santa ends up visiting some houses more than once.
# How many houses receive at least one present?

# For example:

# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

# --- Part Two ---
# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house),
# then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

# For example:

# ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
# ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
# ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

with open("input3.txt", "r") as file:
    string = file.readlines()[0].strip("\n")


def at_least_one_present(string):
    # Create dict for all visited houses with x, y coords as key
    # Add/subtract x,y for each direction and return number of houses
    houses = {}
    # Starting house
    houses[(0, 0)] = 1
    x, y = 0, 0
    for i in string:
        if i == "^":
            y += 1
        elif i == "v":
            y -= 1
        elif i == ">":
            x += 1
        elif i == "<":
            x -= 1
        if (x, y) not in houses:
            houses[(x, y)] = 1
        else:
            houses[(x, y)] += 1
    return len(houses)


def increment_direction(x, y, direction):
    if direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    elif direction == ">":
        x += 1
    elif direction == "<":
        x -= 1
    return x, y


def coop_delivery(string):
    houses = {}
    houses[(0, 0)] = 2
    x, y, a, b = 0, 0, 0, 0
    for i, direction in enumerate(string):
        if i % 2 == 0:
            x, y = increment_direction(x, y, direction)
            if (x, y) not in houses:
                houses[(x, y)] = 1
            else:
                houses[(x, y)] += 1
        else:
            a, b = increment_direction(a, b, direction)
            if (a, b) not in houses:
                houses[(a, b)] = 1
            else:
                houses[(a, b)] += 1
    return len(houses)


if __name__ == "__main__":
    print(at_least_one_present(string))

    print(coop_delivery(string))
