#Part 1
import string

f = open("Day 3/Input.txt", "r")

rucksacklist = f.read().split("\n")

comp1 = []
comp2 = []
for i in rucksacklist:
    rucksacklen = len(i)
    complen = rucksacklen / 2
    complen = int(complen)
    comp1.append(i[:complen])
    comp2.append(i[complen:])


matches = []
for i in comp1:
    count = 0
    for ii in i:
        if ii in comp2[count]:
            matches.append(ii)
            break
        else:
            count += 1

score = 0
for i in matches:
    if i.islower():
        score += (string.ascii_lowercase.index(i) + 1)
    elif i.isupper():
        score += (26 + string.ascii_lowercase.index(i.lower()) + 1)
print(score)

#Part 2

matches = []
for i in range(int(len(rucksacklist)/3)):
    group = rucksacklist[(i*3):((i*3)+3)]
    for ii in group[0]:
        if ii in group[1] and ii in group[2]:
            matches.append(ii)
            break

score = 0
for i in matches:
    if i.islower():
        score += (string.ascii_lowercase.index(i) + 1)
    elif i.isupper():
        score += (26 + string.ascii_lowercase.index(i.lower()) + 1)

print(score)