import sys
from collections import deque
input = sys.stdin.readline


def solution():

    start, end = map(int,input().split())

    que = deque([(start,1)])


    while que:

        cur = que.popleft()
        value, idx = cur 

        if value == end:
            print(idx)
            return

        if value > end :
            continue    

        que.append((value*2,idx+1))
        que.append((int(str(value)+'1'),idx+1))

    print(-1)

solution()