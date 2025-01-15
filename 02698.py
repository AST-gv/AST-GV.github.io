s = []

def empty(l,x,y):
    for i in range(8):
        for j in range(8):
            if i == x or j == y or i - x == j - y or x - i == j - y:
                if l[i][j] == 1:
                    return False
    return True

def queen(n):
    if n == 1:
        lst = [[0] * 8 for _ in range(8)]
        for i in range(8):
            for j in range(8):
                temp = lst
                temp[i][j] = 1
                s.append(temp)
        return s
    else:
        for board in queen(n-1):
            for i in range(8):
                for j in range(8):
                    if empty(board,i,j):
                        temp = board
                        temp[i][j] = 1
                        s.append(temp)

            s.remove(board)
        return s

print(queen(8))


