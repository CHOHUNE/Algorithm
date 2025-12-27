import sys

input = sys.stdin.readline


def solution():

    N = int(input())
    lis = [ list(map(int,input().strip())) for _ in range(N)]
    ans = []
    visited= [[False] * N for _ in range(N)]

    def dfs(x,y):
        
        cnt = 0

        if visited[x][y] == False and lis[x][y] != 0:
            visited[x][y] = True
            cnt +=1
            
            for mx,my in [(0,1),(1,0),(-1,0),(0,-1)]:

                nx = x+ mx
                ny = y+ my

                if 0<= nx <N and 0<= ny < N:

                    if lis[nx][ny] == 1 and visited[nx][ny] == False:
                        cnt += dfs(nx,ny)
        
        return cnt 

    for i in range(N):
        for j in range(N):

            cnt = dfs(i,j)

            if cnt != 0:
                ans.append(cnt)


    print(len(ans))

    ans.sort()

    print(*ans,sep='\n')

solution()