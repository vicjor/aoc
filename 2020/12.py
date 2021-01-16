import time
import sys

print(sys.path)
with open("input12.txt", "r") as file:
    instructions = [line.strip("\n") for line in file]


def part1():
    # 0 degree = E, 90 = S (-N), 180 = W (-E), 270 = N, 360 = 0 = E
    degree = 0

    # Only need North and East variables. Subtract S/W values.
    N = 0
    E = 0

    for instruction in instructions:
        if (instruction[0] == "N"):
            N += int(instruction[1:])
        elif (instruction[0] == "S"):
            N -= int(instruction[1:])
        elif (instruction[0] == "E"):
            E += int(instruction[1:])
        elif (instruction[0] == "W"):
            E -= int(instruction[1:])
        elif (instruction[0] == "L"):
            # Modulo to ensure degree stay within [0, 360>
            degree = (degree - int(instruction[1:])) % 360
        elif (instruction[0] == "R"):
            degree = (degree + int(instruction[1:])) % 360
        elif (instruction[0] == "F"):
            # Set of possible degree values (0, 90, 180, 270)
            if (degree == 0):
                E += int(instruction[1:])
            elif (degree == 90):
                N -= int(instruction[1:])
            elif (degree == 180):
                E -= int(instruction[1:])
            elif (degree == 270):
                N += int(instruction[1:])

    # Manhattan distance = abs(E - W) + abs(N - S)
    # Since we have subtracted W and S along the way, our correct formula is
    # abs (E) + abs(N)
    print("Manhattan distance pt1 {}".format(abs(E) + abs(N)))
    return abs(E) + abs(N)


start = time.perf_counter()
part1()  # Result: 1007
end = time.perf_counter()
print("Time pt1: {}\n".format(end - start))


def part2():
    # Waypoint coordinates is relative to the ship
    waypoint = [1, 10]  # [N, E]
    ship = [0, 0]  # [N, E]
    degree = 0

    for instruction in instructions:
        if (instruction[0] == "N"):
            waypoint[0] += int(instruction[1:])
        elif (instruction[0] == "S"):
            waypoint[0] -= int(instruction[1:])
        elif (instruction[0] == "E"):
            waypoint[1] += int(instruction[1:])
        elif (instruction[0] == "W"):
            waypoint[1] -= int(instruction[1:])
        elif (instruction[0] == "L"):
            degree = int(instruction[1:])

            # Rotate waypoint 90 degrees left. E.g. [10, 1] -> [1, -10]
            if (degree == 90):
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
            # Rotate waypoint 180 degrees. E.g. [10, 1] -> [-10, -1]
            elif (degree == 180):
                waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
            # Rotate waypoint 270 degrees left. E.g. [10, 1] -> [-1, 10]
            elif (degree == 270):
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
        elif (instruction[0] == "R"):
            degree = int(instruction[1:])

            # Rotate waypoint 90 degrees right. E.g. [10, 1] -> [-1, 10]
            if (degree == 90):
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
            # Rotate waypoint 180 degrees. E.g. [10, 1] -> [-10, -1]
            elif (degree == 180):
                waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
            # Rotate waypoint 270 degrees right. E.g. [10, 1] -> [1, -10]
            elif (degree == 270):
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]

        elif (instruction[0] == "F"):
            # Set of possible degree values (0, 90, 180, 270)
            ship[0] += int(instruction[1:])*waypoint[0]
            ship[1] += int(instruction[1:])*waypoint[1]

    print("Manhattan distance pt2: {}".format(abs(ship[0]) + abs(ship[1])))
    return abs(ship[0]) + abs(ship[1])


start = time.perf_counter()
part2()  # Result 41212
end = time.perf_counter()
print("Time pt2: {}".format(end - start))
