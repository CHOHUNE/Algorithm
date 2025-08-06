from collections import *
def solution(k, tangerine):
    
    
    count =Counter(tangerine)
    result = 0 
    for size, cnt in count.most_common():
        k -= cnt
        result+=1
        if k <=0:
            break
    return result