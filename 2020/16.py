with open("input16.txt", "r") as file:
    data = [line.strip("\n") for line in file]

blank_lines = [i for i, x in enumerate(data) if x == ""]
rules_raw = data[0:blank_lines[0]]

rules = {}
for rule in rules_raw:
    field, interval = rule.split(":")[0], rule.split(":")[1]
    interval1 = interval.split("or")[0].strip()
    interval2 = interval.split("or")[1].strip()
    interval1_lower = int(interval1.split("-")[0])
    interval1_upper = int(interval1.split("-")[1])
    interval2_lower = int(interval2.split("-")[0])
    interval2_upper = int(interval2.split("-")[1])
    interval = [i for i in range(interval1_lower, interval1_upper+1)]
    interval += [i for i in range(interval2_lower, interval2_upper+1)]
    rules[field] = interval

nearby_tickets_raw = data[blank_lines[1]+2::]
nearby_tickets = []
for ticket in nearby_tickets_raw:
    t = ticket.split(",")
    t = [int(i) for i in t]
    nearby_tickets.append(t)

# print(nearby_tickets)


invalid_numbers = []
invalid_tickets = []


def check_rule(ticket):
    for number in ticket:
        valid = False
        for rule in rules.values():
            if number in rule:
                valid = True
        if not valid:
            invalid_numbers.append(number)
            invalid_tickets.append(ticket)


for ticket in nearby_tickets:
    check_rule(ticket)

error_rate = sum(invalid_numbers)
print("(Pt 1) Ticket scanning error rate = {}".format(error_rate))


# Part 2
for invalid_ticket in invalid_tickets:
    nearby_tickets.remove(invalid_ticket)
