a=int(input())
if(a%2!=0):
    print(0,0)
else:
    if(a%4==0):
        m=a/4
    if(a%4==2):
        m=(a+2)/4
    n=a/2
    print(int(m),int(n))

