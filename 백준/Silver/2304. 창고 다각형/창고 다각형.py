def solution():
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N) ]
    arr.sort()
    max_height=0
    max_height_idx=0
    
    area=0
    
    for i in range(N):
        if max_height<arr[i][1]:
            max_height=arr[i][1]
            max_height_idx=i
        
    current_height=arr[0][1]
    for i in range(max_height_idx):
        width=arr[i+1][0] - arr[i][0]
        current_height=max(current_height,arr[i][1])
        area+= width * current_height

    current_height=arr[-1][1]
    for i in range(N-1,max_height_idx,-1):
        width=arr[i][0]-arr[i-1][0]
        current_height=max(current_height,arr[i][1])
        area+=width * current_height
    area+=max_height
    print(area)
solution()
        