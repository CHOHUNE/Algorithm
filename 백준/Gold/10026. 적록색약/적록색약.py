import sys 
sys.setrecursionlimit(10000)
input = sys.stdin.readline



def solution():

    N   = int(input())
    lis = [list(input().strip()) for _ in range(N)]
    visited_GR = [ [False]*N for _ in range(N)]
    visited_norm = [ [False]*N for _ in range(N)]
    cnt_norm = 0
    cnt_GR = 0 

    def dfs(x,y):
        for plus_x,plus_y in  [(0,1),(1,0),(-1,0),(0,-1)]:
            if 0 <= x+plus_x < N and 0<= y + plus_y < N :
                if lis[x][y] == lis[x+plus_x][y+plus_y]:
                    if visited_norm[x+plus_x][y+plus_y] == False:
                        visited_norm[x+plus_x][y+plus_y] = True
                        dfs(x+plus_x,y+plus_y)


    def GR_dfs(x,y):
        for plus_x,plus_y in  [(0,1),(1,0),(-1,0),(0,-1)]:
            
            if 0 <= x+plus_x < N and 0<= y + plus_y < N :
                if visited_GR[x+plus_x][y+plus_y] == False:
                    if lis[x][y] == lis[x+plus_x][y+plus_y]:
                        visited_GR[x+plus_x][y+plus_y] = True
                        GR_dfs(x+plus_x,y+plus_y)
                        
                    elif lis[x][y] == "G" and lis[x+plus_x][y+plus_y] == "R":
                        visited_GR[x+plus_x][y+plus_y] = True
                        GR_dfs(x+plus_x,y+plus_y)
                        
                    elif lis[x][y] == "R" and lis[x+plus_x][y+plus_y] == "G":
                        visited_GR[x+plus_x][y+plus_y] = True
                        GR_dfs(x+plus_x,y+plus_y)
                    
    for i in range(N):
        for j in range(N):

            if not visited_GR[i][j]:
                cnt_GR += 1
                visited_GR[i][j] = True 
                GR_dfs(i,j)

            if not visited_norm[i][j]:
                cnt_norm +=1 
                visited_norm[i][j] = True
                dfs(i,j)
            
    print(cnt_norm,cnt_GR)

solution()