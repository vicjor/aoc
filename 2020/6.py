answers = []
with open("input6.txt", "r") as file:
    answers = [answer for answer in file]


grouped_answers = []
temp = []
# Group each group's answers in a list. Ignore line shifts ("\n")
for group in answers:
    if (group != "\n"):
        temp.append(group.strip("\n"))
    else:
        grouped_answers.append(temp)
        temp = []  # Set list to empty after adding a group


def count_group_answers(group):
    # Add all answers to a string. Return length of set (# unique answers within a group)
    string = ""
    for answer in group:
        for c in answer:
            string += c
    return len(set(string))


count = 0
# Count for each group
for group in grouped_answers:
    count += count_group_answers(group)

print("(Pt1) Sum of the count for answers to which _anyone_ in a group answered 'yes' is {}".format(count))


def count_all_yes(group):
    yes_count = 0  # Counter for questions _all_ group members answered yes to
    dict = {}  # Dict to keep track of count of each answer
    n = len(group)
    for a in group:  # Iterate through group, and count answers in dict
        for c in a:
            if (c in dict.keys()):
                dict[c] += 1
            else:
                dict[c] = 1
    for key_val in dict.items():  # Count all questions with n answers
        if (key_val[1] == n):
            yes_count += 1
    return yes_count


count = 0
for group in grouped_answers:
    count += count_all_yes(group)

print("(Pt2) Sum of questions _everyone_ in a group answered 'yes' to: {}".format(count))
