import sys
input =sys.stdin.readline


def solution():


    N, M = map(int,input().split())
    lis = [ int(input()) for _ in range(N)]

    row = 1
    high = max(lis)
    ans = 0
    
    while row <= high:

        mid = (row+high) // 2 

        if can_cut(lis,M,mid):
            
            ans = mid 
            row = mid + 1
        else : 
            high = mid -1 
    print(ans)

def can_cut(lis,M,mid):

    total = 0
    for each in lis:
        if each >= mid:
            total += each // mid
    
    return total >= M
        
solution()



# parametic search에서 row는 0이면 안된다? -> 정리 필요함 
