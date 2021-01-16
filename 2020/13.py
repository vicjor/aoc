from os import error, times
from time import perf_counter
import sys

with open("input13.txt", "r") as file:
    data = [line.strip("\n") for line in file]
    EARLIST_TIME = int(data[0])
    ids = data[1].split(",")
    in_service = sorted([int(x) for x in ids if x != "x"])

# Bus ID : Earlist departure time possible
departure_times = {}
for bus_id in in_service:
    time = 0
    i = 1
    for i in range(EARLIST_TIME):
        if (i*bus_id >= EARLIST_TIME):
            time = i*bus_id
            break
        i += 1
    departure_times[bus_id] = time


def part1():
    departure = sys.maxsize
    bus_id = 0
    for key, time in departure_times.items():
        if EARLIST_TIME < time < departure:
            departure = time
            bus_id = key
    minutes = departure - EARLIST_TIME
    print("Minutes: {}\nBus ID: {}\nMin x ID: {} ".format(
        minutes, bus_id, minutes*bus_id))


part1()

# START PART 2
# Chinese remainder theorem: https://en.wikipedia.org/wiki/Chinese_remainder_theorem

# List of tuples with (bus_id, offset)
ids_offsets = [(int(ids[x]), x) for x in range(len(ids)) if ids[x] != "x"]

lcm = 1  # Least Common Multiple
timestamp = 0
for i in range(len(ids_offsets)-1):
    bus_id = ids_offsets[i+1][0]
    offset = ids_offsets[i+1][1]
    lcm *= ids_offsets[i][0]
    while (timestamp + offset) % bus_id != 0:
        timestamp += lcm  # Add product of all previous IDs until bus_id is common divider
print("\n(Pt2) Timestamp {}".format(timestamp))
