f = open("Day 4/input.txt", "r")

cardlist = f.read().split("\n")
cards = []
for i in cardlist:
	cards.append(i.split(": ")[1])

winningnums = []
yournums = []

for i in cards:
	winningnums.append(i.split(" | ")[0])
	yournums.append(i.split(" | ")[1])

total = 0
for i in range(len(winningnums)):
	points = 0
	wincount = 0
	winnum = winningnums[i].split(" ")
	yournum = yournums[i].split(" ")
	winnum = [x for x in winnum if x.strip()]
	yournum = [x for x in yournum if x.strip()]
	for ii in yournum:
		if ii in winnum:
			wincount += 1
	if wincount != 0:
		points = 1
		for i in range(wincount - 1):
			points += points
	total += points
print(total)