l = []
N ,M = list(map(int,input().split()))
values = sorted(list(map(int,input().split())))
visited = [False] * N


def dfs():
    
    if len(l) == M :
        print(*l, sep = ' ')
        
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            l.append(values[i])
            dfs()
            l.pop()
            visited[i]=False
            
dfs()