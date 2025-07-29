def solution():
    
    N,M = map(int,input().split())
    num = list(map(int,input().split()))
    ans =0
    left =0
    right = -1
    cur_sum=0
    
    for left in range (N):
        while (right+1 < N) and (cur_sum + num[right+1] <= M):
            right+=1
            cur_sum += num[right]
            if(cur_sum == M):
                ans +=1
        cur_sum-=num[left]
                
    print(ans)
solution()
            