n,m = map(int,input().split())
zhc = n
i = 0
while zhc > 0:
    i += 1
    if i % m == 0:
        zhc += 1
    zhc -= 1
print(i)