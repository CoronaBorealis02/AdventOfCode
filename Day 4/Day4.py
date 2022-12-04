
#PART 1

f = open("Day 4/Input.txt", "r")


def numberfill(start, end):
    numlist = []

    for i in range(int(start), int(end) + 1):
        numlist.append(i)
    return numlist



pairs = f.read().split("\n")

matchcount = 0
for i in pairs:
    elves = i.split(",")
    firstsector = elves[0].split("-")
    secondsector = elves[1].split("-")
    
    sector1range = numberfill(firstsector[0], firstsector[1])
    sector2range = numberfill(secondsector[0], secondsector[1])

    if int(secondsector[0]) in sector1range and int(secondsector[1]) in sector1range or int(firstsector[0]) in sector2range and int(firstsector[1]) in sector2range:
        matchcount += 1



print(matchcount)

#PART 2

overlapcount = 0
for i in pairs:
    elves = i.split(",")
    firstsector = elves[0].split("-")
    secondsector = elves[1].split("-")
    
    sector1range = numberfill(firstsector[0], firstsector[1])
    sector2range = numberfill(secondsector[0], secondsector[1])

    if int(secondsector[0]) in sector1range or int(secondsector[1]) in sector1range or int(firstsector[0]) in sector2range or int(firstsector[1]) in sector2range:
        overlapcount += 1

print(overlapcount)