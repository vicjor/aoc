# --- Day 5: Doesn't He Have Intern-Elves For This? ---
# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:

# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
# How many strings are nice?

# --- Part Two ---
# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice.
# None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

# It contains a pair of any two letters that appears at least twice in the string without overlapping,
# like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
# For example:

# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
# How many strings are nice under these new rules?
from functools import reduce


def three_vowels(string) -> bool:
    vowels = "aeiou"
    count = 0
    for x in string:
        if x in vowels:
            count += 1
            if count == 3:
                return True
    return False


def double_letter(string) -> bool:
    n = len(string)
    for i in range(n-1):
        if string[i] == string[i+1]:
            return True
    return False


def no_forbidden_substring(string) -> bool:
    forbidden_substrings = ["ab", "cd", "pq", "xy"]
    for sub in forbidden_substrings:
        if sub in string:
            return False
    return True


def is_nice_string(string) -> bool:
    if three_vowels(string) and double_letter(string) and no_forbidden_substring(string):
        return True
    return False


def pair_appear_twice(string) -> bool:
    for i in range(len(string)-1):
        if string[i]+string[i+1] in string[i+2:]:
            return True
    return False


def repeat_one_between(string) -> bool:
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False


def is_nice_string_pt2(string) -> bool:
    if pair_appear_twice(string) and repeat_one_between(string):
        return True
    return False


if __name__ == "__main__":
    with open("input5.txt", "r") as file:
        strings = [line.strip("\n") for line in file]
    count = 0
    for s in strings:
        if is_nice_string(s):
            count += 1
    print("Part 1: There are %s nice strings " % count)
    # Part 1: There are 236 nice strings

    number_of_nice_strings = sum(map(
        lambda x: 1 if is_nice_string_pt2(x) else 0, strings))
    print("Part 2: There are %s nice strings " % number_of_nice_strings)
    # Part 2: There are 51 nice strings
