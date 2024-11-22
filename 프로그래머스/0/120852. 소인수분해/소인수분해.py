def solution(n):
    answer = []
    divisor=2
    while n>1 :
        if n%divisor==0 :
            n= n//divisor
            if divisor not in answer :
                answer.append(divisor)
        else :
            divisor+=1
        
    return answer