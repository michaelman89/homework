n=int(input())
o=n
prime_dividers=[]
for i in range(2,n):
    t=0
    if n%i>0:
        continue
    for j in prime_dividers:
        if i%j==0:
            t=1
    if t==1:
        continue
    prime_dividers.append(i)
dividers_power=[]
while n>1:
    for k in prime_dividers:
        c=0
        while n%k==0:
            n//=k
            c+=1
        dividers_power.append(c)
print(o,'= ', end='')
for i in range(len(prime_dividers)):
    if i!=len(prime_dividers)-1:
        print(prime_dividers[i],'^',dividers_power[i],' * ', sep='',end='')
    else:
        print(prime_dividers[i], '^', dividers_power[i], sep='', end='')
