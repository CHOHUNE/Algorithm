import sys
input = sys.stdin.readline
from collections import deque

def solution():


    N = int(input())

    lis = [list(map(int,input().split())) for _ in range(N)]

    ans = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):

                if lis[j][i] and lis[i][k]:
                    lis[j][k] = 1 

    for i in range(N):
        print(*lis[i], sep=' ')
    # 

    # 아래는 bfs 풀이 -> 경로 찾기와 달리 해당 문제는 bfs가 한 번만 실행되는 게 아니라
    # 각 라인 마다 독립적으로 실행 된다.
    # 따라서 visted 와 que를 for 루프 안에서 반드시 초기화 하는 과정이 필요하다. 
    
    # N   = int(input())
    # lis = [list(map(int,input().split())) for _ in range(N)]
    # visited = [[0]*N for _ in range(N)]

    # c_lis = [[] for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         if lis[i][j] == 1 :
    #             c_lis[i].append(j)

    # for i in range(N):

    #     visited = [0] * N
        
    #     que = deque([i])
        
    #     while que:
    #         cur = que.popleft()

    #         for node in c_lis[cur]:
    #             if not visited[node]:
    #                 visited[node] = 1
    #                 que.append(node)

    #     print(*visited, sep=' ')
    
        
solution()
            

        