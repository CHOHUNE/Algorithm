def solution():
   
    N = int(input())
    M = [0] + list(map(int,input().split()))
    
    arr = [0] * (N+1)
    
    for i in range(1,N+1):
        arr[i] = max(0,arr[i-1]) + M[i]
        
    print(max(arr[1:]))
    
solution()