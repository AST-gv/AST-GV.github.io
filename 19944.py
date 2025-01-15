from math import floor
n=eval(input())
lst=[]
def zeller(c,y,m,d):
    w=(y+floor(y/4)+floor(c/4)-2*c+floor(2.6*(m+1))+d-1)%7
    tinydict={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    return tinydict[w]
for i in range(n):
    string=input()
    c=int(string[0:2])
    y=int(string[2:4])
    m=int(string[4:6])
    if m==1 or m==2:
        m+=12
        if y!=0:
            y-=1
        else:
            y=99
            c-=1
    d=int(string[6:8])
    lst.append(zeller(c,y,m,d))
output='\n'.join(lst)
print(output)
