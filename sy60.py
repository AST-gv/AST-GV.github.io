a,b=map(int,input().split())
lst=[x ** 3 for x in range(10)]
output=[]

def daffodil(m):
    b=(m - m % 100)//100
    s=((m-100*b) - m % 10)//10
    g=m-100*b-10*s
    if  m == lst[b] + lst[s] + lst[g]:
        return True

for i in range(a,b+1):
    if daffodil(i):
        output.append(i)
if output == []:
    print('NO')
else:
    for element in output[0:-1]:
        print(element,end=' ')
    print(output[-1])