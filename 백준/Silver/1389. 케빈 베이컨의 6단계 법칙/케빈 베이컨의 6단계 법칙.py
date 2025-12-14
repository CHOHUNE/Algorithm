import sys 
from collections import deque

def solution():

    N, M = map(int,input().split())
    lis = [[]*(N+1) for _ in range(N+1)]
    ans = [] 

    for _ in range(M):

        x,y = map(int,input().split())
        lis[x].append(y)
        lis[y].append(x)


    for i in range(N+1):

        visited = [False] * (N+1)
        distance= [0] * (N+1)

        que = deque([i])
        visited[i] = True

        while que:

            cur_node = que.popleft()

            for next_node in lis[cur_node]:

                if not visited[next_node]:
                    visited[next_node] = True

                    distance[next_node] = distance[cur_node] + 1 
                    que.append(next_node)

        ans.append((sum(distance),i))


    ans.sort()

    print(ans[1][1])


solution()