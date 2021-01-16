import time
passwords = []

with open("input2.txt", "r") as file:
    passwords = [line for line in file]


def part1():
    valid = 0
    for line in passwords:
        split = line.split(" ")
        min_occurence = split[0].split("-")[0]
        max_occurence = split[0].split("-")[1]
        letter = split[1][0]
        password = split[2]

        if (password.count(letter) >= int(min_occurence) and password.count(letter) <= int(max_occurence)):
            valid += 1
    print("Valid passwords pt1: {}".format(valid))


start = time.perf_counter()
part1()
end = time.perf_counter()
print("Time pt2: {}\n".format(end-start))


def part2():
    valid = 0
    for line in passwords:
        split = line.split(" ")
        first = int(split[0].split("-")[0])
        second = int(split[0].split("-")[1])
        letter = split[1][0]
        password = split[2]

        if (password[first - 1] == letter and not password[second-1] == letter or not password[first - 1] == letter and password[second-1] == letter):
            valid += 1
    print("Valid passwords pt2: {}".format(valid))


start = time.perf_counter()
part2()
end = time.perf_counter()

print("Time pt2: {}".format(end-start))
