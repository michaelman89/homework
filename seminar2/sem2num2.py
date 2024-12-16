g,s=input().split()
g=int(g)
default=list(s)
result=list(s)
for i in range(len(s)//g):
    for k in range(g):
        result[g*i+k]=default[g*(i+1)-k-1]
print(''.join(result))