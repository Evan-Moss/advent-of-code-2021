import os, sys

with open(os.path.join(sys.path[0],'input.txt'), 'r') as file:
    lines = [int(l.strip()) for l in file.readlines()]

windows = []
countHigher = 0

for lineNo in range(len(lines)-2):
    windowTotal = sum(lines[lineNo:lineNo+3])
    windows.append(windowTotal)
    if (len(windows) > 0) and (windows[lineNo] > windows[lineNo-1]):
            countHigher += 1

print(countHigher)