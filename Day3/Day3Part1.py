import numpy as np
OZ = np.array([],[])
#2D array
i = 0
x = 0
AdventData = open('Binary.txt', 'r', encoding = 'utf-8-sig')
for line in AdventData:
    while x < 11:
        OZ[i, x] = (i, int(line.strip('\n')[x:(x+1)]))
        x += 1
    i += 1


