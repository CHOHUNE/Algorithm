import sys
input = sys.stdin.readline
from collections import deque

def solution():
    N   = int(input())
    lis = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    c_lis = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lis[i][j] == 1 :
                c_lis[i].append(j)

    for i in range(N):

        visited = [0] * N
        
        que = deque([i])
        
        while que:
            cur = que.popleft()

            for node in c_lis[cur]:
                if not visited[node]:
                    visited[node] = 1
                    que.append(node)

        print(*visited, sep=' ')
    
        
solution()
            

        