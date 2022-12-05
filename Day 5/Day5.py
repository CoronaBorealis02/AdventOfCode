#PART 1

f = open("Day 5/Input.txt", "r")

Instructions = f.read().split("\n")

def resetstacks():
    originalstacks = [["B", "V", "S", "N", "T", "C", "H", "Q"],
                      ["W", "D", "B", "G"],
                      ["F", "W", "R", "T", "S", "Q", "B"],
                      ["L", "G", "W", "S", "Z", "J", "D", "N"],
                      ["M", "P", "D", "V", "F"],
                      ["F", "W", "J"],
                      ["L", "N", "Q", "B", "J", "V"],
                      ["G", "T", "R", "C", "J", "Q", "S", "N"],
                      ["J", "S", "Q", "C", "W", "D", "M"]]
    return originalstacks


stacks = resetstacks()

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

stacks = resetstacks()

for line in Instructions:
    numins = [int(i) for i in line.split() if i.isdigit()]
    amount = numins[0]
    start = numins[1]
    end = numins[2]

    for i in range(amount, 0, -1):
            stacks[(end - 1)].append(stacks[(start - 1)].pop(-i))
for i in stacks:
        print(i.pop())