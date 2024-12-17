n=int(input())
s=[1,1]
if n==1 or n==2:
    print(1)
else:
    for i in range(n-2):
        s.append(s[-1]+s[-2])
    print(s[-1])
