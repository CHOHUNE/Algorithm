def solution():
    
    N,M = map(int,input().split())
    lis = [True] * (M+1)
    lis[0]=lis[1]=False
    
    for i in range(2,M+1):
        if lis[i]:
            for j in range(i*i,M+1,i):
                lis[j] = False
    for i in range(N,M+1):
        if lis[i]:
            print(i)

solution()