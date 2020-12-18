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
    for i in group:
        selections += i
    return selections

total = 0
for i in questions:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for ii in counting(i):
        for iii in alphabet:
            if iii in ii:
                alphabet.remove(iii)
                total += 1
print(total)