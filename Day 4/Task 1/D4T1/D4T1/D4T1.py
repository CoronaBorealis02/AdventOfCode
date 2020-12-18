import re
input = list(open("input.txt").readlines())

for i in range(len(input)):
    if input[i] == "\n":
        input[i] = "NewEnt"

formattedinput = []
for i in range(len(input)):
    input[i] = input[i].strip("\n")
    formattedinput += input[i].split()

stillformatting = "|".join(formattedinput)
stillgoing = []
stillgoing = stillformatting.split("NewEnt")

passport = []
for i in range(len(stillgoing)):
    passport.append(stillgoing[i].split("|"))

def isValid(passportinput):
    print(passportinput)
    passports = "#".join(passportinput)
    print(passports)
    pattern = r"((?:byr)|(?:iyr)|(?:eyr)|(?:hgt)|(?:hcl)|(?:ecl)|(?:pid))"
    matches = re.finditer(pattern, passports)
    matches = tuple(matches)
    print(len(matches))
    if len(matches) == 7:
        return 1
    else:
        return 0

count = 0
for i in range(len(passport)):
    count += isValid(passport[i])

print(count)