n=int(input())
dic={}
lst1=[]
lst2=[]
for i in range(n):
    a,b=map(int,input().split())
    dic[a]=b
    lst1.append(a)
    lst2.append(b)
lst1=sorted(lst1)
lst2=sorted(lst2)
for i in range(len(lst1)):
    if dic[lst1[i]] != lst2[i]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")