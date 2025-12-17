from collections import deque,defaultdict
import sys


def solution():

    N, M = map(int,input().split())
    
    
    ladder= defaultdict(int)
    for i in range(N+M):
        key,value = map(int,input().split())
        ladder[key] = value


    dist = [-1] * 101
    dist[1]=0
    que = deque([1])

    while que:

        cur_dist = que.popleft()
        for i in range(1,7):

            new_dist = cur_dist +i 
            if 1 <= new_dist <= 100:
                
                if ladder[new_dist] :
                    new_dist = ladder[new_dist]
                    
                if dist[new_dist] == -1 :
                    dist[new_dist] = dist[cur_dist] +1
                    que.append(new_dist)

    print(dist[-1])

solution()