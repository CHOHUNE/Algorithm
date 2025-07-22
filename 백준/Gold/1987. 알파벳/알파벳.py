import sys
sys.setrecursionlimit(10000)

def solve():
    R, C = map(int, input().split())
    board = [input().strip() for _ in range(R)]
    
    memo = {}
    
    def dfs(r, c, visited):
        if (r, c, visited) in memo:
            return memo[(r, c, visited)]
        
        result = bin(visited).count('1')  # 현재까지의 길이
        
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                char_bit = 1 << (ord(board[nr][nc]) - ord('A'))
                if not (visited & char_bit):
                    result = max(result, dfs(nr, nc, visited | char_bit))
        
        memo[(r, c, visited)] = result
        return result
    
    first_bit = 1 << (ord(board[0][0]) - ord('A'))
    print(dfs(0, 0, first_bit))

solve()