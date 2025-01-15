while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    else:
        zhc = 0
        lst = [x for x in range(1,n + 1)]
        pre = 0
        while zhc < n - 1:
            del lst[(pre + m - 1) % (n - zhc)]
            pre = (pre + m - 1) % (n - zhc)
            zhc += 1
        print(lst[0])

