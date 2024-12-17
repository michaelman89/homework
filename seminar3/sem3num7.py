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
print(delta)
solve=[]
for jk in range(m-1):
    xm1=xm
    for y in range(n):
        xm1[y][m-2-jk]=tm[y][0]
    print(xm1)
    delta1=np.linalg.det(xm1)
    solve.append(delta1)
print(solve)




