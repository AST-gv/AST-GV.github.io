def filestructure(level, di, ncase):
    v = []  #用来存储file
    print('|     ' * level,end = '')
    if level != 0:
        print(di)
    t = 0   #用来标记当前是否为ROOT层
    while True:
        s = input()
        if s == '#':
            return 0
        if t == 0 and level == 0:
            print('')
            print(f'DATA SET {ncase}:')
            print('ROOT')
            t = 1
        if s == '*':
            break
        if s[0] == 'f':
            v.append(s)
        if s[0] == 'd':
            filestructure(level + 1, s, ncase)
        if s[0] == ']':
            break
    v.sort()
    for it in v:
        print('|     ' * level, end='')
        print(it)
    return 1

ncase = 0
while True:
    ncase += 1
    end = filestructure(0,'ROOT',ncase)
    if end == 0:
        break

