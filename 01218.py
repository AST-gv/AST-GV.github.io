a = int(input())
output=[]
for _ in range(a):
    n=int(input())
    lst = [False] * n
    for i in range(n):
        for j in range(n):
            if (j + 1) % (i + 1) == 0:
                lst[j] = not lst[j]
    output.append(sum(lst))
for element in output:
    print(element)