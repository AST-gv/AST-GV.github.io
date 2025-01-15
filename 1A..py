n,m,a=map(int,input().split())
def flagstone(k,a):
    if(k%a==0):
        r=k//a
    else:
        r=k//a+1
    return(r)
i=flagstone(n,a)
j=flagstone(m,a)
s=i*j
print(s)