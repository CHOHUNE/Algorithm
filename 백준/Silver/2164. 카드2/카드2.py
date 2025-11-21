from collections import deque

def solution():
    
    N = int(input())
    
    lis = deque()
    for i in range(1,N+1):
        lis.append(i)
        
    for i in range(N):
        if len(lis) == 1 :
            break
        lis.popleft()
        i = lis.popleft()
        lis.append(i)
        
    print(*lis)
solution()
    