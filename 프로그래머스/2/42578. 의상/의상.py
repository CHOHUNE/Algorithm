def solution(clothes):
    
    cate = {}
    answer = 0
    
    for item, category in clothes:
        if category not in cate:
            cate[category] = [item]
        else:
            cate[category] += [item]
    answer = 1
    for category, item in cate.items():
        answer *= (len(item)+1)
        
    return answer-1