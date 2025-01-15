n = int(input())
lst = [int(x) for x in input().split()]
dp = [''] * n
zhc = 0
if lst[0] == 0:
    zhc = 1
    dp[0] = 'rest'
elif lst[0] == 1:
    dp[0] = 'match'
elif lst[0] == 2:
    dp[0] = 'exercise'
else:
    dp[0] = 'either'

for i in range(1, n):
    if lst[i] == 0:
        zhc += 1
        dp[i] = 'rest'
    elif lst[i] == 1:
        if dp[i - 1] != 'match':
            dp[i] = 'match'
        else:
            dp[i] = 'rest'
            zhc += 1
    elif lst[i] == 2:
        if dp[i - 1] != 'exercise':
            dp[i] = 'exercise'
        else:
            dp[i] = 'rest'
            zhc += 1
    else:
        if dp[i - 1] == 'rest':
            dp[i] = 'either'
        elif dp[i - 1] == 'exercise':
            dp[i] = 'match'
        elif dp[i - 1] == 'match':
            dp[i] = 'exercise'
        else:
            dp[i] = 'either'
print(zhc)