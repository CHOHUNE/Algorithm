def solution():
    A,B = map(int,input().split())
    arr = list(map(int,input().split()))
    
    prefix = [0 for _ in range(A+1)]
    
    for i in range(A):
        prefix[i+1]= prefix[i] + arr[i]
        
    res =[]
    
    for k in range(B,A+1):
        res.append(prefix[k]-prefix[k-B])
        
    print(max(res))
    
solution()