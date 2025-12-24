import sys

input = sys.stdin.readline

def solution():

    N, M = map(int,input().split())

    lis = [list(map(int,input().split())) for _ in range(N)]
    #합을 구해야 하는 횟수와 x1,y1 부터 x2,y2 까지 구함

    lis_2 = [list(map(int,input().split())) for _ in range(M)]
    #합을 추출해야 하는 배열

    #x2,y2 - [x2 -1, y2] - [x1,y2 -1] + [x1,y1]

    sum_lis = [[0]*(N+1) for _ in range(N+1)]
    
    for i in range(1,N+1):
        for j in range(1,N+1):
            sum_lis[i][j] = lis[i-1][j-1] + sum_lis[i-1][j] + sum_lis[i][j-1] - sum_lis[i-1][j-1]

    
    for x1,y1,x2,y2 in lis_2:
        ans = sum_lis[x2][y2] - sum_lis[x2][y1-1] - sum_lis[x1-1][y2] + sum_lis[x1-1][y1-1]
        print(ans)

solution()
    

