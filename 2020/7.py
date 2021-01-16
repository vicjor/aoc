import re

bags = []

with open("input7.txt", "r") as file:
    for line in file:
        bag = line.strip("\n").strip(".")
        bags.append(bag)


rules = {}  # Bag color as key, list of sub bags as value


# Awful parsing of lines
def parse_sub_bag(rule):
    sub_line = rule.split("contain")[1]
    for i in range(10):
        sub_line = sub_line.replace("{}".format(i), "")
    sub_line = sub_line.strip(" ")
    sub_bags = sub_line.split(",")
    for i in range(len(sub_bags)):
        sub_bags[i] = sub_bags[i].strip(".").replace(
            "bags", "").replace("bag", "").strip(" ")

    if (sub_bags[0] == "no other"):
        return []

    return sub_bags


def contain_shiny(bag):  # Recursive search for if a bag can contain a shiny gold bag
    other_bags = rules[bag]
    for sub_bag in other_bags:
        if (sub_bag == "shiny gold" or contain_shiny(sub_bag)):
            return True
    return False


def part1():
    count = 0
    for rule in bags:  # Add all rules to dict
        color = rule.split(" ")[0] + " " + rule.split(" ")[1]
        color = color.strip(" ")
        sub_bags = parse_sub_bag(rule)
        rules[color] = sub_bags

    for bag in rules.keys():
        if (contain_shiny(bag)):
            count += 1

    print("{} bags can eventually contain at least one shiny gold bag".format(count))


# part1()

# END PART 1

def parse_sub_bag2(rule):
    sub_line = rule.split("contain")[1]
    sub_line = sub_line.strip(" ")
    sub_bags = sub_line.split(",")
    for i in range(len(sub_bags)):
        sub_bags[i] = sub_bags[i].strip(".").replace(
            "bags", "").replace("bag", "").strip(" ")

    if (sub_bags[0] == "no other"):  # Add a empty list to dict if bag is empty
        return []

    return sub_bags


def sum_bags(bag):  # Recursive sum bags within a bag
    count = 0
    sub_bags = rules[bag]
    for bag in sub_bags:  # Sum N bags + N bags times thei sum of their content
        count += int(bag[0]) + int(bag[0]) * sum_bags(bag[2:])
    return count


def part2():
    for rule in bags:  # Add all rules to dict
        color = rule.split(" ")[0] + " " + rule.split(" ")[1]
        color = color.strip(" ")
        sub_bags = parse_sub_bag2(rule)
        rules[color] = sub_bags
    print("The shiny gold bag can eventually contain {} individual bags".format(
        sum_bags("shiny gold")))


part1()

part2()
