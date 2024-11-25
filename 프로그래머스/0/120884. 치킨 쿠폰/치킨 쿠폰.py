def solution(chicken):
    ans=0
    while chicken >= 10 :
        ans+= chicken//10 
        chicken = chicken//10 + chicken%10
    else : return ans 
    
    
    