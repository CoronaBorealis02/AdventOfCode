import numpy as np
input = np.loadtxt("input.txt")

for x in input:
	for y in input:
		for z in input:
			if (x + y + z == 2020):
				print(x * y * z)