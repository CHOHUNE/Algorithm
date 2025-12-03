import sys 
input = sys.stdin.readline
def solution():
    
    N = int(input())
    lis = [ list(map(int,input().split())) for _ in range(N)]
                 
    for i in range(N-2,-1,-1):
        for j in range(i+1):
            lis[i][j] += max(lis[i+1][j], lis[i+1][j+1])
                 
    print(lis[0][0])
                 
solution()
                 

                
   

"""
이 문제는 매 번 최선의 값을 찾는 단순한 문제가 아니라
모든 선택을 고려해 최대값을 찾는 문제임.
-> 따라서 매 번 최선의 선택을 한다면 최대값이 보장이 안됨.
배열의 맨 밑에서 더한 값을 고쳐 나가는 방식으로 한다.


output 결과는 아래와 같음 
   30
  23 21
 20 13 10
7 12 10 10
4 5 2 6 5

"""
# 아래는 DP 임......
# def solution():

#     N = int(input())
    
#     dp = [-1]*(N)

#     dp[0] = int(input())
#     idx = 0

#     for i in range(1,N):

#         lis = list(map(int,input().split()))
#         max_lis, max_idx = max((lis[idx],idx),(lis[idx+1],idx+1))
#         dp[i] = dp[i-1]+ max_lis

#         idx = max_idx
        

#     print(dp)
# solution()

    