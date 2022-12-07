#Part 1

f = open("Day 7/Input.txt", "r")
line = f.read().split("\n")

totsize = 0
curdir = []
dirsize = dict()
readmode = False
path = ""

def makepath(limit = 0):
    if limit == 0:
        path = "/" + "/".join(curdir[1:])
    else:
        path = "/" + "/".join(curdir[1:-(limit)])
    if len(curdir) == 1:
        path = "/"
    return path

for i in line:
    op = i.strip("$").split(" ")
    if readmode == True and (op[1] == "cd" or op[1] == "ls"):
        readmode = False
    if readmode == False:
        if op[1] == "cd":
            if op[2] == ".." and curdir[:-1] != "/":
                curdir.pop()
            elif op[2] == "/":
                curdir.clear()
                curdir.append(op[2])
                if makepath() not in dirsize.keys():
                    dirsize[makepath()] = 0
            else:
                curdir.append(op[2])
                if makepath() not in dirsize.keys():
                    dirsize[makepath()] = 0
        if op[1] == "ls":
            readmode = True
    else:
        if op[0] != "dir":
            dirsize[makepath()] += int(op[0])
            if makepath() != "/":
                dirsize['/'] += int(op[0])
            if len(curdir) > 2:
                for i in range(len(curdir) - 2):
                    if makepath(i+1) in dirsize.keys() and makepath(i) in dirsize.keys():
                        dirsize[makepath(i+1)] += dirsize[makepath(i)]
                    elif makepath(i) in dirsize:
                        dirsize[makepath(i+1)] = 0
                        dirsize[makepath(i+1)] += dirsize[makepath(i)]

            
for i in dirsize:
    if dirsize[i] <= 100000:
        totsize += int(dirsize[i])
print(totsize)

#Part 2

usedspace = dirsize['/']
totalspace = 70000000
neededspace = 30000000
unusedspace = totalspace - usedspace
neededspace -= unusedspace
delcandidates = []

for i in dirsize:
    if dirsize[i] > neededspace:
        delcandidates.append(dirsize[i])

delcandidates.sort()
print(delcandidates[0])

