case = int(input())
output=[]
for _ in range(case):
    l,n = map(int, input().split())
    lst = list(map(int, input().split()))
    zhc = l / 2 - abs(lst[0] - l / 2)
    for i in range(1,n):
        if l / 2 - abs(lst[i] - l / 2) > zhc:
            zhc = l / 2 - abs(lst[i] - l / 2)
    a = max(max(lst),l - min(lst))
    output.append(f'{int(zhc)} {a}')
for element in output:
    print(element)

