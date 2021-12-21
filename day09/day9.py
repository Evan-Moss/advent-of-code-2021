import os, sys
import numpy as np
with open(os.path.join(sys.path[0],'input.txt'), 'r') as file:
    input_list = np.array([np.array([int(x) for x in list(l.strip())]) for l in file.readlines()])

def get_adjacent_vals(x, y):
    adjs = get_adjacent_coords(x, y)
    out = []
    for a in adjs:
        out.append(input_list[a[0]][a[1]])
    return out

def get_adjacent_coords(x, y):
    verticals = [(x+1, y) if x+1 < len(input_list) else False, (x-1,y) if x-1 >=0 else False]
    horizontals = [(x, y+1) if y+1 < len(input_list[x]) else False, (x,y-1) if y-1 >=0 else False]
    out = verticals + horizontals
    return [o for o in out if o]

def is_low_point(x, y):
    point = input_list[x][y]
    
    if point == 9:
        return False
    adjacent = get_adjacent_vals(x, y)
    if all(point < i for i in adjacent):
        return True
    return False 

def get_basin(x, y, basin_no):
    point_val = input_list[x][y]
    for i in get_adjacent_coords(x, y):
        adj = input_list[i[0]][i[1]]
        if adj < 9 and adj > point_val and basin_state[i[0]][i[1]] == 0:
            basin_state[i[0]][i[1]] = basin_no
            get_basin(i[0],i[1], basin_no)

basin_state = np.zeros(input_list.shape)

total = 0
for x in range(len(input_list)):
    line = input_list[x]
    for y in range(len(line)):
        if is_low_point(x, y):
            total += input_list[x][y] + 1
            basin_no = np.max(basin_state) +1
            basin_state[x][y] = basin_no
            get_basin(x, y, basin_no)

print(total)

num_basins = np.max(basin_state)

basin_sizes = []

for x in range(1, int(num_basins)+1):
    basin_sizes.append(len(np.where(basin_state == x)[0]))

print(np.product(sorted(basin_sizes)[-3:]))