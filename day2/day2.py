import numpy as np

with open('input.txt') as f:
    data = f.read().splitlines()

posDic = {"hor": 0, "ver": 0}

for ins in data:
    sp = ins.split(' ')
    if sp[0] == 'up':
        posDic["ver"] -= int(sp[1])
    elif sp[0] == 'down':
        posDic["ver"] += int(sp[1])
    else:
        posDic["hor"] += int(sp[1])

print('Part 1: ' + str(posDic["hor"] * posDic["ver"]))

posDic = {"hor": 0, "ver": 0, "aim": 0}

for ins in data:
    sp = ins.split(' ')
    if sp[0] == 'up':
        posDic["aim"] -= int(sp[1])
    elif sp[0] == 'down':
        posDic["aim"] += int(sp[1])
    else:
        posDic["hor"] += int(sp[1])
        posDic["ver"] += posDic["aim"] * int(sp[1])

print('Part 2: ' + str(posDic["hor"] * posDic["ver"]))