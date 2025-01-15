def lucky(string):
    for m in string:
        if m != '4' and m != '7':
            break
    else:
        return True
n= int(input())
for i in range(1,n+1):
    if n%i == 0 and lucky(str(i)) :
        print('YES')
        break
else:
    print('NO')



