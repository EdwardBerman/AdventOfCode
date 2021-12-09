from _typeshed import Self

AdventData = open('Binary.txt', 'r', encoding = 'utf-8-sig')
Score = []
counter = 0
runCounter = 0
x = 0 
z = 0
fullList = []
Lines = AdventData.readlines()

class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def addChild(self, data):
        if data == self.data:
            return
        if data[z] == Score[z]: #Change I
            if self.left:
                self.left.addChild(data) #adds a node if not already present
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = Node(data)
    def searchLeft(self):
        if self.left == None:
            return self
        else:
            self.left.searchLeft()
    def searchRight(self):
        if self.right == None:
            return self
        else:
            self.right.searchRight()

for i in range(0, 12):
    for line in Lines:
        fullList.append(line)
        Temp = line.strip('\n')
        TempTwo = Temp[i: i + 1]
        if TempTwo == '1':
            counter += 1
        else:
            counter -= 1
    if counter > 1:
        Score.append(1)
    else:
        Score.append(0)
    counter = 0

print(Score)
tree = Node(fullList)
for line in Lines:
    tree.addChild(fullList[z])
    z += 1
print("left = ", tree.searchLeft(), " right = ", tree.searchRight())





