n = int(input())
lst = [int(x) for x in input().split()]
dp = [1] * n
for i in range(n):
    maxn = 1
    for j in range(i):
        if lst[i] > lst[j] and dp[j] + 1 > maxn:
            maxn = dp[j] + 1
    dp[i] = maxn
print(max(dp))