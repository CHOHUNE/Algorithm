from collections import deque
import sys

input = sys.stdin.readline

def solution():


    row, ver, height = map(int,input().split())
    lis = [ [list(map(int,input().split())) for _ in range(ver)] for _ in range(height)]

    que = deque([])
    ans = 0 

    for x in range(height):
        for y in range(ver):
            for z in range(row):
                
                if lis[x][y][z] == 1 :
                    que.append((x,y,z))
    
    rotate_x = [0,0,0,0,1,-1]
    rotate_y = [0,0,1,-1,0,0]
    rotate_z = [1,-1,0,0,0,0]

    while que:
        
        cur_x,cur_y,cur_z = que.popleft()

        for num in range(6):

            new_x = cur_x + rotate_x[num]
            new_y = cur_y + rotate_y[num]
            new_z = cur_z + rotate_z[num]

            if 0 <= new_x < height and 0<= new_y < ver and 0<= new_z < row:

                if lis[new_x][new_y][new_z] == 0:
                    
                    que.append((new_x,new_y,new_z))
                    lis[new_x][new_y][new_z] = lis[cur_x][cur_y][cur_z] + 1


    for x in range(height):
        for y in range(ver):
            for z in range(row):

                if lis[x][y][z] == 0:
                    print(-1)
                    return
                
            ans = max(ans,max(lis[x][y]))
    
    print(ans-1)

solution()