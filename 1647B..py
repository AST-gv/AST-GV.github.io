t= int(input())
lst=[]
def judge(m):
    sum2,sum3=0,0
    while m%2 == 0 :
        m//=2
        sum2 += 1
    while m % 3 == 0 :
        m//=3
        sum3 += 1
    if m != 1 or sum2 > sum3:
        return -1
    else:
        return 2*sum3-sum2

for _ in range(t):
    a=int(input())
    lst.append(judge(a))
for element in lst:
    print(element)