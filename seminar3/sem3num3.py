def evklid(a, b):
    if a == 0:
        return 0, 1, b
    else:
        x, y, q = evklid(b%a, a)
    return y-(b//a)*x,x,q
a,b=map(int, input().split())
print(*evklid(a,b))