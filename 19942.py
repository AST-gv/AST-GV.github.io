m, n, p, q = map(int, input().split())
big = [0] * m
small = [0] * p
for i in range(m):
    big[i] = list(map(int, input().split()))
for j in range(p):
    small[j] = list(map(int, input().split()))
for i in range(m + 1 - p):
    for j in range(n + 1 - q):

        sum_matrix = 0
        for a in range(p):
            for b in range(q):
                sum_matrix += big[i + a][j + b] * small[a][b]
        print(sum_matrix, end = ' ')
    print('')