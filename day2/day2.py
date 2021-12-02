import sys
file = open(sys.argv[1], 'r')
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