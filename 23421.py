n, b = map(int, input().split())
price = [0] + [int(x) for x in input().split()]
weight = [0] + [int(x) for x in input().split()]
bag = [[0] * (b + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, b + 1):
        if weight[i] <= j:
            bag[i][j] = max(bag[i - 1][j - weight[i]] + price[i], bag[i - 1][j])
        else:
            bag[i][j] = bag[i - 1][j]
print(bag[-1][-1])