def solution(n, words):
    answer = set()
    
    for i, word in enumerate(words):
                
        if word in answer:
            return [(i%n) +1,(i//n)+1]
        
        if words[i-1][-1] != word[0] and i > 0 :
            return [(i%n) +1,(i//n)+1]
        answer.add(word)
        



    return [0,0]