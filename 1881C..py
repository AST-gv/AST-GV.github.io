import math
output = []
for _ in range(int(input())):
    n = int(input())
    zhc = math.ceil(n / 2)
    bey = 0
    lst = [[0] * n for _ in range(n)]
    for i in range(n):
        string = input()
        for j in range(n):
            lst[i][j] = ord(string[j])
    for i in range(zhc):
        for j in range(zhc):
            tem = max(lst[i][j], lst[n - j - 1][i], lst[n - i - 1][n - j - 1], lst[j][n - i - 1])
            bey += 4 * tem - sum([lst[i][j], lst[n - j - 1][i], lst[n - i - 1][n - j - 1], lst[j][n - i - 1]])
    output.append(bey)
for num in output:
    print(num)


