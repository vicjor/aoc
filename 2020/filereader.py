def file_reader(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(line.strip("\n"))
    return lines


def file_reader_int(filename):
    lines = []
    with open(filename, "r") as file:
        for line in file:
            lines.append(int(line.strip("\n")))
    return lines
