#PART 1

f = open("Day 5/Input.txt", "r")

Instructions = f.read().split("\n")

s1 = ["B", "V", "S", "N", "T", "C", "H", "Q"]
s2 = ["W", "D", "B", "G"]
s3 = ["F", "W", "R", "T", "S", "Q", "B"]
s4 = ["L", "G", "W", "S", "Z", "J", "D", "N"]
s5 = ["M", "P", "D", "V", "F"]
s6 = ["F", "W", "J"]
s7 = ["L", "N", "Q", "B", "J", "V"]
s8 = ["G", "T", "R", "C", "J", "Q", "S", "N"]
s9 = ["J", "S", "Q", "C", "W", "D", "M"]

stacks = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

for line in Instructions:
    numins = [int(i) for i in line.split() if i.isdigit()]
    amount = numins[0]
    start = numins[1]
    end = numins[2]

    for i in range(amount):
        stacks[(end - 1)].append(stacks[(start - 1)].pop())

for i in stacks:
    print(i.pop())

print("-----")

#PART 2

s1 = ["B", "V", "S", "N", "T", "C", "H", "Q"]
s2 = ["W", "D", "B", "G"]
s3 = ["F", "W", "R", "T", "S", "Q", "B"]
s4 = ["L", "G", "W", "S", "Z", "J", "D", "N"]
s5 = ["M", "P", "D", "V", "F"]
s6 = ["F", "W", "J"]
s7 = ["L", "N", "Q", "B", "J", "V"]
s8 = ["G", "T", "R", "C", "J", "Q", "S", "N"]
s9 = ["J", "S", "Q", "C", "W", "D", "M"]

stacks = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

for line in Instructions:
    numins = [int(i) for i in line.split() if i.isdigit()]
    amount = numins[0]
    start = numins[1]
    end = numins[2]

    for i in range(amount, 0, -1):
            stacks[(end - 1)].append(stacks[(start - 1)].pop(-i))
for i in stacks:
        print(i.pop())