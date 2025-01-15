from collections import deque
n, d = map(int, input().split())
h = deque(int(input()) for _ in range(n))
ans = []

while h:
    max_val = h[0]
    min_val = h[0]
    inlist = []

    for _ in range(len(h)):
        m = h.popleft()
        if abs(m - max_val) <= d and abs(m - min_val) <= d:
            inlist.append(m)
        else:
            h.append(m)

        if m > max_val:
            max_val = m
        if m < min_val:
            min_val = m

        if max_val - min_val > 2*d:
            break

    ans += sorted(inlist)

print(*ans,sep = '\n')