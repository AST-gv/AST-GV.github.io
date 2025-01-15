t = int(input())
output = []
for _ in range(t):
    n = int(input())
    lst = []
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    for i in range(n):
        lst.append((lst1[i], lst2[i]))
    lst.append((0, 0))
    lst.sort(reverse = True)
    zhc = 0
    for i in range(n + 1):
        if zhc >= lst[i][0]:
            output.append(min(zhc, lst[i - 1][0]))
            break
        zhc += lst[i][1]
    else:
        output.append(zhc)
print(*output, sep = '\n')
