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

questions = []
for i in range(len(stillgoing)):
	questions.append(stillgoing[i].split("|"))

def counting(group):
	selections = ""
	nopep = len(group)
	for i in group:
		selections += i
	
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	totalll = 0
	total = 0
	for ii in selections:
		for iii in alphabet:
			if iii in ii:
				total += 1
		if total == nopep:
			totalll += 1
		else:
			totalll += 0
	return totalll
totall = 0
for i in questions:
	totall += counting(i)
print(totall)