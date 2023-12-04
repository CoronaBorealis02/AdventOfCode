

f = open("Day 3/input.txt", "r")
engineschema = f.read().split("\n")
linelength = 10
lineno = 0
numbers = ""
symbollist = ["*", "!", "@", "#", "$", "%", "^", "&", "(", ")", "-", "_", "=", "+", "|", "/", "?", "'", '"', ":", ";", "?", ">", "<", ",", "`", "~", "[", "]", "{", "}", " "]
for line in engineschema:
    for index in range(linelength): 
        for symbol in symbollist:
            if line[index] == symbol:
                if lineno != 0:
                    #if top left of symbol and 3 digits long with last digit diagonal
                    if not index <= 2 and engineschema[lineno - 1][index - 3].isdigit() and engineschema[lineno - 1][index - 2].isdigit() and engineschema[lineno - 1][index -1].isdigit():
                        numbers += engineschema[lineno - 1][index - 3] + engineschema[lineno - 1][index - 2] + engineschema[lineno - 1][index - 1] + ","
                    #if top left of symbol and 3 digits long with last digit above
                    elif not index <= 1 and engineschema[lineno - 1][index - 2].isdigit() and engineschema[lineno - 1][index - 1].isdigit() and engineschema[lineno - 1][index].isdigit():
                        numbers += engineschema[lineno - 1][index - 2] + engineschema[lineno - 1][index - 1] + engineschema[lineno - 1][index] + ","
                    #if top left of symbol and 2 digits long with last digit diagonal
                    elif not index <= 1 and engineschema[lineno - 1][index - 2].isdigit() and engineschema[lineno - 1][index - 1].isdigit():
                        numbers += engineschema[lineno - 1][index - 2] + engineschema[lineno - 1][index - 1] + ","
                    #if top left of symbol and 2 digits long with last digit above
                    elif index <= 0 and engineschema[lineno - 1][index - 1].isdigit() and engineschema[lineno - 1][index].isdigit:
                        numbers += engineschema[lineno - 1][index - 1] + engineschema[lineno - 1][index] + ","
                    #if top left of symbol and 1 digit
                    elif not index <= 0 and engineschema[lineno - 1][index - 1].isdigit():
                        numbers += engineschema[lineno - 1][index - 1] + ","
                    #if top middle of symbol and 3 digits long with middle digit above
                    elif not index <= 0 and index != linelength and engineschema[lineno - 1][index - 1].isdigit() and engineschema[lineno - 1][index].isdigit() and engineschema[lineno - 1][index + 1].isdigit():
                        numbers += engineschema[lineno - 1][index - 1] + engineschema[lineno - 1][index] + engineschema[lineno - 1][index + 1] + ","
                    #if top left of symbol and 2 digits long with last digit above
                    elif not index <= 0 and  engineschema[lineno - 1][index - 1].isdigit() and engineschema[lineno - 1][index].isdigit():
                        numbers += engineschema[lineno - 1][index - 1] + engineschema[lineno - 1][index] + ","
                    #if top right of symbol and 3 digits long with first digit above 
                    if not index >= (linelength - 1) and engineschema[lineno - 1][index].isdigit() and engineschema[lineno - 1][index + 1].isdigit() and engineschema[lineno - 1][index + 2].isdigit():
                        numbers += engineschema[lineno - 1][index] + engineschema[lineno - 1][index + 1] + engineschema[lineno - 1][index + 2] + ","
                    #if top right of symbol and 2 digits long with first digit above
                    elif not index >= (linelength) and engineschema[lineno - 1][index].isdigit() and engineschema[lineno - 1][index + 1].isdigit():
                        numbers += engineschema[lineno - 1][index] + engineschema[lineno - 1][index + 1] + ","
                    #if top right of symbol and 3 digits long with first digit diagonal
                    elif not index >= (linelength - 2) and engineschema[lineno - 1][index + 1].isdigit() and engineschema[lineno - 1][index + 2].isdigit and engineschema[lineno - 1][index + 3]:
                        numbers += engineschema[lineno - 1][index + 1] + engineschema[lineno - 1][index + 2] + engineschema[lineno - 1][index + 3] + ","
                    #if top right of symbol and 2 digits long with first digit diagonal
                    elif not index >= (linelength - 1) and engineschema[lineno - 1][index + 1].isdigit() and engineschema[lineno - 1][index + 2].isdigit():
                        numbers += engineschema[lineno - 1][index + 1] + engineschema[lineno - 1][index + 2] + ","
                    #if top right of symbol and 1 digit
                    elif not index >= (linelength) and engineschema[lineno - 1][index + 1].isdigit():
                        numbers += engineschema[lineno - 1][index + 1] + ","
                    #if top middle of symbol and 1 digit long
                    if not index >= linelength and not index <= 0 and engineschema[lineno - 1][index].isdigit() and not engineschema[lineno - 1][index - 1].isdigit() and not engineschema[lineno - 1][index + 1].isdigit():
                        numbers += engineschema[lineno - 1][index] + ","
                #if left of symbol and 3 digits
                if not index <= 2 and engineschema[lineno][index - 3].isdigit() and engineschema[lineno][index - 2] and engineschema[lineno][index - 1]:
                    numbers += engineschema[lineno][index - 3] + engineschema[lineno][index - 2] + engineschema[lineno][index - 1] + ","
                #if left of symbol and 2 digits
                elif not index <= 1 and engineschema[lineno][index - 2].isdigit() and engineschema[lineno][index - 1].isdigit():
                    numbers += engineschema[lineno][index - 2] + engineschema[lineno][index - 1] + ","
                #if left of symbol and 1 digit
                elif not index <= 0 and engineschema[lineno][index - 1].isdigit():
                    numbers += engineschema[lineno][index - 1] + ","
                #if right of symbol and 3 digits
                if not index >= (linelength - 2) and engineschema[lineno][index + 1].isdigit() and engineschema[lineno][index + 2].isdigit() and engineschema[lineno][index + 3].isdigit():
                    numbers += engineschema[lineno][index + 1] + engineschema[lineno][index + 2] + engineschema[lineno][index + 3] + ","
                #if right of symbol and 2 digits
                elif not index >= (linelength - 1) and engineschema[lineno][index + 1].isdigit() and engineschema[lineno][index + 2].isdigit():
                    numbers += engineschema[lineno][index + 1] + engineschema[lineno][index + 2] + ","
                #if right of symbol is 1 digit
                elif not index >= (linelength) and engineschema[lineno][index + 1].isdigit():
                    numbers += engineschema[lineno][index + 1] + ","
                if lineno != len(engineschema):
                    #if bottom left of symbol and 3 digits long with last digit diagonal
                    if not index <= 2 and engineschema[lineno + 1][index - 3].isdigit() and engineschema[lineno + 1][index - 2].isdigit() and engineschema[lineno + 1][index -1].isdigit():
                        numbers += engineschema[lineno + 1][index - 3] + engineschema[lineno + 1][index - 2] + engineschema[lineno + 1][index - 1] + ","
                    #if bottom left of symbol and 3 digits long with last digit below
                    elif not index <= 1 and engineschema[lineno + 1][index - 2].isdigit() and engineschema[lineno + 1][index - 1].isdigit() and engineschema[lineno + 1][index].isdigit():
                        numbers += engineschema[lineno + 1][index - 2] + engineschema[lineno + 1][index - 1] + engineschema[lineno + 1][index] + ","
                    #if bottom left of symbol and 2 digits long with last digit diagonal
                    elif not index <= 1 and engineschema[lineno + 1][index - 2].isdigit() and engineschema[lineno + 1][index - 1].isdigit():
                        numbers += engineschema[lineno + 1][index - 2] + engineschema[lineno + 1][index - 1] + ","
                    #if bottom left of symbol and 2 digits long with last digit below
                    elif not index >= linelength and not index <= 0 and engineschema[lineno + 1][index - 1].isdigit() and engineschema[lineno + 1][index].isdigit and not engineschema[lineno + 1][index + 1]:
                        numbers += engineschema[lineno + 1][index - 1] + engineschema[lineno + 1][index] + ","
                    #if bottom left of symbol and 1 digit
                    elif not index >= linelength and not index <= 0 and engineschema[lineno + 1][index - 1].isdigit() and not engineschema[lineno + 1][index].isdigit() and not engineschema[lineno + 1][index + 1].isdigit():
                        numbers += engineschema[lineno + 1][index - 1] + ","
                    #if bottom middle of symbol and 3 digits long with middle digit below
                    elif not index <= 0 and index != linelength and engineschema[lineno + 1][index - 1].isdigit() and engineschema[lineno + 1][index].isdigit() and engineschema[lineno + 1][index + 1].isdigit():
                        numbers += engineschema[lineno + 1][index - 1] + engineschema[lineno + 1][index] + engineschema[lineno + 1][index + 1] + ","
                    #if bottom left of symbol and 2 digits long with last digit below
                    elif not index <= 0 and  engineschema[lineno + 1][index - 1].isdigit() and engineschema[lineno + 1][index].isdigit():
                        numbers += engineschema[lineno + 1][index - 1] + engineschema[lineno + 1][index] + ","
                    #if bottom right of symbol and 3 digits long with first digit below 
                    if not index >= (linelength - 1) and engineschema[lineno + 1][index].isdigit() and engineschema[lineno + 1][index + 1].isdigit() and engineschema[lineno + 1][index + 2].isdigit():
                        numbers += engineschema[lineno + 1][index] + engineschema[lineno + 1][index + 1] + engineschema[lineno + 1][index + 2] + ","
                    #if bottom right of symbol and 2 digits long with first digit below
                    elif not index >= (linelength) and engineschema[lineno + 1][index].isdigit() and engineschema[lineno + 1][index + 1].isdigit():
                        numbers += engineschema[lineno + 1][index] + engineschema[lineno + 1][index + 1] + ","
                    #if bottom right of symbol and 3 digits long with first digit diagonal
                    elif not index >= (linelength - 2) and engineschema[lineno + 1][index + 1].isdigit() and engineschema[lineno + 1][index + 2].isdigit and engineschema[lineno + 1][index + 3]:
                        numbers += engineschema[lineno + 1][index + 1] + engineschema[lineno + 1][index + 2] + engineschema[lineno + 1][index + 3] + ","
                    #if bottom right of symbol and 2 digits long with first digit diagonal
                    elif not index >= (linelength - 1) and engineschema[lineno + 1][index + 1].isdigit() and engineschema[lineno + 1][index + 2].isdigit():
                        numbers += engineschema[lineno + 1][index + 1] + engineschema[lineno + 1][index + 2] + ","
                    #if bottom right of symbol and 1 digit
                    elif not index >= (linelength) and engineschema[lineno + 1][index + 1].isdigit():
                        numbers += engineschema[lineno + 1][index + 1] + ","
                    #if bottom middle of symbol and 1 digit long
                    if not index >= linelength and not index <= 0 and engineschema[lineno + 1][index].isdigit() and not engineschema[lineno + 1][index - 1].isdigit() and not engineschema[lineno + 1][index + 1].isdigit():
                        numbers += engineschema[lineno + 1][index] + ","
                   
    lineno += 1
print(numbers)
finalnum = numbers.split(",")
total = 0
finalnum.pop()
for i in finalnum:
    total += int(i)
print(total)