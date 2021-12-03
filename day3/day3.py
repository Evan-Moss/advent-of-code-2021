import pandas as pd

file = open('input.txt', 'r')
lines = [list(l.strip()) for l in file.readlines()]

df = pd.DataFrame(lines)

output = ''
for c in df.columns:
    output += df[c].value_counts().idxmax()

epsilon = int(output,2)
gamma = epsilon ^ int('1'*12,2)

print('e: {}, g: {}, e*g: {}'.format(epsilon, gamma, epsilon*gamma))