def solution(chicken):
    
    ans=0
    while chicken/10 >= 0.1 :
            ans+=chicken/10
            chicken= chicken/10
    else : return int(ans)
    
    
    