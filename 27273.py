t=int(input())
lst=[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]
output=[]
for _ in range(t):
    a=int(input())
    sum1=a*(a+1)/2
    for element in lst:
        if element <= a:
            sum1-=2*element
        else:
            break
    output.append(sum1)
for s in output:
    print(int(s))

