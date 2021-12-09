forward = 0
depth = 0
aim = 0
AdventData = open('inputDay2.txt', 'r', encoding = 'utf-8-sig')
for line in AdventData:
    if (line.find('forward') != -1):
        forwardTemp = line.strip('forward ')
        forwardTemp = int(forwardTemp)
        forward += forwardTemp
        depth += (aim * forwardTemp)
    if (line.find('down') != -1):
        downTemp = line.strip('down ')
        downTemp = int(downTemp)
        aim += downTemp
    if (line.find('up') != -1):
        upTemp = line.strip('up')
        upTemp = int(upTemp)
        aim -= upTemp

result = forward * depth
print(result)
