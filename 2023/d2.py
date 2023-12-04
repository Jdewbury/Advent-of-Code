import numpy as np
from aocd import get_data

session_id = str(np.load('session_id.npy'))

arr = []

for lines in get_data(day=2, year=2023, session=session_id).split('\n'):
    temp = []
    subsets = lines.split(':')[1]
    for draw in subsets.strip().split('; '):
        temp.append(draw)
    arr.append(temp)

# Part 1

total = 0
max_scores = {'red':12, 'green':13, 'blue':14}

for idx in range(len(arr)):
    valid = True
    for game in arr[idx]:
        for subset in game.split(', '):
            hand = subset.split(' ')
            if hand[1] in max_scores and int(hand[0]) > max_scores[hand[1]]:
                valid = False
                break

    if valid:
        total += idx + 1

print('Part 1:', total)

# Part 2 

total = 0

for idx in range(len(arr)):
    min_scores = {'red':0, 'green':0, 'blue':0}
    for game in arr[idx]:
        for subset in game.split(', '):
            hand = subset.split(' ')
            if hand[1] in min_scores and int(hand[0]) > min_scores[hand[1]]:
                min_scores[hand[1]] = int(hand[0])

    score = 1
    for key, val in min_scores.items():
        score *= val
    total += score

print('Part 2:', total)