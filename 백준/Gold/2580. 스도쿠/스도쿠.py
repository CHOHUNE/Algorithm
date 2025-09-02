def is_possible(y,x,n):
    global pos, matrix
    
    for i in range(9):
        if(matrix[i][x] == n):
            return False
        
    for i in range(9):
        if(matrix[y][i] == n):
            return False
        
    for i in range(3):
        for j in range(3):
            if matrix[3*(y//3)+i][3*(x//3)+j] == n:
                return False
            
    return True
   
def search(lev):
    global pos, matrix
    
    #base_case
    if lev == len(pos):
        for i in range(9):
            for j in range(9):
                print(matrix[i][j], end = ' ')
            print()
        exit(0)
        return
    
    #recursive_case
    y,x =pos[lev]
    for i in range(1,10):
        if is_possible(y,x,i):
            matrix[y][x] = i
            search(lev+1)
            matrix[y][x] = 0
    
matrix = [list(map(int,input().split())) for _ in range(9)]
pos = []

for i in range(9):
    for j in range(9):
        if matrix[i][j] == 0:
            pos.append((i,j))

search(0)
        