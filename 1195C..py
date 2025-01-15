n = int(input())
row1 = [int(x) for x in input().split()]
row2 = [int(x) for x in input().split()]
dp=[[0] * 3 for _ in range(n)]
dp[0][1] = row1[0]
dp[0][2] = row2[0]
for i in range(1, n):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = row1[i] + max(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = row2[i] + max(dp[i - 1][0], dp[i - 1][1])
print(max(dp[n - 1][1], dp[n - 1][2]))