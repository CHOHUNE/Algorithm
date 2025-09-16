def solution():
    N = input()
    
    nums=[]
    
    for i in range(len(N)):
        nums.append(N[i])
    nums.sort(reverse=True)
    
    ans=""
    
    for i in range(len(N)):
        ans+=nums[i]
    print(ans)
    
    
    
solution()
    