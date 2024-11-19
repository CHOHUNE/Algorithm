from collections import Counter

def solution(a, b, c, d):
    # 주사위 숫자를 리스트로 만들고 각 숫자의 등장 횟수를 셈
    dice = [a, b, c, d]
    counts = Counter(dice)
    
    # 1. 네 주사위가 모두 같은 경우
    if 4 in counts.values():
        return 1111 * a
    
    # 2. 세 주사위가 같은 경우
    elif 3 in counts.values():
        p = 0  # 3번 나온 수
        q = 0  # 1번 나온 수
        for num, count in counts.items():
            if count == 3:
                p = num
            if count == 1:
                q = num
        return (10 * p + q) ** 2
    
    # 3. 두 개씩 같은 경우 (2,2)
    elif list(counts.values()).count(2) == 2:
        p, q = [num for num, count in counts.items() if count == 2]
        return (p + q) * abs(p - q)
    
    # 4. 두 개가 같고 나머지가 다른 경우 (2,1,1)
    elif 2 in counts.values():
        q, r = 0, 0
        for num, count in counts.items():
            if count == 1:  # 1번만 나온 수들 저장
                if q == 0:
                    q = num
                else:
                    r = num
        return q * r
    
    # 5. 모두 다른 경우
    else:
        return min(dice)