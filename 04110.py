n,w = map(int,input().split())
lst=[]
for _ in range(n):
    a,b = map(int,input().split())
    lst.append((a/b,a,b))
lst.sort(reverse=True)
zhc,zhc1 = 0,0
i = 0
while True:
    if i == n:
        break
    else:
        if zhc1 + lst[i][2] <= w:
            zhc += lst[i][1]
            zhc1 += lst[i][2]
        else:
            zhc += (w - zhc1) * lst[i][0]
            break
        i += 1
print(f'{zhc:.1f}')