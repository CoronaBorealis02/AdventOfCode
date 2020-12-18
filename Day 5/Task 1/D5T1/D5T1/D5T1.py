
import numpy as np
input = open("input.txt").readlines()


for i in range(len(input)):
	input[i] = input[i].strip("\n")

def IDFinder(input):
	operations = list(input)
	rangestart = 0
	rangeend = 127
	for i in range(7):
		if operations[i] == "F":
			rangeend = np.floor((np.floor(rangeend - rangestart) / 2) + rangestart)
		elif operations[i] == "B":
			rangestart = np.ceil((np.ceil(rangeend - rangestart) / 2) + rangestart)
	row = rangestart
	rangestart = 0
	rangeend = 7
	for i in range(7,10):
		if operations[i] == "L":
				rangeend = np.floor((np.floor(rangeend - rangestart) / 2) + rangestart)
		elif operations[i] == "R":
			rangestart = np.ceil((np.ceil(rangeend - rangestart) / 2) + rangestart)
	column = rangestart
	return (row * 8) + column
max = 0
for i in input:

	if IDFinder(i) > max:
		max = IDFinder(i)
print(max)