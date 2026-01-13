import sys
input = sys.stdin.readline
from collections import deque

N, M =map(int,input().split())
lis = [ list(map(int,input().split())) for _ in range(N)]



def bfs(x,y):

    que = deque([(x,y)])
    lis[x][y] = 0
    size = 1

    while que:
        cur_x,cur_y = que.popleft()
        for x, y in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx,ny = cur_x+x,cur_y+y

            if 0<= nx< N and 0<= ny <M:
                if lis[nx][ny]==1:
                    lis[nx][ny] =0
                    que.append((nx,ny))
                    size+=1

    return size


ans = []

for i in range(N):
    for j in range(M):
        if lis[i][j] == 1:
            ans.append(bfs(i,j))


print(len(ans))
if ans:
    print(max(ans))
else:
    print(0)

    


