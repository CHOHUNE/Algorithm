N , M = map(int, input().split())
l = []

def dfs(start):
    
    if len(l) == M:
        print(*l , sep = ' ')
        return
    
    for i in range(start,N+1):
        l.append(i)
        dfs(i)
        l.pop()
        

dfs(1)
