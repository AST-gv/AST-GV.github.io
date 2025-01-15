n=int(input())
i,s=2,0
while i<=n:
    if n%i==0:
        if n%(i*i)==0:
            print(0)
            break
        else:
            n/=i
            s+=1
    i+=1
else:
    if(s%2)==0:
        print(1)
    else:
        print(-1)


