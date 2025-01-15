lst=[]
string=0
while True:
    try:
        string=input()
        if string=='':
            break
        if string.count('@')!=1:
            lst.append('NO')
            continue
        if string[0]=='@' or string[0]=='.' or string[-1]=='@' or string[-1]=='.':
            lst.append('NO')
            continue
        m=string.find('@')
        n=string.find('.',m+2)
        if n==-1 or string[m+1]=='.' or string[m-1]=='.':
            lst.append('NO')
            continue
        lst.append('YES')
    except EOFError:
        break
for i in lst:
    print(i)