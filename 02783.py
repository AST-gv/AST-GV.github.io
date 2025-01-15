n = int(input())
lst1 = []
lst2 = []
zhc1 = []
zhc2 = []
sum1 = 0
for i in range(n):
    a,b=map(int,input().split())
    lst1.append((a,b,i))
    lst2.append((b,a,i))
lst1.sort()
lst2.sort()
useless=input()
for i in range(n):
    for j in range(i):
        if lst1[j][1] <= lst1[i][1] and lst1[j][0] < lst1[i][0]:
            break
    else:
        zhc1.append(lst1[i][2])
for i in range(n):
    for j in range(i):
        if lst2[j][1] <= lst2[i][1] and lst2[j][0] < lst2[i][0]:
            break
    else:
        zhc2.append(lst2[i][2])
for i in zhc1:
    if i in zhc2:
        sum1 += 1

print(sum1)