instructions = {}
with open("input8.txt", "r") as file:
    for index, line in enumerate(file):
        instructions[index] = [line.strip("\n"), False]


def execute(operation):
    op, val = operation.split(" ")[0], operation.split(" ")[1]
    if (op == "jmp"):
        return ("jmp", int(val))
    elif (op == "nop"):
        return ("nop", int(val))
    else:
        return ("acc", int(val))


def part1():
    acc = 0
    pointer = 0
    while True:
        instruction = instructions[pointer]
        if (instruction[1]):
            print("Acc value when entering loop: {}".format(acc))
            break
        instructions[pointer][1] = True
        nxt = execute(instruction[0])
        if (nxt[0] == "pointer"):
            pointer += nxt[1]
        elif (nxt[0] == "nop"):
            pointer += 1
        elif (nxt[0] == "acc"):
            acc += nxt[1]
            pointer += 1


nop_index = 0
jmp_index = 0

# Count all nop and jmp
for key in instructions.keys():
    if (instructions[key][0][0:3] == "nop"):
        nop_index += 1
    elif (instructions[key][0][0:3] == "jmp"):
        jmp_index += 1


def reset_dict(dict):
    for key in dict.keys():
        dict[key][1] = False


def part2():

    instructions_copy = instructions.copy()
    acc = 0
    pointer = 0
    jmp_pointer, jmp_counter = 0, 0
    nop_pointer, nop_counter = 0, 0

    while True:
        # When trying to an instruction after the last, program is fixed
        if (pointer == len(instructions_copy)-1):
            print("No loop! Terminating accumulator value is {}.".format(acc))
            break
        elif (instructions_copy[pointer][1]):  # If loop
            # Reset all parameters and start over by swapping either the next jmp or nop
            print("Loop. Increment jmp/nop pointer and reset parameters. Nop: {}, Jmp: {}, Acc: {}, Pointer: {}".format(
                nop_pointer, jmp_pointer, acc, pointer))
            jmp_counter, nop_counter, pointer, acc = 0, 0, 0, 0
            if (jmp_pointer <= jmp_index - 1):  # Unless swapping all jmp instructions , swap next
                jmp_pointer += 1
            # If all jmp has been attempted swapped, swap next nop
            elif (nop_pointer <= nop_index - 1):
                nop_pointer += 1
            reset_dict(instructions_copy)  # Set all booleans back to False

        instruction = instructions_copy[pointer]
        instructions_copy[pointer][1] = True
        nxt = execute(instruction[0])
        if (nxt[0] == "jmp"):
            if (jmp_counter != 0 and jmp_pointer != 0 and jmp_counter == jmp_pointer):
                # Swap to nop
                pointer += 1
            else:
                if (pointer + nxt[1] >= 0):
                    pointer += nxt[1]
            jmp_counter += 1
        elif (nxt[0] == "nop"):
            if (nop_counter != 0 and nop_pointer != 0 and nop_counter == nop_pointer):
                # Swap to jmp
                pointer += nxt[1]
            else:
                pointer += 1
            nop_counter += 1
        elif (nxt[0] == "acc"):

            acc += nxt[1]
            pointer += 1


part1()  # Acc value when entering loop is 28
part2()  # Terminating acc value is 1056
