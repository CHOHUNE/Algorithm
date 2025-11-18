from collections import deque


def solution():


    S,E = map(int,input().split())
    dist = [-1] * 200000
    que = deque()
    dist[S]=0

    que.append(S)

    while que:
        
        cur_node = que.popleft()

        if cur_node == E:
            print(dist[cur_node])

        for new_x in (cur_node -1 , cur_node + 1 , cur_node * 2):
            if 0 <= new_x < len(dist) and dist[new_x] == -1:
                
                dist[new_x] = dist[cur_node] +1
                que.append(new_x)

solution()