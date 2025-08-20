# 이것도 정답
def solution(n):
    if n <= 2:
        return n
    
    prev2, prev1 = 1, 2
    
    for i in range(3, n + 1):
        current = (prev1 + prev2) % 1234567
        prev2, prev1 = prev1, current
    
    return current  # 이것도 같은 결과