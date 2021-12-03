# --- Day 6: Probably a Fire Hazard ---
# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?
# --- Part Two ---
# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

# The phrase turn on actually means that you should increase the brightness of those lights by 1.

# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

# The phrase toggle actually means that you should increase the brightness of those lights by 2.

# What is the total brightness of all lights combined after following Santa's instructions?

# For example:

# turn on 0,0 through 0,0 would increase the total brightness by 1.
# toggle 0,0 through 999,999 would increase the total brightness by 2000000.

# Init 1000 x 1000 grid with zeroes
grid = [[0 for i in range(1000)] for j in range(1000)]


def turn_on(x0, y0, x, y):
    for lighty in range(y0, y+1):
        for lightx in range(x0, x+1):
            grid[lighty][lightx] = 1


def turn_off(x0, y0, x, y):
    for lighty in range(y0, y+1):
        for lightx in range(x0, x+1):
            grid[lighty][lightx] = 0


def toggle(x0, y0, x, y):
    for lighty in range(y0, y+1):
        for lightx in range(x0, x+1):
            grid[lighty][lightx] = int(not bool(grid[lighty][lightx]))


def turn_on2(x0, y0, x, y):
    for lighty in range(y0, y+1):
        for lightx in range(x0, x+1):
            grid[lighty][lightx] += 1


def turn_off2(x0, y0, x, y):
    for lighty in range(y0, y+1):
        for lightx in range(x0, x+1):
            if grid[lighty][lightx] > 0:
                grid[lighty][lightx] -= 1


def toggle2(x0, y0, x, y):
    for lighty in range(y0, y+1):
        for lightx in range(x0, x+1):
            grid[lighty][lightx] += 2


def parse_instructions(instruction):
    instruction_list = instruction.split(" ")
    if len(instruction_list) == 4:
        action = instruction_list[0]
        x0, y0 = int(instruction_list[1].split(",")[0]), int(
            instruction_list[1].split(",")[1])

        x, y = int(instruction_list[3].split(",")[0]), int(
            instruction_list[3].split(",")[1])
    else:
        action = instruction_list[0]+" " + instruction_list[1]
        x0, y0 = int(instruction_list[2].split(",")[0]), int(
            instruction_list[2].split(",")[1])
        x, y = int(instruction_list[4].split(",")[0]), int(
            instruction_list[4].split(",")[1])

    if action == "turn on":
        turn_on(x0, y0, x, y)
    elif action == "turn off":
        turn_off(x0, y0, x, y)
    else:
        toggle(x0, y0, x, y)


def parse_instructions2(instruction):
    instruction_list = instruction.split(" ")
    if len(instruction_list) == 4:
        action = instruction_list[0]
        x0, y0 = int(instruction_list[1].split(",")[0]), int(
            instruction_list[1].split(",")[1])

        x, y = int(instruction_list[3].split(",")[0]), int(
            instruction_list[3].split(",")[1])
    else:
        action = instruction_list[0]+" " + instruction_list[1]
        x0, y0 = int(instruction_list[2].split(",")[0]), int(
            instruction_list[2].split(",")[1])
        x, y = int(instruction_list[4].split(",")[0]), int(
            instruction_list[4].split(",")[1])

    if action == "turn on":
        turn_on2(x0, y0, x, y)
    elif action == "turn off":
        turn_off2(x0, y0, x, y)
    else:
        toggle2(x0, y0, x, y)


if __name__ == "__main__":
    with open("input6.txt", "r") as file:
        instructions = [line.strip("\n") for line in file]
    for instruction in instructions:
        parse_instructions(instruction)
    lights_on = sum([sum(row) for row in grid])
    print("%s lights are turned on after executing instructions" % lights_on)
    # 543903 lights are turned on after executing instructions

    grid = [[0 for i in range(1000)] for j in range(1000)]
    for instruction in instructions:
        parse_instructions2(instruction)
    total = sum([sum(row) for row in grid])
    print("%s is the total brightness" % total)
    # 14687245 is the total brightness
