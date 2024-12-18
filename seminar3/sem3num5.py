import numpy as np
n, m = map(int, input().split())
a=[[0]*m for t in range(n)]
i,j,k = 0, 0, 0
step=((0, 1,), (1, 0,), (0, -1,), (-1, 0,),)
for d in range(1, n*m+1):
    a[i][j] = d
    for l in range(4):
        k1 = (k+l) % 4
        di, dj = step[k1]
        i1, j1 = i+di, j+dj
        if (0<=i1<n) and (0<=j1<m) and (a[i1][j1]==0):
            i,j,k = i1,j1,k1
            break
f=np.array(a)
for stroka in range(n):
    f[stroka]=(stroka+1)*f[stroka]
print(f)