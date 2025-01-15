n=eval(input())
passage=input().split(' ',n-1)
answer=''
sum1,i=0,0
while i<n:
    sum1+=len(passage[i])+1
    if sum1>81:
        sum1=0
        print(answer[:-1])
        answer=''
    else:
        answer+=passage[i]+' '
        i+=1
print(answer)


