
# data = [0, 3, 6]  # Test input
data = [1, 17, 0, 10, 18, 11, 6]

history = {}


def next_number(number, turn):
    if number not in history:
        history[number] = [turn]
        return 0
    else:
        history[number].append(turn)
        history[number] = history[number][-2::]
        return history[number][-1] - history[number][-2]


def memory_game(limit):
    spoken = 0
    for turn in range(0, limit-1):
        if turn < len(data):
            spoken = next_number(data[turn], turn)
        else:
            spoken = next_number(spoken, turn)
    print("Turn: {}, Spoken: {}".format(turn+2, spoken))


memory_game(2020)  # Pt1: 595
history = {}  # Clear history dict before pt2
memory_game(30000000)  # Pt2: 1708310
