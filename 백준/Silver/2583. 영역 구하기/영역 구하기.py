import sys
input =sys.stdin.readline
from collections import deque

def solution():

    N, M, K = map(int,input().split())
    lis = [list(map(int,input().split())) for _ in range(K)]
    visited = [[0]*M for _ in range(N)]
    graph = [[0]*M for _ in range(N)]

    for x,y,nx,ny in lis:
        for mx in range(y,ny):
            for my in range(x,nx):
                graph[mx][my] = 1
    
    que = deque([])
    ea = 0 
    ans = []

    for i in range(N):
        for j in range(M):

            if graph[i][j] == 0 and visited[i][j] == 0:
                que.append((i,j))
                visited[i][j] =1 
                ea += 1
                area_size = 1 
                
                while que:
                    x,y = que.popleft()

                    for mx,my in [(1,0),(-1,0),(0,-1),(0,1)]:
                        nx = x + mx
                        ny = y + my

                        if 0<= nx < N and 0<= ny < M and visited[nx][ny] ==0 and graph[nx][ny] ==0:
                            visited[nx][ny] = 1
                            que.append((nx,ny))
                            area_size += 1 

                ans.append(area_size)
    ans.sort()
    print(ea)
    print(*ans,sep= ' ')


solution()