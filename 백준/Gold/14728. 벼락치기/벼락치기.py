

def solution():


    N , M = map(int,input().split())
    lis =  [[0,0]] +  [list(map(int, input().split())) for _ in range(N)] 
    dp = [ [0]*(M+1) for _ in range(N+1) ]
    

    for i in range(1,N+1):
        time = lis[i][0]
        score = lis[i][1]

        for j in range(1,M+1):

            if j >= time :
                dp[i][j] = max(dp[i-1][j-time] +score , dp[i-1][j])
                # 현재 최대 시간(j)이 현재 time 보다 큼 -> 현재 값 넣음
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                # 현재 최대 시간이 현재 time 보다 작을 때 -> 현재 값 안넣음 
    print(dp[N][M])

solution()