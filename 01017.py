import math
output=[]
a,b,c,d,e,f=1,1,1,1,1,1
def xxh(m):
    if m % 4 == 1:
        return 5
    elif m % 4 == 2:
        return 3
    elif m % 4 == 3:
        return 1
    else:
        return 0
while sum([a,b,c,d,e,f]) != 0:
    plus = 0
    a,b,c,d,e,f=map(int,input().split())
    zhc=sum([a,4*b,9*c,16*d,25*e,36*f]) #箱子占的总格子数
    plus += sum([d,e,f]) + math.ceil(c / 4) #3以上的箱子能占多少大箱子
    two=5 * d + xxh(c)
    if b > two:
        plus += math.ceil((b-two) / 9 )
    if 36*plus >= zhc:
        output.append(plus)
    else:
        output.append(math.ceil(zhc / 36))
for i in output[:-1]:
    print (i)