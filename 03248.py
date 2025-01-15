import math
s=''
while True:
    try:
        a,b=map(int,input().split())
        s+=str(math.gcd(a,b))+'\n'
    except:
        break
print(s)

