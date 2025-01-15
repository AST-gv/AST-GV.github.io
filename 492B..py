n,m,k=map(int,input().split())
lst=[[0]*(m+2) for _ in range(n+2)]
def judge(p,q):
    if lst[p + 1][q] and lst[p][q + 1] and lst[p + 1][q + 1]:
        return True
    if lst[p + 1][q] and lst[p][q - 1] and lst[p + 1][q - 1]:
        return True
    if lst[p - 1][q] and lst[p][q - 1] and lst[p - 1][q - 1]:
        return True
    if lst[p - 1][q] and lst[p][q + 1] and lst[p - 1][q + 1]:
        return True
s=0
for i in range(k):
    a,b=map(int,input().split())
    lst[a][b]=1
    if judge(a,b) :
        s=i+1
        break
print(s)