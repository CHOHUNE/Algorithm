def solution(answers):
    patterns=[[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    score = [0,0,0]
    
    for i in range(len(answers)):
        answer=answers[i]
        for j in range(len(patterns)):
            pattern = patterns[j]
            
            if answer == pattern[i%len(pattern)]:
                score[j]+=1
    result=[]
    max_score = max(score)
    
    for i in range(len(score)):
        if max_score == score[i]:
            result.append(i+1)
            
    return result
    
