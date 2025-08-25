from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_number = {}
    
    for i, item in enumerate(want) :
        want_number[item] = number[i]
        
    for i in range(len(discount)-9):
        temp_want_number = Counter(discount[i:i+10])
        
        if want_number==temp_want_number:
            answer += 1 
            
    return answer