n, m = map(int, input().split())
lst = [int(x) for x in input().split()]
zhc = {}
w = set()
len_w = 0
for i in range(n - 1, -1, -1):
    if not lst[i] in w:
        len_w += 1
        w.add(lst[i])
    zhc[i] = len_w
output = []
for _ in range(m):
    output.append(zhc[int(input()) - 1])
print(*output, sep='\n')