n=input()
b=int(input())
c=int(input())
d=0
for i in range(len(n)):
    d+=int(n[i])*b**(len(n)-i-1)
k=''
while d!=0:
    k=str(d%c)+k
    d//=c
print(k)