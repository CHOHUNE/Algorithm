def solution():
    
    N,M = map(int,input().split())
    num = [0] + list(map(int,input().split()))
    total = [0] * len(num)
    ans =0
    for i in range(len(num)):
        total[i] = total[i-1] + num[i]
        
    for left in range(1,len(num)):
        for right in range(left,len(num)):
            if total[right] - total[left-1] == M:
                ans+=1
                
    print(ans)
solution()
            