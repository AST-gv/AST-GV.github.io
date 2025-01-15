useless=input()
pre=list(map(int,input().split()))
post=sorted(pre)
m=input()
def ast(arr):
    newlist=[0] * (len(arr)+1)
    for i in range(1,len(arr)+1):
        newlist[i]=newlist[i-1] + arr[i-1]
    return newlist
lst=[]
sumpre=ast(pre)
sumpost=ast(post)
for _ in range(int(m)):
    typ,l,r=map(int,input().split())
    if typ == 1:
        lst.append(sumpre[r]-sumpre[l-1])
    if typ == 2:
        lst.append(sumpost[r]-sumpost[l-1])
for element in lst:
    print(element)
    #超时是不是因为每次都求sum太多了，应该只求一次，即采用累加的办法