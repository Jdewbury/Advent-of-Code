import numpy as np
from aocd import get_data

session_id = str(np.load('session_id.npy'))

arr = []

for lines in get_data(day=4, year=2023, session=session_id).split('\n'):
    temp = []
    card, nums = lines.split(':')
    for num in nums.split('|'):
        temp.append(num.split())
    arr.append(temp)

# Part 1

p1 = 0

for winning_nums, my_nums in arr:
    wins = 0
    for num in my_nums:
        if num in winning_nums:
            wins += 1
    if wins > 0:
        p1 += 2**(wins-1)

print('Part 1:', p1)

# Part 2 

p2 = 0

card_copies = [1]*len(arr)

for idx, (winning_nums, my_nums) in enumerate(arr):
    wins = 0
    for num in my_nums:
        if num in winning_nums:
            wins += 1
    num_copies = card_copies[idx]
    for i in range(wins):
        card_copies[idx+i+1] += num_copies

for cards in card_copies:
    p2 += cards

print('Part 2:', p2)