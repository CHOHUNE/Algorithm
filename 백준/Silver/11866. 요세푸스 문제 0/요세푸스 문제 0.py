from collections import deque

def solution():



    N , M =map(int,input().split())

    lis = deque()

    for i in range(1,N+1):
        lis.append(i)    
    ans = []
    for _ in range(N):

        for _ in range(M-1):
            i = lis.popleft()
            lis.append(i)

        ans.append(lis.popleft())


    print("<", end= '')
    print(*ans,sep=", ",end='')
    print(">",end='')

solution()