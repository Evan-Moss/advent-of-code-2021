import os, sys

with open(os.path.join(sys.path[0],'input.txt'), 'r') as file:
    lines = [int(l.strip()) for l in file.readlines()]

countHigher = 0

for lineNo in range(1,len(lines)):
    if lines[lineNo] >= lines[lineNo-1]:
        countHigher += 1

print(countHigher)
file.close()