import math
def solution():

    
    N = int(input())
    cnt = 0

    while True:

        if N // 5:
            N = N //5
            cnt += N
        else:
            break

    print(cnt)

solution()