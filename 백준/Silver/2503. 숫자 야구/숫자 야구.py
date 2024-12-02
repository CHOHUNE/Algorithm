def solution():
    num = int(input())
    
    numbers = [list(map(str,input().split())) for _ in range(num)]
    answer = 0 #만족하는 정답의 갯수 
    
    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                cnt = 0 
                
                if a==b or a==c or b==c : continue
                
                for array in numbers :
                    check = list(array[0])
                    strike= int(array[1])
                    ball = int(array[2])
                    
                    strike_count=0
                    ball_count=0

                    if a == int(check[0]): strike_count +=1
                    if b == int(check[1]): strike_count +=1 
                    if c == int(check[2]): strike_count +=1 

                    if a == int(check[1]) or a== int(check[2]): ball_count+=1
                    if b == int(check[0]) or b== int(check[2]): ball_count+=1
                    if c == int(check[0]) or c== int(check[1]): ball_count+=1                        

                    if ball_count != ball or strike != strike_count : break

                    cnt+=1
                if cnt == num : answer+=1 
    print(answer)
solution()
                    
                