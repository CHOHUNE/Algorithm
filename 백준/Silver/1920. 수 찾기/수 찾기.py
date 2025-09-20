import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    lis_1 = set(map(int, input().split()))  # set으로 변경
    M = int(input())
    lis_2 = list(map(int, input().split()))
    
    for i in lis_2:
        if i in lis_1:  # set에서 in은 O(1)
            print(1)
        else:
            print(0)

solution()