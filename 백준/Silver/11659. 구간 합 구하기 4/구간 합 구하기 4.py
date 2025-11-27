    
    



def solution():
    N , M = map(int,input().split())

    lis =  list(map(int,input().split()))
    part_sum =  [ list(map(int,input().split())) for _ in range(M)]

    all_sum = []
    all_sum.append(0)
    all_sum.append(lis[0])

    for i in range(1,N):
        all_sum.append(all_sum[i]+lis[i])
    
    for x,y in part_sum:
        print(all_sum[y]-all_sum[x-1])
    

    


solution()
