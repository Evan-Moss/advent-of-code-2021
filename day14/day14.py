import os, sys
from collections import defaultdict

with open(os.path.join(sys.path[0],'input.txt'), 'r') as file:
    lines = [f.strip() for f in file.readlines()]
    template = lines[0]
    rules = {}
    for r in [[x.strip() for x in l.split('->')] for l in lines[2:]]:
        rules[r[0]] = (r[0][0] + r[1], r[1] + r[0][1])

def transform(pair_counts):
    pairs = pair_counts.copy()
    for k, v in pairs.items():
        if v > 0:
            pair_counts[k] -= v
            pair_counts[rules[k][0]] += v
            pair_counts[rules[k][1]] += v
    return pair_counts

pair_counts = defaultdict(int)
for i in [template[x:x+2] for x in range(len(template)-1)]:
    pair_counts[i] += 1

for x in range(40):
    pair_counts = transform(pair_counts)

char_counts = defaultdict(int)
char_counts[template[0]] += 1
for k,v in pair_counts.items():
    char_counts[k[1]] += v

answer = char_counts[max(char_counts, key=char_counts.get)] - char_counts[min(char_counts, key=char_counts.get)]
print(answer)