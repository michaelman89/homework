dict={'A':'A','H':'H','I':'I','M':'M','O':'O', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y','1':'1','8':'8', 'E':'3', 'J':'L', 'S':'2', 'Z':'5', '3':'E', 'L':'J', '2':'S', '5':'Z'}
s=input()
rp=True
ms=True
for k in range(len(s)):
    if s[k]!=s[len(s)-1-k]:
        rp=False
    if s[k] in dict:
        if dict[s[k]]!=s[len(s)-1-k]:
            ms=False
    else:
        ms=False
print(s,end='')
if rp==False and ms==False:
    print(' is not a palindrome')
if rp==True and ms==False:
    print(' is a regular palindrome')
if rp == False and ms == True:
    print(' is a mirrored string')
if rp==True and ms==True:
    print(' is a mirrored palindrome')
