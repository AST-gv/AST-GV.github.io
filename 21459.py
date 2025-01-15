x=int(input())
lst=[]

while True:
    if x == 1:
        break
    else:
        if x % 2 == 0:
            lst.append(f'{x}/2={x//2}')
            x//=2
        else:
            lst.append(f'{x}*3+1={3*x+1}')
            x=3*x+1
for i in lst:
    print(i)