import sys 
from collections import deque

def solution():
    X,Y = map(int,input().split())
    
    graph = [ list(input().strip()) for _ in range(X)]
    
    doyeon =  next((x,y)
                   for x in range(X)
                   for y in range(Y)
                   if graph[x][y] =="I")
    
    dfs = deque()
    dfs.append(doyeon)

    visited = [ [False]*Y for _ in range(X)]
    
    ans = 0

    while dfs:
        ex_x, ex_y = dfs.popleft()

        for nx,ny in [(1,0),(-1,0),(0,1),(0,-1)]:

            fx = ex_x + nx
            fy = ex_y + ny

            if 0<= fx and fx < X and 0 <= fy and fy < Y:

                if graph[fx][fy] == "P" and visited[fx][fy] == False:
                    ans +=1
                    visited[fx][fy] = True
                    dfs.append((fx,fy))
                    
                elif graph[fx][fy] =="O" and visited[fx][fy] == False:
                    visited[fx][fy] = True
                    dfs.append((fx,fy))
                
    if ans == 0:
        print("TT")
    else:
        print(ans)

solution()



"""
next 함수 사용법 next =  ( 반환할 값 , 외 조건 for for if)

dfs에 append 하는 부분이 매우 중요하다.
popleft 하자마자 ex_x 와 ex_y 즉 전 위치에 방문처리를 했는데 이렇게 하면 이동하게 될 위치를
visited 전부 처리하지 못해 무한 루프에 빠지게 된다. 

상하 좌우로 움직일 때 해당 좌표의 위치 검사를 하고, 조건 검사를 하고, 다음 dfs 배열에 append 하기 전에 visited 처리를 해야 
중복으로 오가는 일이 없다..! 


"""