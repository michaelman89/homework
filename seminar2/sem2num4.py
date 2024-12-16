s=[str(x) for x in input().split()]
for k in range(1, len(s), 2):
    s[k-1],s[k]=s[k],s[k-1]
print(*s)