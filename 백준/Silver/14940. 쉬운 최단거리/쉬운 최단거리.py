from collections import deque
import sys
input = sys.stdin.readline

def solution():

    N , M = map(int,input().split())

    origin_lis = [ list(map(int,input().split())) for _ in range(N)]
    ans  = [ [-1 for _ in range(M)] for _ in range(N)] # 가로가 x -> N 임 

    temp = deque()
    # visited 가 None일 경우 -1 
    
    found = False
    for i in range(N):
        if found:
            break
        for j in range(M):
            if origin_lis[i][j] == 2 :
                ans[i][j] = 0
                temp.append((i,j))
                found= True
                break
        

    while temp:

        start_x, start_y = temp.popleft()

        for nx, ny in [(1,0),(0,1),(-1,0),(0,-1)]:
                
            fx = start_x+nx
            fy = start_y+ny

            if 0 <= fx < N and 0 <= fy < M:
                if origin_lis[fx][fy] == 1 and ans[fx][fy] == -1:
                    ans[fx][fy] = ans[start_x][start_y] +1
                    temp.append((fx,fy))

    for i in range(N):
        for j in range(M):
            if origin_lis[i][j]  == 0:
                print(0, end = ' ')
            else:
                print(ans[i][j] , end = ' ')
        print()


        

solution()