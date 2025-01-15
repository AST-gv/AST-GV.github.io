n=input()
s=0
for _ in range(int(n)):
    a,b,c=map(int,input().split())
    if a+b+c>1:
        s+=1
print(s)

