def solution():


    N = int(input())
    lis = [ list(map(int,input().split())) for _ in range(N)]

    lis.sort( key= lambda x :( x[1],x[0]) )
    cnt = 1 
    before = lis[0][1]
    for i in range(1,N):
        
        if lis[i][0] >= before:
            cnt += 1 
            before = lis[i][1]

    print(cnt)

solution()

    
    