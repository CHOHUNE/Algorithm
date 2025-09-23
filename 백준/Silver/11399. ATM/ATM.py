def solution():

    N = int(input())
    M = list(map(int,input().split()))

    M.sort()

    dp = [0] *(N+1)
    dp[0] = M[0]

    for i in range(1,N):

        dp[i] += M[i] + dp[i-1]

    print(sum(dp))



solution()

