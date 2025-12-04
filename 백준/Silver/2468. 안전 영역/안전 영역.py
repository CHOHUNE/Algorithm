import sys 
input = sys.stdin.readline
from collections import deque


def solution():

    O = int(input())

    lis = [ list(map(int,input().split())) for _ in range(O)]
    move = [(0,1), (1,0), (-1,0), (0,-1)]
    cnt = 0

    # for i in range(N):
    #     for j in range(N):
    #         if lis[i][j] <= N:
    #             visited[i][j] = True
                
    ans = []
    max_num =  max(max(row) for row in lis)
    for N in range(max_num):
        visited = [ [False]*O for i in range(O) ]
        cnt = 0 

        for i in range(O):
            for j in range(O):

                if lis[i][j] > N and visited[i][j] == False:
                    que = deque()                
                    visited[i][j] = True
                    cnt += 1
                    que.append((i,j))
                    
                    while que:
                        ox, oy =que.popleft()

                        for mx,my in move:

                            nx = ox+mx
                            ny = oy+my

                            if 0<= nx < O and 0 <= ny <O:
                                if lis[nx][ny] > N and visited[nx][ny] == False:
                                    visited[nx][ny] = True
                                    que.append((nx,ny))
        
        ans.append(cnt)

    # print(ans)
    print(max(ans))

solution()    



"""

아래는 잘못된 구조. dfs로 풀어야 하는데 브루트 포스로 돌려버림
얼추 보면 그럴싸해보이지만 덩어리를 인식하는데 매우 불편한 구조임. 
상하좌우만 이동하는데 끝남 -> 덩어리는 확장하면서 모두 인식해야함 


import sys 
input = sys.stdin.readline

def solution():

    N = int(input())


    lis = [ list(map(int,input().split())) for _ in range(N)]
    visited = [ [False]*N for i in range(N) ]
    move = [(0,1), (1,0), (-1,0), (0,-1)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if lis[i][j] <= N:
                visited[i][j] = True
                
    
    for i in range(N):
        for j in range(N):

            if lis[i][j] > N and visited[i][j] == False:
                
                visited[i][j] = True
                cnt += 1
                print(i,j,cnt)
                
                for x,y in move:
                    nx = i+x 
                    ny = j+y
                    if 0<= nx < N and 0 <= ny <N:

                        visited[nx][ny] = True

    print(cnt)

solution()    


"""