n=int(input())
lst=list(map(int,input().split()))
lst.sort()
sum1=0
while lst[0] != lst[-1]:
   s=lst[0]
   useless=[lst[0]]
   for i in range(1,len(lst)):
       if lst[i] > s:
            s=lst[i]
            useless.append(s)
   for element in useless:
       lst.remove(element)
   sum1+=1
   if lst == []:
       break
print(sum1 + len(lst))

