import numpy as np
import itertools

# example from wikipedia
a = [[-1,1],[3,2],[2,3],[-1,0],[0,-1]]
b = [1,12,12,0,0]

n = len(a)
k = len(a[0])

for s in itertools.combinations(range(n),k):
    aa = []
    bb = []
    for x in s:
        aa.append(a[x])
        bb.append(b[x])
    aaa = np.array(aa)
    bbb = np.array(bb)
    x = np.linalg.solve(aaa,bbb)
    
    good = True
    for i in range(n):
        t = 0
        for j in range(k):
            t += x[j] * a[i][j]
        if t > b[i]:
            good = False
    if good:
        print(s,aa,bb,x)
    
    
    
