l,m=map(int,input().split())
trees=[1]*(l+1)
for i in range(m):
    a,b=map(int,input().split())
    trees[a:b+1]=[0]*(b+1-a)
print(sum(trees))