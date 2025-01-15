lst = [[0] * 1025 for _ in range(1025)]
d = int(input())
n = int(input())
x_max = 0
x_min = 0
y_max = 0
y_min = 0
for _ in range(n):
    x, y, i = map(int,input().split())
    x_max = max(x, x_max)
    y_max = max(y, y_max)
    x_min = min(x, x_min)
    y_min = min(y, y_min)
    lst[x - 1][y - 1] = i
zhc = 0
output = 0
for i in range(x_min + d, x_max - d):
    for j in range(y_min + d, y_max - d):
        temp = 0
        for a in range(-d, d + 1):
            for b in range(-d, d + 1):
                temp  += lst[i + a][j + b]
        if temp > zhc:
            zhc = temp
            output = 1
            break
        if temp == zhc:
            output += 1
print(f'{output} {zhc}')