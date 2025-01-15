m=eval(input())
for i in range(m):
    a,b,c,d=map(int,input().split(" "))
    if(a+b+c+d==24 or a+b+c-d==24 or a+b-c+d==24 or a-b+c+d==24 or -a+b+c+d==24 or a+b-c-d==24 or a-b-c+d==24 or a-b+c-d==24 or -a-b+c+d == 24 or -a+b-c+d==24 or -a+b+c-d==24 or a-b-c-d==24 or -a+b-c-d==24 or -a-b-c+d==24 or -a-c+c-d==24 or -a-b-c-d==24):
        print("YES")
    else:
        print("NO")