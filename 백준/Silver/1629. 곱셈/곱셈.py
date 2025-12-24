def seper(N,M,L):
    
    if M == 0:
        return 1
    
    half = seper(N,M//2,L)
    half = (half*half) % L
    
    if M % 2 == 1:
        half = (half * N) % L
        
    return half

def solution():
    N,M,L = map(int,input().split())
    
    print(seper(N,M,L))
    
solution()
        