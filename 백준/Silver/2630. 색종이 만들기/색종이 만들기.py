import sys
input = sys.stdin.readline

def solve(x,y,size,paper):

    color = paper[x][y]
    same = True
    
    for i in range(x,x+size):
        for j in range(y,y+size):
            if paper[i][j] !=  color:
                same = False
                break
        if not same:
            break

    if same:
        if color == 0:
            return (1,0)
        else:
            return (0,1)
    else:
        half = size // 2 
        result = [0,0]
        for w,b in [solve(x,y,half,paper),
                    solve(x+half,y,half,paper),
                    solve(x,y+half,half,paper),
                    solve(x+half,y+half,half,paper)]:
            
            result[0] += w 
            result[1] += b 
            
    return tuple(result)


def solution():

    N = int(input())
    paper  = [list(map(int,input().split())) for _ in range(N)]

    result = solve(0,0,N,paper)

    print(*result,sep="\n")
    


solution()