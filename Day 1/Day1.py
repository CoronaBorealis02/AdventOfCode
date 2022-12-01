#Task 1:

f = open("Day 1/Input.txt", "r")

cal_list = []
caltot = []
cal_list = f.read().replace("\n", " ").split("  ")
for i in cal_list:
    caltemp = i.split(" ")
    temptot = 0
    for i in caltemp:
        temptot += int(i)
    caltot.append(temptot)

print(max(caltot))

#Task 2:

caltot.sort(reverse=True)

print(sum(caltot[:3]))