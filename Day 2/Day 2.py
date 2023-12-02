
f = open("Day 2/input.txt", "r")

games = f.read().split("\n")
counter = 0
game = 0
for i in range(len(games)):
    game += 1
    splitgame = games[i].split(": ")
    games[i] = splitgame[-1]
    colonsplit = games[i].split("; ")
    games[i] = colonsplit
    colours = []
    for ii in range(len(games[i])):
        colours.append(games[i][ii].split(", "))
    gamecandidate = True
    greencheck = True
    redcheck = True
    bluecheck = True
    for iii in range(len(colours)):
        colourindex = []
        for iiii in range(len(colours[iii])):
            colourindex.append(colours[iii][iiii].split(" "))
        for iiiii in colourindex:
            if iiiii[1] == "green":
                if int(iiiii[0]) > 13:
                    greencheck = False
            elif iiiii[1] == "red":
                if int(iiiii[0]) > 12:
                    redcheck = False
            elif iiiii[1] == "blue":
                if int(iiiii[0]) > 14:
                    bluecheck = False
        if greencheck == False or redcheck == False or bluecheck == False:
            gamecandidate = False
            break
    if gamecandidate == True:
        counter += game
print(counter)

# part 2
f = open("Day 2/input.txt", "r")

games = f.read().split("\n")
total = 0
for i in range(len(games)):
    splitgame = games[i].split(": ")
    games[i] = splitgame[-1]
    colonsplit = games[i].split("; ")
    games[i] = colonsplit
    #print(games[i])
    colours = []
    for ii in range(len(games[i])):
        colours.append(games[i][ii].split(", "))
    green = 0
    red = 0
    blue = 0
    for iii in range(len(colours)):
        colourindex = []
        for iiii in range(len(colours[iii])):
            colourindex.append(colours[iii][iiii].split(" "))
        for iiiii in colourindex:
            if iiiii[1] == "green":
                if int(iiiii[0]) > green:
                    green = int(iiiii[0])
            if iiiii[1] == "red":
                if int(iiiii[0]) > red:
                    red = int(iiiii[0])
            if iiiii[1] == "blue":
                if int(iiiii[0]) > blue:
                    blue = int(iiiii[0])
        if green == 0:
            power = red * blue
        elif red == 0:
            power = green * blue
        elif blue == 0:
            power = green * red
        else:
            power = green * red * blue
    total += power
print(total)