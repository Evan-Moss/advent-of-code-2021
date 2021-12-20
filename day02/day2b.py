import os, sys

with open(os.path.join(sys.path[0],'input.txt'), 'r') as file:
    lines = [l.strip().split() for l in file.readlines()]

aim = 0
horizontal = 0
depth = 0

for l in lines:
    direction = l[0]
    ammount = int(l[1])
    if direction == 'forward':
        horizontal += ammount
        depth += aim * ammount
    elif direction == 'down':
        aim += ammount
    elif direction == 'up':
        aim -= ammount

print(depth * horizontal)