import sys
import math
x=eval(input())
if x<6 or x%2==1:
    print('Error!')
    sys.exit()
def prime(m):   #是质数返回0，不是质数返回1
    i=3
    while i<=math.sqrt(m):
        if m%i==0:
            return 1
        i+=2
    return 0
j=3
while j<=x/2:
    if prime(j)==0 and prime(x-j)==0:
        print(f"{x}={j}+{x-j}")
    j+=2


