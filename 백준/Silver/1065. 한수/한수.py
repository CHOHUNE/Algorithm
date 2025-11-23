def solution():

    N = int(input())
    cnt = 0
    
    lis = [ list(map(int,str(i))) for i in range(1,N+1)]
    
    for i in lis:
        if len(i) <= 2:
            cnt+=1
        elif len(i) == 3:
            x,y,z = i
            if x-y == y-z:
                    cnt+=1

    print(cnt)

solution()