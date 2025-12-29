def solution():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    ans = 0

    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 1️⃣ DFS로 만들 수 있는 모든 테트로미노 (ㅗ 제외)
    def dfs(x, y, depth, total):
        if depth == 4:
            return total

        max_value = 0
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                max_value = max(
                    max_value,
                    dfs(nx, ny, depth + 1, total + board[nx][ny])
                )
                visited[nx][ny] = False
        return max_value

    # 2️⃣ ㅗ 계열 테트로미노 (중심 기준, 원점 포함)
    shapes = [
        [(0,0), (-1,0), (0,-1), (0,1)],  # ㅗ
        [(0,0), (1,0),  (0,-1), (0,1)],  # ㅜ
        [(0,0), (-1,0), (1,0),  (0,1)],  # ㅏ
        [(0,0), (-1,0), (1,0),  (0,-1)]  # ㅓ
    ]

    for i in range(N):
        for j in range(M):
            # DFS 시작점 전처리 (필수)
            visited[i][j] = True
            ans = max(ans, dfs(i, j, 1, board[i][j]))
            visited[i][j] = False

            # ㅗ 모양 처리
            for shape in shapes:
                temp = 0
                valid = True
                for dx_s, dy_s in shape:
                    nx, ny = i + dx_s, j + dy_s
                    if 0 <= nx < N and 0 <= ny < M:
                        temp += board[nx][ny]
                    else:
                        valid = False
                        break
                if valid:
                    ans = max(ans, temp)

    print(ans)


solution()
