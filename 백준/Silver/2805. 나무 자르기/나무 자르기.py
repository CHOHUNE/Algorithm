def is_possible(k):
    
    ans = 0 
    for num in num_list:
        if num > k:
            ans += num-k
    return (ans>=M)


def solution():
    global num_list, M
    N,M = map(int,input().split())
    num_list=list(map(int,input().split()))
    
    cur = -1 
    step= int(1e9)+1
    
    while step != 0:
        while (cur+step) < int(1e9) and is_possible(cur+step):
            cur+=step
        step //=2
    print(cur)
    
solution()