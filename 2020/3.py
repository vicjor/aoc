import time
file = open("input3.txt")
text = file.readlines()
file.close()


def traverse_forest():
    position = 0
    tree_count = 0

    for row in text:
        row = row.strip("\n")
        if (row[position % len(row)] == "#"):
            tree_count += 1
        position += 3

    print("{} trees encountered (pt1)".format(tree_count))


start = time.perf_counter()
traverse_forest()
end = time.perf_counter()
print("Time pt1: {}".format(end-start))


# Part 2
def traverse_forest2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    current_slope = 0

    trees = []

    for slope in slopes:
        count = 0
        position = [0, 0]
        for line in range(0, len(text), slope[1]):
            row = text[line][:-1].strip("\n")
            if (row[position[0] % len(row)] == "#"):
                count += 1
            position[0] += slope[0]
        trees.append(count)
    product = 1
    for result in trees:
        product *= result

    print("Product of trees encountered for each slope: {}".format(product))


start = time.perf_counter()
traverse_forest2()
end = time.perf_counter()
print("Time pt2: {}".format(end-start))
