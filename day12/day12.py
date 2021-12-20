import os, sys # This file can definitely be optimised.
from collections import defaultdict

with open(os.path.join(sys.path[0],'input.txt'), 'r') as file:
    lines = [f.strip().split('-') for f in file.readlines()]

nodes = defaultdict(set)

for l in lines:
    if l[0] != 'end' and l[1] != 'end':
        nodes[l[0]].add(l[1])
        nodes[l[1]].add(l[0])
    elif l[0] == 'end':
        nodes[l[1]].add(l[0])
    elif l[1] == 'end':
        nodes[l[0]].add(l[1])

def is_end(path):
    node = path[-1]
    if node == 'end':
        return True
    return False

def other_small_caves_visited_once(path):
    small_counts = []
    for p in path:
        if p.islower():
            small_counts.append(path.count(p))
    return all(s == 1 for s in small_counts)
            

def can_visit(node, path, part=1):
    if part == 1:
        if (node in path) and (node.islower()):
            return False
        return True
    if part == 2:
        if (not other_small_caves_visited_once(path) and (node in path) and node.islower()) or node == 'start':
            return False
        return True
        

paths = []

def eval(path, part=1):
    new_paths = []
    options = nodes[path[-1]]
    for v in options:
        if can_visit(v, path, part):
            new_paths.append(path + [v])
    return new_paths

def recurse(path, part=1):
    e = eval(path, part)
    if e != []:
        for p in e:
            if is_end(p):
                paths.append(p)
            else:
                recurse(p, part)


recurse(['start'], part=2)
print(len(paths))
