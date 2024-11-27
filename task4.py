s=open('input.txt')
k=open('output.txt','w')
a,b = map(int, s.readline().split())
z=s.readline()
if z=='-':
    k.write(str(a-b))
if z=='*':
    k.write(str(a*b))
if z==('+'):
    k.write(str(a+b))
