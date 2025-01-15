t=int(input())
lst=[]
for _ in range(t):
    m=input()
    if 360/(180-int(m))==int(360/(180-int(m))):
        lst.append("YES")
    else:
        lst.append("NO")
for i in lst:
    print(i)