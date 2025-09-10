def solution():
    
    N  = int(input())
    HP = list(map(int,input().split()))
    HAP = list(map(int,input().split()))
    
    dp = [0] * 100
    
    for i in range(N):
        if HP[i] >=100:
            continue
        for j in range(99,HP[i]-1,-1):
            dp[j] = max(dp[j],dp[j-HP[i]]+HAP[i])
            
    print(max(dp))
solution()
            