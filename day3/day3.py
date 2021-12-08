import numpy as np

with open('input.txt') as f:
    data = f.read().splitlines()

aList = []
for i in range(len(data[0])):
    posSum = 0
    for c in data:
        posSum += int(c[i])
    aList.append(posSum)
gamma = [str(int(x > (len(data) / 2))) for x in aList]
eps = [str(int(x != "1")) for x in gamma]

print('Part 1: ' + str(int("".join(gamma), 2) * int("".join(eps), 2)))

dataOX = data.copy()
dataCO = data.copy()

def checkBIT(dataOX, greater = True):
    bitLen = len(dataOX[0])
    for i in range(bitLen):
        curOXlen = len(dataOX)
        if greater:
            if sum([c[i] == "1" for c in dataOX]) >= (curOXlen / 2):
                remSym = '0'
            else:
                remSym = '1'
        else:
            if sum([c[i] == "1" for c in dataOX]) < (curOXlen / 2):
                remSym = '0'
            else:
                remSym = '1'
        delOX = [ox for ox in range(curOXlen) if dataOX[ox][i] == remSym]
        for index in sorted(delOX, reverse=True):
            del dataOX[index]
        if len(dataOX) == 1:
            return dataOX
    return dataOX

ox = checkBIT(dataOX = dataOX, greater=True)[0]

co = checkBIT(dataOX = dataCO, greater=False)[0]

print('Part 2: ' + str(int(ox, 2) * int(co, 2)))