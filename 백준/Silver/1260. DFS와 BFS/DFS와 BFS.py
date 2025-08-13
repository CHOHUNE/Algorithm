from collections import deque

def solve_bfs(snode):
    global adj_list, visited  # adj_list로 이름 통일
    q = deque()
    q.append(snode)
    visited[snode] = True     # visited 사용
    
    while q:
        node = q.popleft()    # node 변수로 받기
        print(node, end=' ')  # 현재 node 출력
        
        for each_node in adj_list[node]:  # 현재 node의 인접노드들
            if visited[each_node]:
                continue
            q.append(each_node)
            visited[each_node] = True

def solve_dfs(node):
    global adj_list, visited  # adj_list로 이름 통일
    
    if visited[node]:         # visited 사용
        return
    visited[node] = True      # visited 사용
    print(node, end=' ')      # 출력 추가
    
    for each_node in adj_list[node]:
        solve_dfs(each_node)

def solution():
    global adj_list, visited  # adj_list로 이름 통일
    
    N, M, H = map(int, input().split())
    adj_list = [[] for i in range(N+1)]  # adj_list로 이름 통일
    
    for _ in range(M):        # range(M) - 0부터 M-1까지 (M개)
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    for i in range(1, N+1):
        adj_list[i].sort()
    
    visited = [False] * (N+1)
    solve_dfs(H)
    print()
    
    visited = [False] * (N+1)
    solve_bfs(H)
    print()

solution()