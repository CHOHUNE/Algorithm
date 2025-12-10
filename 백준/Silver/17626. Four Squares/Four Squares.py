import sys
input = sys.stdin.readline

def solution():

    N = int(input())

    dp = [float('inf')] *(N+1)
    dp[0] = 0
    dp[1] = 1

    
    for i in range(1,N+1):
        j = 1 
        
        while j*j <= i:
            dp[i] = min(dp[i-(j*j)]+1,dp[i])
            j += 1
            
    print(dp[-1])

solution()    
