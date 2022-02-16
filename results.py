import pandas as pd
import os
path = './yolov5/runs/detect/exp_number/labels/'
files = os.listdir(path)
f = open('results.txt', 'w+')
for i in files:
    file = open(path+i)
    for j in file:
        ts = j.split(' ')
        ts.insert(0, i.split('.')[0])
        ts = ' '.join(ts)
        #print(ts)
        f.write(ts)

import pandas as pd
df = pd.read_csv('results.txt', sep=' ' ,names=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(df.head())
df['b'] = df['b']+1
print(df.head())
df.to_csv('results.txt', index=False, sep=' ')