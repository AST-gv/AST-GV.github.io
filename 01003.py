lst=[]
n,a=0,0
while a!='0.00':
    a=input()
    lst.append(float(a))
while n<len(lst)-1:
    i,s=2,0
    while s<lst[n]:
        s+=1/i
        i+=1
    print(f'{i-2} card(s)')
    n+=1





