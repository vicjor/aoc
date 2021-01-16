from collections import defaultdict
from filereader import file_reader_int
data = file_reader_int("input10.txt")
data = sorted(data)


def part1():
    one = 0
    two = 0
    three = 0
    if (data[0] == 1):  # If the first adapter is of one volt, increment 1
        one += 1
    else:  # Else increment 3-jolt by one
        three += 1
    for x in range(len(data)-1):
        if (data[x+1] - data[x] == 1):
            one += 1
        elif (data[x+1] - data[x] == 2):
            two += 1
        elif (data[x+1] - data[x] == 3):
            three += 1
    # Always increment 3-jolt by one extra (device-jolt minus highest adapter jolt = 3)
    three += 1
    print("""The product of 1-jolt differences and 3-jolt differences is
    {}({} * {} = {})""".format(one * three, one, three, one*three))


part1()


def part2():
    paths = defaultdict(int)  # Dict with int (0) as default value
    paths[0] = 1
    jolts = [0, *data]
    for adapter in jolts:
        for diff in range(1, 4):
            next_adapter = adapter + diff
            if (next_adapter in jolts):  # Add path only if current jolt + diff is a existing jolt
                # of path for next jolt is sum of all paths to next
                paths[next_adapter] += paths[adapter]
    number_of_paths = paths[jolts[-1]]
    print(number_of_paths)
    return number_of_paths


part2()
