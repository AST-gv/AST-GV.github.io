from collections import defaultdict

def  f(n,x1,y1,x2,y2):
    if dp[(n,x1,y1,x2,y2)] > 0:
        return dp[(n,x1,y1,x2,y2)]
    if n == 1:
        su = 0
        for i in range(x1,x2 + 1):
            for j in range(y1,y2 + 1):
                su += lst[i][j]
        dp[1,x1,y1,x2,y2] = su * su
        return su * su
    mi = float('inf')
    for i in range(x1 ,x2):
        mi = min(mi,f(n - 1,x1,y1,i,y2) + f(1,i + 1,y1,x2,y2))
        mi = min(mi, f(1, x1, y1, i, y2) + f(n - 1, i + 1, y1, x2, y2))
    for i in range(y1 , y2 ):
        mi = min(mi,f(n - 1,x1,i + 1,x2,y2) + f(1,x1,y1,x2,i))
        mi = min(mi, f(1, x1, i + 1, x2, y2) + f(n - 1, x1, y1, x2, i))
    dp[(n,x1,y1,x2,y2)] = mi
    return mi

m = int(input())
lst = []
for _ in range(8):
    lst.append([int(x) for x in input().split()])
s = 0
for i in lst:
    for j in i:
        s += j
s /= m
dp = defaultdict(int)
result = (f(m,0,0,7,7) / m - s ** 2) ** 0.5
print(f'{result:.3f}')