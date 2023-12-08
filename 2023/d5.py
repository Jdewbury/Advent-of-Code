import numpy as np
from aocd import get_data

session_id = str(np.load('session_id.npy'))

arr = []

for idx, lines in enumerate(get_data(day=5, year=2023, session=session_id).split('\n\n')):
    name, vals = lines.split(':')
    if idx == 0:
        seeds = vals.split()
    else:
        temp = []
        for i in range(0, len(vals.split()), 3):
            temp.append([int(num) for num in vals.split()[i:i+3]])
        arr.append(temp)

# Part 1

locations = []

for seed in seeds:
    current = int(seed)
    for category in arr:
        for _map in category:
            if current >= _map[1] and current <= _map[1] + _map[2]:
                current -= _map[1] - _map[0]
                break

    locations.append(current)

p1 = min(locations)

print('Part 1:', p1)

# Part 2 

p2 = 0


print('Part 2:', p2)