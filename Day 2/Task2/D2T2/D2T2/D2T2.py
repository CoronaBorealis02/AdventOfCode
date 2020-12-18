input = open("input.txt").readlines()

splitinput = []
for i in input:
    splitinput.append(i.split())

def isValid(range, char, string):
    counter = 0
    rangear = range.split("-")
    char = list(char)
    match = list(string)
    if match[int(rangear[0]) - 1] == char[0] and match[int(rangear[1]) - 1] == char[0]:
        return 0
    elif match[int(rangear[0]) - 1] == char[0]:
        return 1
    elif match[int(rangear[1]) - 1] == char[0]:
        return 1
    else:
        return 0

count = 0
for x in range(len(splitinput)):
    count += isValid(splitinput[x][0], splitinput[x][1], splitinput[x][2])

print(count)