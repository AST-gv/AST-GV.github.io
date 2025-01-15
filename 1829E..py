from collections import deque
def bfs(x,y):
    cnt = field[x][y]
    field[x][y] = 0
    queue = deque([(x,y)])
    while queue:
        x,y = queue.pop()
        for k in range(4):
            nx,ny = x + dx[k],y + dy[k]
            if field[nx][ny]:
                queue.append((nx,ny))
                cnt += field[nx][ny]
                field[nx][ny] = 0
    return cnt
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    field = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(1,n + 1):
        field[i][1:-1] = list(map(int,input().split()))
    best = 0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in range(1,m + 1):
        for j in range(1,n + 1):
            if field[j][i]:
                best = max(best,bfs(j,i))
    print(best)
