a=input()
b=input()
n=len(a)
a=a.lower()
b=b.lower()
for i in range(n):
    if a[i]<b[i]:
        print(-1)
        break
    if a[i]>b[i]:
        print(1)
        break
    if i==n-1:
        print(0)

