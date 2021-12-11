from time import perf_counter
from utils.filereader import file_reader, file_reader_int
from typing import List


def get_invalid_character(line: str) -> bool:
    stack = []
    for char in line:
        if char in '([{<':
            stack.append(char)
        else:
            peek = stack.pop()
            if char == ')' and peek != '(':
                return char
            if char == ']' and peek != '[':
                return char
            if char == '}' and peek != '{':
                return char
            if char == ">" and peek != '<':
                return char


def syntax_error_score(lines: List[str]) -> int:
    """Return sum of syntax error scores."""
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    invalid_characters = [get_invalid_character(
        line) for line in lines if get_invalid_character(line) != None]
    return sum([points[char] for char in invalid_characters])


def get_missing_characters(line: str) -> List[str]:
    missing_characters = []
    stack = []
    characters = {'(': ')', '[': ']', '{': '}', '<': '>'}
    for char in line:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            stack.pop()
    missing_characters = [characters[char] for char in stack]
    missing_characters.reverse()
    return missing_characters


def get_middle_score(lines: List[str]) -> int:
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    missing_characters = [get_missing_characters(line) for line in lines]
    scores = []
    for line in missing_characters:
        score = 0
        for char in line:
            score *= 5
            score += points[char]
        scores.append(score)
    scores = sorted(scores)
    n = len(scores)
    return scores[n//2]


def main():
    lines = file_reader("data/input10.txt")
    print("Total score: ", syntax_error_score(lines))
    incomplete_lines = [x for x in lines if get_invalid_character(x) == None]
    middle_score = get_middle_score(incomplete_lines)
    print(f"Middle score: {middle_score}")


if __name__ == "__main__":
    start = perf_counter()  # Start time
    main()
    end = perf_counter()  # End time
    time = end-start  # Total runtime
    print(f"Total runtime: {time} seconds.")
