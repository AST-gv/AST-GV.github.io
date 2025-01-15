a, b, k = map(int,input().split())
r = [0] * k
s = [0] * k
p = [0] * k
t = [0] * k
for i in range(k):
    r[i], s[i], p[i], t[i] = map(int,input().split())

temp = (max(p) - 1) // 2
lst = [[1] * (b + 2 * temp) for _ in range(a + 2 * temp)]
for i in range(k):
    if t[i] == 0:
        for m in range(temp + r[i] -1 -(p[i]-1)//2, temp + r[i] - 1 +(p[i]-1)//2 + 1):
            for n in range(temp + s[i] - 1 -(p[i]-1)//2, temp + s[i] - 1 +(p[i]-1)//2 + 1):
                lst[m][n] = 0
    if t[i] == 1:
        for m in range(temp, a + temp):
            for n in range(temp, b + temp):
                if temp + r[i] - 1 -(p[i]-1)//2 <= m <= temp + r[i] - 1 + (p[i]-1)//2 and temp + s[i] - 1 -(p[i]-1)//2 <= n <= temp + s[i] - 1 +(p[i]-1)//2:
                    continue
                else:
                    lst[m][n] = 0
zhc = 0
for i in range(temp, a + temp):
    for j in range(temp, b + temp):
        zhc += lst[i][j]
print(zhc)