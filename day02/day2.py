import os, sys

with open(os.path.join(sys.path[0],'input.txt'), 'r') as file:
    lines = [l.strip().split() for l in file.readlines()]

horizontal = 0
vertical = 0

for l in lines:
    direction = l[0]
    ammount = int(l[1])
    if direction == 'forward':
        horizontal += ammount
    elif direction == 'down':
        vertical += ammount
    elif direction == 'up':
        vertical -= ammount

print(horizontal * vertical)