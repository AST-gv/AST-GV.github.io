n=int(input())
lst=[0]*n
def ou(m):
    return int(m)%2
lst=list(map(ou,input().split()))
if sum(lst) == 1:
    print(lst.index(1)+1)
else:
    print(lst.index(0)+1)