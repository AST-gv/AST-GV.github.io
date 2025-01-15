n,q = map(int,input().split())
lst = []
for _ in range(q):
    lst.append(tuple(map(int,input().split())))

def zhc():
    for i in range(q):
        for j in range(q):
            if lst[i][1] == lst[j][0] and (lst[j][1],lst[i][0]) in lst:
                return 'Yes'
    return 'No'
print(zhc())