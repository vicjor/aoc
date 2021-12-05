
from time import perf_counter
from typing import List
from utils.filereader import file_reader


def gamma_rate(bits) -> str:
    """
    Input: List[str]
    Output: str
    Calculates the gamma rate from a list of string binary numbers. The gamma rate is a string of bits containing the most common bit for each position.
    """
    # List of all positions. Initially zeroes, but will contains the most common bit in that position and represent the gamma
    indices = [0 for x in range(12)]
    for index, b in enumerate(indices):
        zero, one = 0, 0
        for binary in bits:
            if binary[index] == "0":
                zero += 1
            else:
                one += 1
        if zero > one:
            indices[index] = "0"
        else:
            indices[index] = "1"
    return "".join(indices)  # convert list to string


def epsilon_rate(gamma) -> int:
    """
    Input: str
    Output: int
    Calculates the epsilon rate from the gamma_rate. The epsilon rate is a string of bits containing the most least bit for each position.
    """
    eps = ""
    for bit in gamma:
        if bit == "1":
            eps += "0"
        else:
            eps += "1"
    return int(eps, 2)


def most_common_bit_oxygen(bits, position) -> List[str]:
    """
    Takes a list of binary numbers and return a filtered list containing only the numbers with the most common bit. If equal, 1 is prioritized.
    params:
    * bits: List[str]
    * position: int
    """
    zero, one = 0, 0  # Count number of 0's and 1's to find most common bit
    for bit in bits:
        if bit[position] == "1":
            one += 1
        else:
            zero += 1
    filtered = []
    if (zero > one):
        for bit in bits:
            if bit[position] == "0":
                filtered.append(bit)

    else:
        for bit in bits:
            if bit[position] == "1":
                filtered.append(bit)
    return filtered


def least_common_bit_co2(bits, position) -> List[str]:
    """
    Takes a list of binary numbers and return a filtered list containing only the numbers with the least common bit. If equal, 0 is prioritized.
    :params bits: List of binary numbers
    bits: List[str]
    position: int
    """
    zero, one = 0, 0  # Count number of 0's and 1's to find least common bit

    for bit in bits:
        if bit[position] == "1":
            zero += 1
        else:
            one += 1
    filtered = []
    if (zero > one or zero == one):
        for bit in bits:
            if bit[position] == "0":
                filtered.append(bit)

    else:
        for bit in bits:
            if bit[position] == "1":
                filtered.append(bit)
    return filtered


def oxygen_generator_rating(bits: List[str]) -> int:
    """
    Calculates the oxygen generator rating.
    Filters the list of binaries until only one binary number remains.

    Iterate through each position, and filter the list of numbers keeping only the most common bit.

    :params List[str] bits: List of binary numbers
    :return: Oxygen generator rating
    :rtype: int
    """
    n = bits[0]
    for index, number in enumerate(n):
        if len(bits) == 1:
            break
        bits = most_common_bit_oxygen(bits, index)

    return int(bits[0], 2)


def co2_scrubber_rating(bits: List[str]) -> int:
    """
    Calculate the CO2 scrubber rating.
    Filters the list of binaries until only one binary number remains. 
    Iterate through each position, and filter the list of numbers keeping only the least common bit.

    :params bits: List of binary numbers represented as strings. 
    :return: CO2 scrubber rating
    :rtype: int
    """
    n = bits[0]
    for index, number in enumerate(n):
        if len(bits) == 1:
            break
        bits = least_common_bit_co2(bits, index)

    return int(bits[0], 2)


def main():
    start = perf_counter()  # Start time

    bits = file_reader("data/input3'.txt")

    print("## PART 1 ##")
    # Gamma rate represented as binary
    gamma_rate_bin = gamma_rate(bits)

    # Epsilon rate represented as integer
    epsilon_rate_int = epsilon_rate(gamma_rate_bin)

    # Gamma rate represented as integer
    gamma_rate_int = int(gamma_rate_bin, 2)

    power_consumption = epsilon_rate_int * gamma_rate_int
    print(f"Power consumption of submarine: {power_consumption}\n")  # 3959450

    print("## PART 2 ##")

    o_2 = oxygen_generator_rating(bits)
    co_2 = co2_scrubber_rating(bits)
    life_support_rating = o_2 * co_2
    print(f"Life support rating: {life_support_rating}.\n")  # 7440311

    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"Total runtime: {time} seconds.")


if __name__ == "__main__":
    main()
