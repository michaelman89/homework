x=[float(x) for x in input().split()]
y=[float(y) for y in input().split()]
srx=0
sry=0
srx2=0
srxy=0
n=len(x)
for i in range(n):
    srx+=x[i]/n
    srx2+=x[i]**2/n
    sry+=y[i]/n
    srxy+=x[i]*y[i]/n
k=(srxy-srx*sry)/(srx2-srx**2)
b=sry-k*srx
print('y = kx + b')
print('k =',k)
print('b =',b)



