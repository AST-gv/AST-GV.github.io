for _ in range(int(input())):
    n = int(input())
    lst = []
    zhc = 0
    for x in list(map(int, input().split())):
        if x == 0:
            zhc += 1
            left, right, i = 0, 1, 0
            while right <= len(lst):
                temp = lst[right - 1]
                while i >= left:
                    if temp == 0:
                        zhc += 1
                        left = right
                        right = left + 1
                        i = right - 1
                        break
                    else:
                        i -= 1
                        temp += lst[i]
                else:
                    right += 1
                    i = right - 1
            lst = []
        else:
            lst.append(x)

    left, right, i = 0, 1, 0
    while right <= len(lst):
        temp = lst[right - 1]
        while i >= left:
            if temp == 0:
                zhc += 1
                left = right
                right = left + 1
                i = right - 1
                break
            else:
                i -= 1
                temp += lst[i]
        else:
            right += 1
            i = right - 1
    print(zhc)

