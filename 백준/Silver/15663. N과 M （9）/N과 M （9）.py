import sys
sys.setrecursivelimit = 10 * 7 

def solution():
    
    N, M = map(int,input().split())
    lis = sorted(list(map(int,input().split())))
    
    visited = [False] * N
    ans = [] 
    
    def dfs():
        if len(ans) == M :
            print(*ans, sep = ' ')
            return

        pre_val = 0 

        for i in range(N):

            cur_val = lis[i]
            if visited[i] == False and cur_val != pre_val:
                ans.append(lis[i])
                visited[i] = True
                dfs()
                visited[i] = False
                ans.pop()
                
                pre_val = cur_val
    dfs()
solution()

                
            
        
    
    