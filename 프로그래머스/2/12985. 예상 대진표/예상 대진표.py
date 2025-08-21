def solution(n,a,b):
    cnt = 0

    for i in range (n//2):
        a += a%2
        b += b%2
        
        cnt +=1 
        
        a //=2
        b //=2
        
        if a==b :
            return cnt
        

    return cnt