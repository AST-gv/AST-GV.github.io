t = int(input())
output = []

for _ in range(t):
    n, x = map(int, input().split())
    lst = list(map(int, input().split()))

    if sum(lst) % x != 0:
        output.append(n)
        continue

    for i in range(n):
        if lst[i] % x != 0:
            left = i + 1
            break
    else:
        output.append(-1)
        continue

    for j in range(1, n + 1):
        if lst[-j] % x != 0:
            right = j
            break

    output.append(n - min(left, right))

print(*output, sep='\n')