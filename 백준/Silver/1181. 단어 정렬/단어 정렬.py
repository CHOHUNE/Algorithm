def solution():
    
    N = int(input())
    lis = [input() for _ in range(N)]
    lis.sort(key = lambda x : (len(x),x))
    
    ans = [] 
    for each in lis:
        if each not in ans:
            ans.append(each)
            
    print(*ans,sep = '\n')
solution()