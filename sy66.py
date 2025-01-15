n=int(input())
if n <= 3:
    for i in range(1,n+1):
        print('*'* i)
else:
    print('*')
    print('**')
    for i in range(n-3):
        print('*' + ' ' * (i + 1) + '*')
    print('*' * n)