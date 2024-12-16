def sol():
    N,M = map(int,input().split())
    
    board=[]
    for i in range(N):
        board.append(input())
        
    min_count=64
    
    for a in range(N-7):
        for b in range(M-7):
            
            count1=0 # 짝수인덱스
            count2=0 # 홀수인덱스 
            
            for x in range( a,a+8):
                for y in range(b,b+8):
                    if (x+y)% 2 == 0:#짝수 인덱스,짝수열 
                        if board[x][y] != 'W': # B로 시작한다고 상정 
                            count1+=1
                        if board[x][y] != 'B':
                            count2+=1
                    else: #홀수 인덱스 상정 
                        if board[x][y]!= 'B': #A로 시작한다고 상정 
                            count1 += 1
                        if board[x][y] !='W':
                            count2+=1
            min_count=min(min_count,count1,count2)
    print(min_count)
sol()
                       
            