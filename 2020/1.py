from time import perf_counter

with open("input1.txt", "r") as file:
    liste = [int(line) for line in file]

# Part one


def part1():
    prod1 = 0
    for num1 in liste:
        for num2 in liste:
            if (num1 + num2 == 2020):
                prod1 = num1*num2
                print(
                    "The product of the two entries that sum to 2020: {}"
                    .format(prod1))
                return prod1


start = perf_counter()
part1()
end = perf_counter()
print("Time pt1: {} (O(n^2) where n={})\n".format(end-start, len(liste)))


# Part two


def part2():
    prod2 = 0
    for num1 in liste:
        for num2 in liste:
            for num3 in liste:
                if (num1 + num2 + num3 == 2020):
                    prod2 = num1*num2*num3
                    print(
                        "The product of the three entries that sum to 2020: {}"
                        .format(prod2))
                    return prod2


start = perf_counter()
part2()
end = perf_counter()
print("Time pt1: {} (O(n^3) where n={})".format(end-start, len(liste)))
