import sys

input = sys.stdin.readline


def solution():


    N = int(input())

    if N == 1:
        print(1%10007)
        return

    dp = [0] * (N+1)

    dp[1] = 1
    dp[2] = 2

    
    for i in range(3,N+1):
        dp[i]= dp[i-1] + dp[i-2]

    print(dp[-1] % 10007)


solution()    
    