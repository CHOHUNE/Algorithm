def solution(citations):
    answer = 0
    # 0부터 논문 수까지 모든 h 값 체크
    for h in range(len(citations) + 1):
        cnt = 0
        for num in citations:
            if num >= h:
                cnt += 1
        
        # h번 이상 인용된 논문이 h편 이상이면
        if cnt >= h:  # 핵심: >= 사용!
            answer = max(answer, h)  # 최댓값 갱신
    
    return answer