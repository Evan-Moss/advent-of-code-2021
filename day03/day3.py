import pandas as pd
import os, sys

with open(os.path.join(sys.path[0],'input.txt'), 'r') as file:
    lines = [list(l.strip()) for l in file.readlines()]

df = pd.DataFrame(lines)

output = ''
for c in df.columns:
    output += df[c].value_counts().idxmax()

epsilon = int(output,2)
gamma = epsilon ^ int('1'*12,2)

print('e: {}, g: {}, e*g: {}'.format(epsilon, gamma, epsilon*gamma))