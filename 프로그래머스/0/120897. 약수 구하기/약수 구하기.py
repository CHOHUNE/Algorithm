from math import sqrt

def solution(n):
    answer = []
    for i in range(1, int(sqrt(n)) + 1): 
        if n % i ==0:
            answer.append(i)
            if n // i !=i:
                answer.append(n//i)
            
    return sorted(answer)  

