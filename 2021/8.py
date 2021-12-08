from time import perf_counter
from utils.filereader import file_reader
from typing import Dict, List

"""
Horrible brute force implementation to solve day 8. But it works.
"""

unique_segments = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

mixed_segments = {
    5: (2, 3, 5),
    6: (0, 6, 9),
}


def part1(notes: List[str]) -> int:
    """
    Count total number of 1, 4, 7 or 8's.
    :param entry list of strings with delimiter '|'. be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
    """
    count = 0
    for entry in notes:
        output = entry.split("|")[1].split(" ")
        for val in output:
            if len(val) in unique_segments:
                count += 1
    return count


def decode_signal_pattern(signal_pattern: List[str]) -> Dict[str, int]:
    """
    We know mapping for 1, 4, 7 and 8. Need to find mapping for 0,2,3,5,6,9.
    """
    decoded_segments = {}
    zero_six_nine = []
    two_three_five = []
    for i, _ in enumerate(signal_pattern):
        signal_pattern[i] = "".join(sorted(_))
    for elem in signal_pattern:
        if len(elem) in unique_segments:
            decoded_segments[unique_segments[len(elem)]] = elem
        elif len(elem) == 6:
            zero_six_nine.append(elem)
        else:
            two_three_five.append(elem)

    one = decoded_segments[1]
    four = decoded_segments[4]

    """Find 0, 6 and 9. """
    # Find 6
    for num in zero_six_nine:
        if one[0] in num and one[1] in num:
            continue
        decoded_segments[6] = num
    zero_six_nine.remove(decoded_segments[6])
    # Find 9
    for num in zero_six_nine:
        if four[0] in num and four[1] in num and four[2] in num and four[3] in num:
            decoded_segments[9] = num

    # Find 0
    zero_six_nine.remove(decoded_segments[9])
    decoded_segments[0] = zero_six_nine[0]
    six = decoded_segments[6]

    """Find 2, 3 and 5. """
    # Find 5
    for num in two_three_five:
        for _ in num:
            if _ not in six:
                break
            if _ == num[-1]:
                decoded_segments[5] = num

    # Find 3
    two_three_five.remove(decoded_segments[5])
    for num in two_three_five:
        if one[0] in num and one[1] in num:
            decoded_segments[3] = num
    # Find 2
    two_three_five.remove(decoded_segments[3])
    decoded_segments[2] = two_three_five[0]

    reverse_decoded = {v: k for k, v in decoded_segments.items()}
    return reverse_decoded


def part2(notes: List[str]) -> int:
    decoded_outputs = []
    for entry in notes:
        signal_pattern = entry.split("|")[0].split(" ")
        signal_pattern.remove("")
        output = entry.split("|")[1].split(" ")
        output.remove("")
        mapping = decode_signal_pattern(signal_pattern)
        out_str = ""
        for val in output:
            sorted_val = "".join(sorted(val))
            out_str += str(mapping[sorted_val])
        decoded_outputs.append(int(out_str))
    return sum(decoded_outputs)


def main():
    start = perf_counter()  # Start time

    notes = file_reader("data/input8.txt")
    print(f"Part 1: {part1(notes)}")
    print(f"Part 2: {part2(notes)}")  # 1016804

    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"Total runtime: {time} seconds.")


if __name__ == "__main__":
    main()
