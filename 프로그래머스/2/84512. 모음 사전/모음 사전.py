from itertools import product
def solution(word):
    answer = 0
    ans =[]
    aeiou =["A","E","I","O","U"]
    
    for i in range(1,6):
        for j in product(aeiou,repeat=i):
            ans.append(''.join(j))
            
    ans.sort()
    return ans.index(word)+1