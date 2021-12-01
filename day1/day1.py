import numpy as np

with open('input.txt') as f:
    data = f.read().splitlines()

sonar = np.array(data)
sonar = sonar.astype(np.int32)

print('Part 1: ' + str(sum(np.diff(sonar) > 0)))

sumSonar = []
for i in range(len(sonar) - 3):
        sumSonar.append(sum(sonar[i:(i + 3)]) < sum(sonar[(i + 1):(i + 4)]))

print('Part 2: ' + str(sum(sumSonar)))