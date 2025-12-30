import sys
from collections import deque
input = sys.stdin.readline

def solution():

    N, M = map(int,input().split())

    ans = 0
    que = deque([(N,0)])
    visited = [False] * 100001 
    visited[N] = True

    while que:
        this_turn_number,sec = que.popleft()

        if this_turn_number == M:
            print(sec)
            return 

        a = this_turn_number + 1
        b = this_turn_number - 1
        c = this_turn_number * 2

        for i in [a,b,c]:
            if 0 <= i < 100001:
                if visited[i] == False:
                
                    visited[i] = True
                    que.append((i,sec+1))


solution()