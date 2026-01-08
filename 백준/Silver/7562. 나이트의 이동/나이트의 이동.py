import sys
from collections import deque
input = sys.stdin.readline

def solution():

    N = int(input())

    for _ in range(N):

        M = int(input())
        
        start = tuple(map(int,input().split()))
        end = tuple(map(int,input().split()))
        visited = [ [0]*M for _ in range(M)]
        que = deque([(start[0],start[1],0)])
        visited[start[0]][start[1]] = 1

        while que:            

            x,y,dist = que.popleft()

            if (x,y) == end:
                print(dist)
                break

            for m_x,m_y in [(1,2),(-1,2),(2,1),(-2,1),(1,-2),(-1,-2),(2,-1),(-2,-1)]:

                nx = x + m_x
                ny = y + m_y

                if 0 <= nx < M and 0<= ny < M:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        que.append((nx,ny,dist+1))

solution()