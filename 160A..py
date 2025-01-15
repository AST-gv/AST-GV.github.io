useless=int(input())
sum1=sum(lst := sorted(map(int,input().split()),reverse=True))
sum2,i=0,0
while sum2 <= sum1/2:
    sum2 += int(lst[i])
    i+=1
print(i)
