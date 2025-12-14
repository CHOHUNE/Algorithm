import sys
from collections import deque
input = sys.stdin.readline

def solution():


    M = int(input())


    for i in range(M):

        cmd = input().strip()
        N = int(input())
        origin_lis = input().strip()

        if origin_lis == "[]":
            que = deque()
        else:
            que = deque(origin_lis[1:-1].split(','))

        reverse_flag = False
        error = False

        for each in cmd:

            if each == "R":
                reverse_flag = not reverse_flag
            else:

                if not que:
                    print("error")
                    error = True
                    break
                else:
                    if reverse_flag:
                        que.pop()
                    else: 
                        que.popleft()

        if not error:
            if reverse_flag:

                que.reverse()

            print("[",end='')
            print(*que, sep=',',end='')
            print("]")




solution()
