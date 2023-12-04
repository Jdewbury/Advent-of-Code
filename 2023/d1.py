import numpy as np
from aocd import get_data

session_id = str(np.load('session_id.npy'))

arr = []

for lines in get_data(day=1, year=2023, session=session_id).split('\n'):
    arr.append(lines)

# Part 1

p1 = 0

for code in arr:
    letters = []
    for letter in code:
        if letter.isdigit():
            letters.append(letter)
    if len(letters) == 1:
        add = int(letters[0]*2)
    if len(letters) > 1:
        add = int(letters[0] + letters[-1])
    p1 += add

print('Part 1:', p1)

# Part 2

number_map = {'one':'1', 
       'two':'2', 
       'three':'3', 
       'four':'4', 
       'five':'5', 
       'six':'6', 
       'seven':'7', 
       'eight':'8', 
       'nine':'9'}

p2 = 0

for code in arr:
    og = code
    code = list(code)
    for i in range(len(code)):
        for j in range(len(code) + 1):
            if "".join(code[i:j]) in number_map:
                code[i] = number_map["".join(code[i:j])]

    letters = []
    for letter in code:
        if letter.isdigit():
            letters.append(letter)
    if len(letters) == 1:
        add = int(letters[0]*2)
    if len(letters) > 1:
        add = int(letters[0] + letters[-1])
    p2 += add

print('Part 2:', p2)