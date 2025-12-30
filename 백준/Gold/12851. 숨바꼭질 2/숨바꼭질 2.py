import sys
from collections import deque
input = sys.stdin.readline

def solution():

    N, M =map(int,input().split())
    visited = [float('INF')] * 100001
    visited[N] = 0
    cnt = [0]  * 100001
    cnt[N] = 1
    que = deque([N])
    

    while que:
        this_turn_number = que.popleft()

        for i in [this_turn_number+1, this_turn_number-1, this_turn_number*2]:
            if 0 <= i <= 100000:
                
                nd = visited[this_turn_number] + 1 

                if visited[i] > nd:
                    visited[i] = nd 
                    cnt[i] = cnt[this_turn_number]
                    que.append(i)
                elif visited[i] == nd:
                    cnt[i] += cnt[this_turn_number]

    print(visited[M])
    print(cnt[M])

solution()