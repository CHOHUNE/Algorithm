import sys
sys.setrecursionlimit(10*7)

def solution(N,start,end,aux):


    if N == 1 :
        print(start,end , sep = ' ')
        return

    solution(N-1,start,aux,end)
    print(start,end)
    solution(N-1,aux,end,start)





N = int(input())
print(2**N-1)
solution(N,1,3,2)