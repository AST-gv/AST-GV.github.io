output = []
for _ in range(int(input())):
    zhc = 0
    s = int(input())
    input()
    lstA = list(map(int,input().split()))
    lstA.sort(reverse = True)
    input()
    lstB = list(map(int,input().split()))
    lstB.sort()
    for num in lstA:
        zhc += lstB.count(s - num)
        lstB = [i for i in lstB if i >= s - num]
    output.append(zhc)
for element in output:
    print(element)
