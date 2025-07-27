from itertools import permutations 
def solution(k, dungeons):

    ans=0
    
    for perm in permutations(dungeons):
        temp=k
        cnt=0
        
        for need,use in perm:
            if temp >= need:
                temp-=use
                cnt+=1
        ans=max(ans,cnt)
                
    
    return ans