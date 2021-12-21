# This is just minimising a function, could probably be achieved with scipy
import os, sys
import numpy as np 

with open(os.path.join(sys.path[0],'input.txt'), 'r') as file:
    input_list = [int(f) for f in file.readline().strip().split(',')]

def calculate_dist(point, part=1):
    dist_total=0
    for i in input_list:
        dist = np.abs(i-point)
        if part == 1:
            dist_total += dist
        elif part == 2:
            for d in range(1,dist+1):
                dist_total += d
    return dist_total

def minimise(input_list, function, jump, point=None, down=True, part=1):
    if point == None:
        point = max(input_list)
    val = function(point, part)
    old_point = point
    while True:
        #print(point)
        old_point = point
        if down:
            point -= jump
        else:
            point += jump
        new_val = function(point, part)
        if new_val < val:
            val = new_val
        else:
            print(val)
            return old_point

jumps = [500,250,100,50,25,10,5,2,1]
down = False
turn_point = None
for x in range(len(jumps)):
    #print("JUMP", jumps[x])
    turn_point = minimise(input_list, calculate_dist, jumps[x], point=turn_point, down=down, part=2)
    down = down ^ True