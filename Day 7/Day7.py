import os
#print(os.getcwd())

f = open("Day 7\Input.txt", "r")
line = f.read().split("\n")

totsize = 0
curdir = []
#dir = ""
#cursize = 0
dirsize = {}
readmode = False
for i in line:
    print(curdir)
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
            else:
                #if op[2] in dirsize.keys():
                #    op[2] = str(op[2] + "2")
                curdir.append(op[2])
        if op[1] == "ls":
            readmode = True
    else:
        if op[0] != "dir":
            #print(curdir)
            try:
                dirsize[str(curdir[-1])] += int(op[0])
            except:
                dirsize[str(curdir[-1])] = 0
                dirsize[str(curdir[-1])] += int(op[0])
            #print(dirsize[curdir[-1]])
            if len(curdir) > 2:
                #print(curdir)
                for i in range(len(curdir) - 1):
                    #print(curdir)
                    #print(curdir[-(i+1)])
                    #print(curdir[-i])
                    try:
                        dirsize[curdir[-(i+1)]] += dirsize[curdir[-i]]
                    except:
                        dirsize[str(curdir[-(i+1)])] = 0
                        dirsize[curdir[-(i+1)]] += dirsize[curdir[-i]]
            

for i in dirsize:
    if dirsize[i] <= 100000:
        #print(str(dirsize[i]) + " True")
        totsize += int(dirsize[i])
    #else:
        #print(str(dirsize[i]) + " False")
#print(totsize)