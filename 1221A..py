q = int(input())
lst = []
output = []
zhc = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
for i in range(q):
    n = int(input())
    lst = list(map(int,input().split()))

    while True:
        if 2048 in lst:
            output.append('YES')
            break

        sig = 0

        for num in zhc:
            if lst.count(num) > 1:
                lst.remove(num)
                lst.remove(num)
                lst.append(2 * num)
                sig = 1

        if sig == 0:
            output.append('NO')
            break

print(*output, sep = '\n')