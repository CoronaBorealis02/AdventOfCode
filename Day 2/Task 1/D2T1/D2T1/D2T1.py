import re
import numpy as np

input = open("input.txt").readlines()

splitinput = []
for i in input:
    splitinput.append(i.split())

def isValid(range, char, string):
    counter = 0
    rangear = range.split("-")
    char = list(char)
    match = list(string)
    for i in match:
        if i == char[0]:
            counter += 1
    if counter <= int(rangear[1]) and counter >= int(rangear[0]):
        return 1
    else:
        return 0

count = 0
for x in range(len(splitinput)):
    count += isValid(splitinput[x][0], splitinput[x][1], splitinput[x][2])

print(count)