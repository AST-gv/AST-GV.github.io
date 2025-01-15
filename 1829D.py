m=int(input())
lst=[]
for _ in range(m):
    a,b=map(int,input().split())
    sum1=0
    while a%3 == 0:
        a //=3
        sum1 += 1
    for _ in range(sum1+1):
        if a == b:
            lst.append('Yes')
            break
        a *= 2
    else:
        lst.append('No')
for element in lst:
        print(element)