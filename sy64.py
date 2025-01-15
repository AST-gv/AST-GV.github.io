n=int(input())
lst=list(map(int,input().split()))
k=int(input())
i,sum1=0,0
lst.sort()
while lst[i] < k/2:
    if k-lst[i] in lst:
        sum1 += 1
    i += 1
print(sum1)