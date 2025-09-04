def solution(elements):
    
    twice = elements + elements
    anset=set()
    
    for i in range(len(elements)):
        for j in range(1,len(elements)+1):
            
            anset.add(sum(twice[i:i+j]))
            
        
    return len(anset)