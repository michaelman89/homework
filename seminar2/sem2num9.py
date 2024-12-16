f=open('input.txt')
s=list(map(str, f.readlines()))
c=0
for i in s:
    for j in range(len(i)):
        if j==len(i)-1:
            if i[j]=='.' or i[j]=='!' or i[j]=='?':
                c+=1
        else:
            if (i[j]=='.' or i[j]=='!' or i[j]=='?') and i[j+1]!='.' and i[j+1]!='!' and i[j+1]!='?':
                c+=1
print(c)