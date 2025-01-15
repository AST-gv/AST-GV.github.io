#创建一个年份(y)+月份(m)与某一个数(x)之间的对应关系：x=(y-1900)*12+m-1;m=x%12+1,y=x//12+1900;2199年12月对应x=3599
lst = [0] * 3600
for x in range(3600):
    y = x // 12 + 1900
    m = x % 12 + 1
    if (y == 1900 and m == 2) or (y == 2100 and m == 2):
        lst[x] = 28
    else:
        if y % 4 == 0 and m == 2:
            lst[x] = 29
        else:
            if m == 1:
                lst[x] = 31
            if m == 2:
                lst[x] = 28
            if m == 3:
                lst[x] = 31
            if m == 4:
                lst[x] = 30
            if m == 5:
                lst[x] = 31
            if m == 6:
                lst[x] = 30
            if m == 7:
                lst[x] = 31
            if m == 8:
                lst[x] = 31
            if m == 9:
                lst[x] = 30
            if m == 10:
                lst[x] = 31
            if m == 11:
                lst[x] = 30
            if m == 12:
                lst[x] = 31
y,m,d =map(int,input().split('-'))
n=int(input())
x = (y - 1900) * 12 + m - 1
zhc = 0
while zhc < n + d:
    zhc += lst[x]
    x += 1
x -= 1
y = x // 12 + 1900
m = x % 12 + 1
print(f'{y}-{m:02}-{(lst[x]-(zhc-n-d)):02}')
