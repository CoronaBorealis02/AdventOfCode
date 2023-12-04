f = open("C:/Users/up2068237/source/repos/CoronaBorealis02/AdventOfCode/Day 4/input.txt", "r")

cardlist = f.read().split("\n")
cards = []
for i in cardlist:
	cards.append(i.split(": ")[1])

winningnums = []
yournums = []

for i in cards:
	winningnums.append(i.split(" | ")[0])
	yournums.append(i.split(" | ")[1])


for i in range(len(winningnums)):
	points = 0
	wincount = 0
	winnum = winningnums[i].split(" ")
	yournum = yournums[i].split(" ")
	
	for ii in yournum:
		if ii in winnum:
			wincount += 1
	if wincount != 0:
		points = 1
		for i in range(wincount - 1):
			points += points
	print(points)