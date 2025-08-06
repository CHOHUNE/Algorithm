def solution(k, tangerine):
    
    count = {}
    
    for size in tangerine:
        count[size] = count.get(size,0)+1
        
    sorted_count= sorted(count.values(), reverse = True)

    result = 0
    for cnt in sorted_count:
        k -= cnt
        result +=1
        if k <= 0:
            break
    return result