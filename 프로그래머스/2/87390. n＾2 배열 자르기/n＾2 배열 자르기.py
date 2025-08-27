def solution(n, left, right):
    answer = []
    
    for idx in range(left,right+1):
        i = idx // n +1
        j = idx % n +1
        answer.append(max(i,j))
    
    return answer