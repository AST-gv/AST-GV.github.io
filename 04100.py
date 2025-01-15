k = int(input())
for _ in range(k):
    n = int(input())
    lst = []
    max_time = 0
    min_time = float('inf')

    for _ in range(n):
        m, t = map(int, input().split())
        lst.append((m, t))
        if m < min_time:
            min_time = m
        if t > max_time:
            max_time = t

    w = 0
    we = []
    y = 0
    while lst:
        for i in range(min_time, max_time):
            zhc = 0
            for (a, b) in lst:
                if a <= i <= b:
                    zhc += 1
                    we.append((a, b))
            if zhc > w:
                w = zhc
                best = we
        we =[]
        k = []
        for element in lst:
            if element not in best:
                k.append(element)
        lst = k
        y += 1

    print(y)