import sys
from collections import deque
input = sys.stdin.readline

def solution():

    N, M =map(int,input().split())
    visited = [float('INF')] * 100001
    visited[N] = 0
    que = deque([N])

    while que:
        this_dist = que.popleft()

        for i in (this_dist+1, this_dist-1):
            if 0<= i < 100001:

                new_dist = visited[this_dist] +1

                if visited[i] > new_dist:
                    visited[i] = new_dist
                    que.append(i)


        if 0 <= this_dist*2 < 100001:
            if visited[this_dist] < visited[this_dist*2]:
                visited[this_dist*2] = visited[this_dist]
                que.append(this_dist*2)
                
    print(visited[M])

solution()