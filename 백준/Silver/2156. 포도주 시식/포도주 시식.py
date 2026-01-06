import sys
input = sys.stdin.readline

def solution():

    N = int(input())
    lis = [0] + [ int(input()) for _ in range(N)]

    if N == 0 :
        print(0)
        return

    if N == 1 :
        print(lis[1])
        return

    if N ==2 :
        print(lis[1] + lis[2])
        return

    dp = [0] * (N+1)

    dp[1] = lis[1]
    dp[2] = lis[1]+lis[2]

    for i in range(3,N + 1):
        dp[i] = max(dp[i-1], dp[i-2]+lis[i],dp[i-3]+lis[i]+lis[i-1])

    print(dp[N])


solution()