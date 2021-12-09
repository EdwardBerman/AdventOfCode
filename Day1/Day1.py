increase = 1
decrease = 0
neither = 0
count = 0
PvC = [] #2 elements
AdventData = open('AdventDay1.txt', 'r', encoding='utf-8-sig')
Basecase = AdventData.readline().strip('\n')
Basecase = int(Basecase)
for line in AdventData:
    if count == 0:
        PvC.append(Basecase)
        PvC.append(Basecase) #Initializes array to first element in dataset
        print(PvC)
        count += 1
    else:
        Previous = PvC[1]
        Previous = int(Previous)
        PvC[0] = Previous
        PvC[1] = int(line.strip('\n'))
        if count < 20:
            print(PvC)
        count += 1

    if PvC[1] == None:
        pass
    elif PvC[1] > PvC[0]: #Compares current and previous lines and updates score
        increase += 1
        if count < 20:
            print('increase = ', increase)
    elif PvC[0] > PvC[1]:
        decrease += 1
        if count < 20:
            print('decrease = ', decrease)
    else:
        neither += 1
        if count < 20:
            print(neither)

increase += 1 #Last Array Doesn't Register// Manual Check
neither -= 1 #The first initialization will always be neither, this overcorrects for that
AdventData.close()
ResultsIDN = [increase, decrease, neither]
print(ResultsIDN)
