n=int(input())
i=6
while i<=n/2:
    if n%i==0:
        print(int(n/i))
        break
    else:
        i+=1
else:
    print(1)