def solution():
    A = int(input())
    arr = list(map(int,input().split()))
    
    prefix = [0 for _ in range(A+1)]
    
    for i in range(A):
        prefix[i+1]= max(prefix[i]+arr[i],arr[i])
    print(max(prefix[1:]))
    
solution()