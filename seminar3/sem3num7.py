import numpy as np
n,m=map(int, input().split())
f=[]
for k in range(n):
    f.append([int(x) for x in input().split()])
s=np.array(f)
x=[]
t=[]
for i in range(n):
    g=[]
    v=[]
    for p in range(m):
        if p!=m-1:
            g.append(s[i][p])
        else:
            v.append(s[i][p])
    x.append(g)
    t.append(v)
xm=np.array(x)
tm=np.array(t)
delta=np.linalg.det(xm)
solve=[]
d=np.array(x)
for jk in range(m-1):
    for y in range(n):
        d[y][jk]=tm[y][0]
    print(d)
    delta1=np.linalg.det(d)
    solve.append(delta1/delta)
    d=np.array(x)
print(*solve)


