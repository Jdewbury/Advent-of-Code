import numpy as np
from aocd import get_data

session_id = str(np.load('session_id.npy'))

arr = []

for lines in get_data(day=3, year=2023, session=session_id).split('\n'):
    arr.append(lines)

# Part 1

p1 = 0
symbol_coordinates = []

for row, line in enumerate(arr):
    for col in range(len(line)):
        char = line[col]
        if char not in '0123456789.':
            symbol_coordinates.append((row, col))

for row, line in enumerate(arr):
    num = ''
    num_idxs = []
    for col in range(len(line)):
        char = line[col]
        if char.isdigit():
            num += char
            num_idxs.append(col)
            if col + 1 == len(line) and num or not line[col+1].isdigit():
                for y, x in symbol_coordinates:
                    if x <= num_idxs[-1] + 1 and x >= num_idxs[0] - 1 and y >= row - 1 and y <= row + 1:
                        p1 += int(num)
                num_idxs = []
                num = ''

print('Part 1:', p1)

# Part 2 

p2 = 0
gear_coordinates = []
num_coordinates = []

for row, line in enumerate(arr):
    num = ''
    num_idxs = []
    for col in range(len(line)):
        char = line[col]
        if char == '*':
            gear_coordinates.append((row, col))
        if char.isdigit():
            num += char
            num_idxs.append(col)
            if col + 1 == len(line) and num or not line[col+1].isdigit():
                num_coordinates.append((num, num_idxs, row))
                num_idxs = []
                num = ''
                
for y, x in gear_coordinates:
    adjacent_nums = []
    for num, cols, row in num_coordinates:
        if x <= cols[-1] + 1 and x >= cols[0] - 1 and y >= row - 1 and y <= row + 1:
            adjacent_nums.append(int(num))
    if len(adjacent_nums) == 2:
        p2 += adjacent_nums[0]*adjacent_nums[1]

print('Part 2:', p2)