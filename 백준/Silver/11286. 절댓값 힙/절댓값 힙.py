import heapq
import sys

input = sys.stdin.readline


def solution():
    
    N = int(input())
    que = []
    
    
    for _ in range(N):
        i = int(input())
        if i == 0:
            if len(que) == 0:
                print(0)
            else:
                temp = heapq.heappop(que)
                print(temp[1])
        else:
            heapq.heappush(que,(abs(i),i))
solution()
