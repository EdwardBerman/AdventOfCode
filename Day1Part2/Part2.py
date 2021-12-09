increase = 0
decrease = 0
count = 0
counterTwo = 0
integers = []
threeElements = []
summation = []
AdventData = open('AdventDay1.txt', 'r', encoding='utf-8-sig')
for line in AdventData:
    integers.append(int(line.strip('\n')))
AdventData.close()
integerLength = len(integers)
loopBoundary = integerLength - 2
for x in range(loopBoundary):
    summation.append(integers[count] + integers[count + 1] + integers[count + 2])
    count += 1

#print(summation[1997])
#print(len(summation))
loopBoundarytwo = len(summation) - 1
for x in range(loopBoundarytwo):
    if summation[counterTwo] < summation[counterTwo + 1]:
        increase += 1
    counterTwo += 1
print(increase)
