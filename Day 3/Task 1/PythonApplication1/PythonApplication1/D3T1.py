import textwrap
with open("input.txt") as textFile:
    skatelane = [line.split() for line in textFile]

for i in range(len(skatelane)):
    for ii in range(len(skatelane[i])):
        skatelane[i][ii] = list(skatelane[i][ii])

def trees():
    for i in range(len(skatelane), 1):
        for ii in range(len(skatelane[i]), 3):
            if skatelane[i][ii] == ".":
                return 0
            else:
                return 1


print(skatelane)