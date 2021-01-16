import time
from collections import defaultdict


with open("input14.txt", "r") as file:
    data = [line.strip("\n") for line in file]

instructions = []
new = [data[0]]
for line in data[1:]:
    content = line.split(" = ")
    if ("mask" in line):
        instructions.append(new)
        new = [line]
    else:
        new.append(line)
instructions.append(new)


def part1():
    mem = defaultdict(int)
    locations = set()

    for line in instructions:
        mask = line[0].split(" = ")[1]
        for m in line[1:]:
            adress = int(m.split(" = ")[0][4:-1])
            mem_value = int(m.split(" = ")[1])

            binary = bin(mem_value)[2:]
            binary = (36 - len(binary))*"0" + binary

            result = ""
            for index, bit in enumerate(binary):
                if (mask[index] != "X"):
                    result += mask[index]
                else:
                    result += bit
            mem[adress] = int(result, 2)
            locations.add(adress)

    # Sum values of all memory locations
    mem_sum = sum([mem[loc] for loc in locations])

    print("(Pt1) Sum of values in memory = {}".format(mem_sum))  # 13105044880745


start = time.perf_counter()
part1()  # 13105044880745
end = time.perf_counter()
print("Completed in {} seconds".format(end-start))


# PART 2
# Input: Bitstring with floating bits
# Output: 2^N adresses without floating bits; N = number of floating bits
def convert_floating_bits(bitstring):
    adresses = []
    # Indices of all X's

    float_indices = [i for i in range(
        len(bitstring)) if bitstring.startswith('X', i)]
    temp = bitstring
    for i in float_indices:
        temp = list(temp)
        temp[i] = "1"
        adresses.append("".join(temp))
        temp = list(temp)
        temp[i] = "0"
        adresses.append("".join(temp))
    for k in adresses:
        if (k.count("X") > 0):
            x_index = set([i for i in range(len(k)) if k.startswith('X', i)])
            j = x_index.pop()
            temp = list(k)
            temp[j] = "1"
            adresses.append("".join(temp))
            temp = list(k)
            temp[j] = "0"
            adresses.append("".join(temp))

    memory_adresses = set()
    # Iterate over all generated addresses and add the non-float addresses to a set
    for adress in adresses:
        if (adress.count("X") == 0):
            memory_adresses.add(adress)
    return memory_adresses


def part2():
    mem = defaultdict(int)
    locations = set()  # Save all unique memory locations
    for line in instructions:
        mask = line[0].split(" = ")[1]
        for m in line[1:]:
            adress = int(m.split(" = ")[0][4:-1])
            mem_value = int(m.split(" = ")[1])

            binary = bin(adress)[2:]
            binary = (36 - len(binary))*"0" + binary

            result = ""  # Bitstring after applying mask
            for index, bit in enumerate(binary):
                if (mask[index] == "0"):
                    result += bit
                elif (mask[index] == "1"):
                    result += "1"
                else:
                    result += "X"
            all_memory_addresses = convert_floating_bits(result)
            for adress in all_memory_addresses:
                mem[adress] = mem_value
                locations.add(adress)

    # Sum all values in memory
    mem_sum = sum([mem[adress] for adress in locations])

    print("(Pt 2) Sum of all values in memory = {}".format(mem_sum))


start = time.perf_counter()
part2()  # 3505392154485
end = time.perf_counter()
print("Completed in {} seconds".format(end-start))
