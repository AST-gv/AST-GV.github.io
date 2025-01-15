n, m = map(int,input().split())
lst = [[0] * m for _ in range(n)]
zhc = float('-inf')

for i in range(n):
    www = list(map(int,input().split()))
    for j in range(m):
        lst[i][j] = www[j]
for i in range(n):
    for j in range(m):
        if lst[i][j] * (lst[0][j] * 1000 + lst[i][-1] * 100 + lst[-1][j] * 10 + lst[i][0])  > zhc:
            zhc = lst[i][j] * (lst[0][j] * 1000 + lst[i][-1] * 100 + lst[-1][j] * 10 + lst[i][0])
print(zhc)