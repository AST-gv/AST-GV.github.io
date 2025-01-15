t=int(input())
output=[]
for _ in range(t):
    n,k=map(int,input().split())
    lst=[0] * n
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    lst_1=sorted(lst1)
    lst_2=sorted(lst2)
    for j in range(n):
        lst[lst1.index(lst_1[j])]=lst_2[j]
        lst1[lst1.index(lst_1[j])]='zhc'    #这里的两个index太耗时导致程序超时了
    output.append(lst)
for a in output:
    for b in a:
        print(b,end=' ')
    print('')

