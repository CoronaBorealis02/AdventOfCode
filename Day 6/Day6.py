#Part 1

f = open("Day 6/Input.txt", "r")

string = f.read()

checker = []
count = 0
endloop = False
for i in string:
    checker.append(i)
    count += 1
    if len(checker) < 4:
        pass
    elif endloop:
        break
    else:
        temp = []
        for ii in checker:
            if ii not in temp:
                temp.append(ii)
            if len(temp) == 4:
                print(count)
                endloop = True
        checker.pop(0)


#Part 2

checker = []
count = 0
for i in string:
    checker.append(i)
    count += 1
    if len(checker) < 14:
        pass
    else:
        temp = []
        for ii in checker:
            if ii not in temp:
                temp.append(ii)
            if len(temp) == 14:
                print(count)
                exit()
        checker.pop(0)