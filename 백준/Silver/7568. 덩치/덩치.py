

def solution() :

    N = int(input())
    
    
    lis = []     
    for i in range(N):
        x,y = map(int,input().split())
        lis.append([x,y])
    
    for i in range(N):
        rank = 1 
        for j in range(N):
            if lis[i][0] < lis[j][0] and lis[i][1] < lis[j][1]:
                rank+=1
        
        print(rank, end =' ')


solution()
                
