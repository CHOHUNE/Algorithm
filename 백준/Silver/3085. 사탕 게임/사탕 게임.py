import sys
input = lambda : sys.stdin.readline().strip()

def get_best():
    global N, matrix
    best = 0
    
    # 가로 방향 확인
    for i in range(N):
        bef = '-'
        value = 0
        for j in range(N):
            if bef == matrix[i][j]:
                value += 1
            else:
                value = 1
            bef = matrix[i][j]
            best = max(best, value)
    
    # 세로 방향 확인
    for i in range(N):
        bef = '-'
        value = 0
        for j in range(N):
            if bef == matrix[j][i]:
                value += 1
            else:
                value = 1
            bef = matrix[j][i]
            best = max(best, value)
    
    return best

def solution():
    global N, matrix
    
    N = int(input())
    matrix = [list(input()) for i in range(N)]
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ans = get_best()
    
    for x in range(N):
        for y in range(N):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if matrix[x][y] != matrix[nx][ny]:
                        matrix[x][y], matrix[nx][ny] = matrix[nx][ny], matrix[x][y]
                        ans = max(ans, get_best())
                        matrix[x][y], matrix[nx][ny] = matrix[nx][ny], matrix[x][y]
    
    print(ans)

solution()