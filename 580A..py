n=int(input())
lst=list(map(int,input().split()))
sum=0
sum1=0
for i in range(n-1):
    if lst[i+1] >= lst[i]:
        sum1 += 1
    if sum<sum1:
        sum=sum1
    if  lst[i+1] < lst[i]:
        sum1=0
print(sum+1)
