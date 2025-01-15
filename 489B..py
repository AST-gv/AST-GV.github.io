sum1=0
n=int(input())
lst1=list(map(int,input().split()))
lst1.sort()
m=int(input())
lst2=list(map(int,input().split()))
lst2.sort()
for num in lst1:
    if num-1 in lst2:
        sum1 += 1
        lst2.remove(num-1)
        continue
    if num in lst2:
        sum1 += 1
        lst2.remove(num)
        continue
    if num+1 in lst2:
        sum1 += 1
        lst2.remove(num+1)
print(sum1)

