import sys
from collections import deque

input =sys.stdin.readline

def solution():

    N =int(input())
    dual_graph = [[] for _ in range(N+1)] 

    for _ in range(N-1):

        x,y = map(int,input().split())
        dual_graph[x].append(y)
        dual_graph[y].append(x)
    
    visited = [False] * (N+1) #N 까지 선언되어야함 
    visited[0] = True
    visited[1] = True

    ans = [0] * (N+1)

    que = deque()
    que.append(1)
    while que:

        cur_idx = que.popleft()
        
        for next_node in dual_graph[cur_idx]:

            if visited[next_node] == False:
                visited[next_node] = True
                ans[next_node] = cur_idx
                que.append(next_node)
    
    print(*ans[2:],sep='\n')
    
solution()
