import numpy as np
input = np.loadtxt("input.txt")

for i in input:
    for x in input:
        if (i + x == 2020):
            print(i * x)