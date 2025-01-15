def qpl(n, lst, m):
    if n == 1:
        print(*lst, sep=' ')
        return
    for i in range(1, m):
        if not i in lst:
            qpl(n - 1, lst + [i], m)
m = int(input()) + 1
qpl(m,[], m)
