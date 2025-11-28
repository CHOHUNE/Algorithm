import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def solution():

    
    N , M = map(int,input().split())

    graph = [ [] for _ in range(N+1)]
    
    cnt = 0
    for _ in range(M):
        x, y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * (N+1)

    def dfs(start):
        visited[start] =True
        for i in graph[start]:
            if visited[i] == False:
                dfs(i)
        

    cnt = 0 

    for i in range(1,N+1):
            if not visited[i]:

                dfs(i)
                cnt+=1

    print(cnt)
solution()