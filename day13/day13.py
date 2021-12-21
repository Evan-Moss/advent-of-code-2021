import os, sys
import numpy as np

with open(os.path.join(sys.path[0],'input.txt'), 'r') as file:
    rl = file.readlines()
    spl = rl.index('\n')
    coords = np.array([np.array([int(x) for x in f.strip().split(',')]) for f in rl[:spl]])
    instructions = [(i[0],int(i[1])) for i in [f.split(' ')[-1].strip().split('=') for f in rl[spl+1:]]]

def create_paper(coords):
    max_x = max(coords[:,0])
    max_y = max(coords[:,1])
    paper = np.zeros((max_y+1, max_x+1))
    for c in coords:
        paper[c[1]][c[0]] = '1'
    return paper

def merge(arr1, arr2):
    assert(len(arr1) == len(arr2))
    return np.array([c[0] or c[1] for c in zip(arr1, arr2)])

def fold_horizontal(paper, y_val):
    merged = []
    for i in range(paper.shape[0]-1, y_val, -1):
        down = i 
        up = paper.shape[0]-i-1
        merged.append(merge(paper[up,:],paper[down,:]))
    return np.array(merged)

def fold_vertical(paper, x_val):
    merged = []
    for i in range(paper.shape[1]-1, x_val, -1):
        down = i 
        up = paper.shape[1]-i-1
        merged.append(merge(paper[:,up],paper[:, down]))
    return np.array(merged).T

paper = create_paper(coords)

for inst in instructions:
    dir = inst[0]
    val = inst[1]
    if dir == 'x':
        paper = fold_vertical(paper, val)
    elif dir == 'y':
        paper = fold_horizontal(paper, val)

with open('output.txt', 'w') as file:
    file.write('\n'.join([''.join([' # ' if x==1 else '   ' for x in p])for p in paper]))