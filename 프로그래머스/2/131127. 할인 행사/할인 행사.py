def solution(want, number, discount):
    answer = 0
    want_number = {}
    
    for i, item in enumerate(want):
        want_number[item] = number[i]
        
    for i in range(len(discount) - 9):  # 범위 수정
        temp_map = want_number.copy()   # 복사본 사용
        
        for j in range(i, i + 10):      # 10일치만
            if discount[j] in temp_map:  # 키 체크
                if temp_map[discount[j]] > 0:
                    temp_map[discount[j]] -= 1
                
        if sum(temp_map.values()) == 0:
            answer += 1
            
    return answer