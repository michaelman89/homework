def des(n,c):
    d=0
    for i in range(len(n)):
        d += int(n[i]) * c ** (len(n) - i - 1)
    return d
f=open('input.txt')
a,b,c=map(str, f.readline().split())
ops=f.readline().strip()
r=int(f.readline().strip())
a=des(a,r)
b=des(b,r)
c=des(c,r)
if ops=='+':
    s=a+b+c
if ops=='-':
    s=a-b-c
if ops=='*':
    s=a*b*c
kon=''
while s!=0:
    kon=str(s%r)+kon
    s//=r
out=open('output.txt','w')
out.write(kon)