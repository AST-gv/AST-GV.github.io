numbers=[1,2,3,4,5,6,8,9,10,11,12,13,15,16,18,19,20,22,23,24,25,26,29,30,31,32,33,34,36,38,39,40,41,43,44,45,46,48,50,51,52,53,54,55,58,59,60,61,62,64,65,66,68,69,80,81,82,83,85,86,88,89,90,92,93,94,95,96,99]
n=eval(input())
i,sum=0,0
while numbers[i]<=n:
    sum+=numbers[i]**2
    if numbers[i]>=n:
        break
    i+=1
print(sum)

