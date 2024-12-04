def solution():
    A,B=map(int,input().split())
    arr = list(map(int,input().split()))
    
    prefix= [0 for _ in range(A+1)]
    

    for i in range(A):
        prefix[i+1]=prefix[i]+arr[i]
    maxi =prefix[B]-prefix[0]
    for k in range(B,A+1):
        maxi= max(maxi,prefix[k]-prefix[k-B])
    print(maxi)
solution()