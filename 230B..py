n = input()
lst=list(map(int,input().split()))
for num in lst:
    a = num ** 0.5
    if a.is_integer() and a > 1:
        if a == 2:
            print('YES')
            continue
        for i in range(2, int(a / 2) + 1):
            if int(a) % i == 0:
                print('NO')
                break
        else:
            print('YES')
    else:
        print('NO')