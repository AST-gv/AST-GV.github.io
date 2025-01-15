n=int(input())
lst=list(map(int,input().split()))
lst.sort()
queue=[]
for i in range(n):
    if lst[i] >= sum(queue):
        queue.append(lst[i])
print(len(queue))
