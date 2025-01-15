a,b,c=map(int,input().split())
sum1=0
lst=[]
def s(x):
    sum2=0
    for num in str(x):
        sum2 += int(num)
    return sum2
for i in range(1,100000):
    if i == b*s(i)**a + c:
        sum1 += 1
        lst.append(i)
print(sum1)
for element in lst:
    print(element)

