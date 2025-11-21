from collections import deque
import sys

input = sys.stdin.readline


def solution() :

    N = int(input())

    lis = deque()
    for _ in range(N):

        cur_word = input().split()
        if cur_word[0] == "push":
            lis.append(cur_word[1])
        elif cur_word[0] == "front":
            if lis:
                print(lis[0])
            else:
                print(-1)
        elif cur_word[0] == "back":
            if lis:
                print(lis[-1])
            else:
                print(-1)
        elif cur_word[0] == "size":
            print(len(lis))
        elif cur_word[0] == "empty":
            if len(lis) == 0:
                print(1)
            else :
                print(0)
        elif cur_word[0] == "pop":
            if len(lis) == 0:
                print(-1)
            else:
                print(lis.popleft())

solution()
