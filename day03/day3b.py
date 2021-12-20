import pandas as pd # Using pandas to avoid recursion
import os, sys

with open(os.path.join(sys.path[0],'input.txt'), 'r') as file:
    lines = [list(l.strip()) for l in file.readlines()]

df = pd.DataFrame(lines)

def filter_vals(df, criteria):
    # Criteria is '1' for oxygen rating, '0' for C02 rating
    for c in df.columns:
        vals = df[c].value_counts()
        if vals.get('0') == vals.get('1'):
            max_bit = criteria
        elif criteria == '1':
            max_bit = vals.idxmax()
        elif criteria == '0':
            max_bit = vals.idxmin()
        
        df = df[df[c] == max_bit]
    return int(''.join(list(df.iloc[0])), base=2)

print(filter_vals(df, '0') * filter_vals(df, '1'))