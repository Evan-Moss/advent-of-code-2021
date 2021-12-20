import os, sys
import numpy as np

# Pre-processing
with open(os.path.join(sys.path[0],'inputtest.txt'), 'r') as file:
    lines = file.readlines()
    for l in range(len(lines)):
        lines[l]  = [[int(y) for y in x.strip().split(',')] for x in lines[l].strip().split('->')]

class Coord:
    def __init__(self, coord_list):
        self.x = coord_list[0]
        self.y = coord_list[1]
    def __str__(self):
        return 'X:{}, Y:{}'.format(self.x, self.y)
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    def __hash__(self):
        return hash((self.x,self.y))

class Line:
    def __init__(self, file_line):
        self.coords1 = Coord(file_line[0])
        self.coords2 = Coord(file_line[1])
        self.is_straight = self.coords1.x == self.coords2.x or self.coords1.y == self.coords2.y
        self.coords_list = self.calculate_points()
    
    def calculate_points(self):
        if self.is_straight:
            points = self.calculate_straight_points()
        else:
            points = self.calculate_angle_points()
        return points

    def ranger(self, i, j):
        if i < j:
            return range(i,j+1)
        return range(j,i+1)

    def calculate_angle_points(self):
        m = (self.coords2.y -  self.coords1.y) / (self.coords2.x -  self.coords1.x)

        small_y = self.coords1.y if self.coords1.y < self.coords2.y else self.coords2.y
        big_y = self.coords1.y if self.coords1.y > self.coords2.y else self.coords2.y
        coords_list = [] 
        if m > 0:
            ys = range(small_y, big_y+1)

        if m < 0:
            ys = range(big_y, small_y-1,-1)

        counter = 0
        
        #!!!!!!!!!!!!!
        print(list(zip(self.ranger(self.coords1.x, self.coords2.x), ys)))

        for x in self.ranger(self.coords1.x, self.coords2.x):
            coords_list.append(Coord([x, ys[counter]]))
            counter+=1
        return coords_list

    def calculate_straight_points(self):
        coords_list = [] 
        for x in self.ranger(self.coords1.x, self.coords2.x):
            for y in self.ranger(self.coords1.y, self.coords2.y):
                coords_list.append(Coord([x,y]))
        
        return coords_list

all_points = {}

for line in lines:
    line = Line(line)
    # For part 1
    # if not line.is_straight:
    #     continue
    coords = line.coords_list
    for c in coords:
        if c not in all_points.keys():
            all_points[c] = 1
        else:
            all_points[c] += 1

grid = np.array(list(all_points.values()))

# To print test grid
# for y in range(0,10):
#     print('\n')
#     for x in range(0,10):
#         num = all_points.get(Coord([x,y]))
#         if num == None:
#             num = '.'
#         print(num, end='')
# print('\n')

print(grid[np.where(grid>1)].size)