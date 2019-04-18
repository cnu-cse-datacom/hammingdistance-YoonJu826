import random
import numpy as np
import pandas as pd
from hamming_practice import hamming

df = pd.read_csv('sample.csv', names=['word', 'bin'])

count = 0
row_size = df.shape[0]
min = 1223466
print(row_size)

for i in range(row_size):
    for j in range(i+1, row_size):
        hd = hamming(df.iloc[i,1], df.iloc[j,1])
    
        print(count, "(", df.iloc[i,0], df.iloc[j,0], ")hamming_distance: ", hd)
        count = count+1
        if min > hd:
            min = hd 

print("min hamming distance", min)



