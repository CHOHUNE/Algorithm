import sys
from queue import PriorityQueue

input =sys.stdin.readline

def solution():

    N = int(input())

    lis = PriorityQueue()

    for _ in range(N):

        each =int(input())
        if each == 0:
            if not lis.empty():
                temp = lis.get()
                print(-temp)
            else:
                print(0)
        else:
            lis.put(-each)


solution()