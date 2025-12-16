from collections import deque
import sys

input = sys.stdin.readline

def solution():

    X, Y = map(int,input().split())
    lis = [list(map(int,input().split())) for i in range(Y)]

    que = deque([])
    cnt = 0 

    for i in range(Y):
        for j in range(X):
            if lis[i][j] == 1 :
                que.append((i,j)) #익은 토마토 전부 넣기


    while que:

        y,x = que.popleft()

        for plus_y,plus_x in [(0,1),(1,0),(-1,0),(0,-1)]:

            n_y = y + plus_y
            n_x = x + plus_x

            if 0 <= n_y < Y and 0 <= n_x < X :

                if lis[n_y][n_x] != -1  and lis[n_y][n_x] == 0:
                    que.append((n_y,n_x))
                    lis[n_y][n_x] = lis[y][x] + 1 

    for line in lis:
        if 0 in line:
            print(-1)
            return


    return print(max(map(max,lis))-1)

solution()

