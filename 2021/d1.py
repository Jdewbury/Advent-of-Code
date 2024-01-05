import numpy as np
from aocd import get_data

session_id = str(np.load('session_id.npy'))

arr = []

for lines in get_data(day=1, year=2021, session=session_id).split():
    arr.append(int(lines))

# Part 1

p1 = 0

for idx in range(len(arr)-1):
    if arr[idx] < arr[idx+1]:
        p1 += 1

print('Part 1:', p1)

# Part 2

p2 = 0

for idx in range(len(arr)-1):
    if sum(arr[idx:idx+3]) < sum(arr[idx+1:idx+4]):
        p2 += 1

print('Part 2:', p2)