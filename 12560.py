n, m = map(int, input().split())
lst = [[0] * (m + 2) for _ in range(n + 2)]
output = [[0] * (m + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    temp = list(map(int,input().split()))
    for j in range(1, m + 1):
        output[i][j] = lst[i][j] = temp[j - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        zhc = lst[i][j + 1] + lst[i + 1][j + 1] + lst[i - 1][j] + lst[i - 1][j - 1] + lst[i][j - 1] + lst[i + 1][j] + lst[i + 1][j - 1] + lst[i - 1][j + 1]
        if lst[i][j]:
            if zhc < 2 or zhc > 3:
                output[i][j] = 0
        if not lst[i][j]:
            if zhc == 3:
                output[i][j] = 1
        print(output[i][j], end=' ')
    print('')
