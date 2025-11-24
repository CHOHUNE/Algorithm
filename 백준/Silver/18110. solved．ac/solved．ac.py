import sys

input = sys.stdin.readline

def rounding(N):
    if N >= 0:
        return int(N + 0.5)
    else:
        return int(N - 0.5)

def solution():

    N = int(input())
    if N == 0:
        print(0)
        return
    
    lis = [int(input()) for _ in range(N)]
    half_cut = rounding(N * 0.15)
    
    lis.sort()
    ans = []
    
    for i in range(half_cut,N-half_cut):
        ans.append(lis[i])
        
    print(rounding(sum(ans)/len(ans)))

solution()
