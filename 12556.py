lst=list(input().lower())
n=len(lst)
s=1
for i in range(1,n):
    if lst[i]==lst[i-1]:
        s+=1
    if lst[i]!=lst[i-1]:
        print(f'({lst[i-1]},{s})',end='')
        s=1
print(f'({lst[-1]},{s})')



