size,sym=input().split()
size=int(size)
for i in range(size//2):
    print((i+1)*sym)
print(sym*(size//2+1))
for j in range(size//2,0,-1):
    print(sym*j)