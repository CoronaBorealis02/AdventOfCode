#PART ONE

f = open("Day 2/Input.txt", "r")
rounds = []
rounds = f.read().split("\n")

score = 0
for i in rounds:
    match = i.split(" ")
    opp = match[0]
    counter = match[1]
    if opp == "A": #ROCK
        if counter == "X": #ROCK
            score += 4
        elif counter == "Y": #PAPER
            score += 8
        elif counter == "Z": #SCISSORS
            score += 3
    elif opp == "B": #PAPER
        if counter == "X": #ROCK
            score += 1
        elif counter == "Y": #PAPER
            score += 5
        elif counter == "Z": #SCISSORS
            score += 9
    elif opp == "C": #SCISSORS
        if counter == "X": #ROCK
            score += 7
        elif counter == "Y": #PAPER
            score += 2
        elif counter == "Z": #SCISSORS
            score += 6

print(score)

#PART 2

score = 0
for i in rounds:
    match = i.split(" ")
    opp = match[0]
    counter = match[1]
    if opp == "A": #ROCK
        if counter == "Y": #DRAW - ROCK
            score += 4
        elif counter == "Z": #WIN - PAPER
            score += 8
        elif counter == "X": #LOSS - SCISSORS
            score += 3
    elif opp == "B": #PAPER
        if counter == "X": #LOSS - ROCK
            score += 1
        elif counter == "Y": #DRAW - PAPER
            score += 5
        elif counter == "Z": #WIN - SCISSORS
            score += 9
    elif opp == "C": #SCISSORS
        if counter == "Z": #WIN - ROCK
            score += 7
        elif counter == "X": #LOSS - PAPER
            score += 2
        elif counter == "Y": #DRAW - SCISSORS
            score += 6

print(score)