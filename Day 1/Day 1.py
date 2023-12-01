import re
import numbers

f = open("Day 1/input.txt", "r")

wordlist = f.read().split("\n")

valuelist = []
for i in wordlist:
	x=re.findall(r'one|two|three|four|five|six|seven|eight|nine|zero|[0-9]', i)
	for ii in range(len(x)):
		if isinstance(x[ii], numbers.Number):
			break
		elif x[ii] == "one":
			x[ii] = "1"
		elif x[ii] == "two":
			x[ii] = "2"
		elif x[ii] == "three":
			x[ii] = "3"
		elif x[ii] == "four":
			x[ii] = "4"
		elif x[ii] == "five":
			x[ii] = "5"
		elif x[ii] == "six":
			x[ii] = "6"
		elif x[ii] == "seven":
			x[ii] = "7"
		elif x[ii] == "eight":
			x[ii] = "8"
		elif x[ii] == "nine":
			x[ii] = "9"
		elif x[ii] == "zero":
			x[ii] = "0"
	calvalues = int(str(x[0]) + str(x[-1]))
	valuelist.append(calvalues)
print(sum(valuelist))