from collections import deque

def solution():

    N, M = map(int,input().split())
    maze =  [list(map(int,input().strip())) for _ in range(N)]
    que = deque([(0,0)])
    distance = [[0]*M for _ in range(N)]
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    distance[0][0] = 1

    while que:
        x, y = que.popleft()
        if x == N-1 and y == M-1:
            print(distance[x][y])
        
        for nx, ny in move:
            nx = nx+x
            ny = ny+y
            if 0 <= nx < N and 0<= ny <M:
                if distance[nx][ny] == 0 and maze[nx][ny] == 1:
                    distance[nx][ny] = distance[x][y] +1
                    que.append((nx,ny))
            
          
solution()