import re
data = []

with open("input4.txt", "r") as file:
    data = file.readlines()

string = ""

for i in data:
    string += i

data = string.split("\n\n")

fields = ["hgt", "ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]


valid_passports = 0
for credentials in data:
    valid = True
    for field in fields:
        if (field not in credentials):
            valid = False
    if (valid):
        valid_passports += 1

print("Valid Passports (pt1): {}".format(valid_passports))


# Part 2
data2 = []

for credential in data:
    data2.append(re.split(r"\s|\n", credential))


def check_valid_credentials(credential):
    # Basic check if all required fields are present
    valid = True
    string = ""
    for c in credential:
        string += c
    for field in fields:
        if (field not in string):
            return False

    # Check for validity of fields
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for cred in credential:
        key_val = cred.split(":")

        # print(key_val)
        if (key_val[0] == "hgt"):
            if (key_val[1][-2:] == "cm"):
                try:
                    height = int(key_val[1][0:-2])
                    if (height < 150 or height > 193):
                        return False
                except:
                    return False
            elif (key_val[1][-2:] == "in"):
                try:
                    height = int(key_val[1][0:2])
                    if (height < 59 or height > 76):
                        return False
                except:
                    return False
            else:
                return False
        if (key_val[0] == "byr"):
            if (len(key_val[1]) != 4):
                return False
            elif (int(key_val[1]) < 1920 or int(key_val[1]) > 2002):
                return False
        if (key_val[0] == "iyr"):
            if (len(key_val[1]) != 4):
                return False
            elif (int(key_val[1]) < 2010 or int(key_val[1]) > 2020):
                return False
        if (key_val[0] == "eyr"):
            if (len(key_val[1]) != 4):
                return False
            if (int(key_val[1]) < 2020 or int(key_val[1]) > 2030):
                return False
        if (key_val[0] == "hcl"):
            if not (re.search('#[0-9a-f]{6}', key_val[1])):
                return False
        if (key_val[0] == "ecl"):
            if (key_val[1] not in eye_colors):
                return False
        if (key_val[0] == "pid"):
            if not (re.search("^[0-9]{9}$", key_val[1])):
                return False
    return True

# Most readable summing
# count = 0
# for cred in data2:
#     if (check_valid_credentials(cred)):
#         count += 1


# One-liner for sum
count = sum([1 for cred in data2 if check_valid_credentials(cred)])
print("Valid passports (pt2): {}".format(count))
