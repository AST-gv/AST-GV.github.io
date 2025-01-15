output = []

while True:
    r, n = map(int,input().split())
    if r == -1 and n == -1:
        break
    army = sorted(map(int,input().split()))
    zhc = 0

    while army:
        pre = army[0]
        for i in range(1, len(army) + 1):
            if army[-i] <= pre + r:
                middle = army[-i]
                break
        for j in range(len(army)):
            if army[j] > middle + r:
                army = army[j:]
                break
        else:
            zhc += 1
            break
        zhc += 1

    output.append(zhc)

print(*output, sep = '\n')



