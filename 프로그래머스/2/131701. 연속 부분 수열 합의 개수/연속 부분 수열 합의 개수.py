def solution(elements):
    
    extended = elements * 2 
    sums = set()
    
    for start in range(len(elements)):
        for length in range(1,len(elements)+1):
            sub_seq_sum = sum(extended[start: start+length])
            sums.add(sub_seq_sum)
        
    return len(sums)
            