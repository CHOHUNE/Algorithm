import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def solution():
    
    N, M = map(int,input().split())
    lis = [ list(map(int,input().split())) for _ in range(N)]

    zero_lis = []
    start_lis= []
    for i in range(N):
        for j in range(M):

            if lis[i][j] == 0:
                zero_lis.append((i,j))
            if lis[i][j] == 2:
                start_lis.append((i,j))

    cnt_zero = len(zero_lis)
    ans = 0
    

    for combi in combinations(zero_lis,3):

        inner_lis = [ row[:] for row in lis ] #깊은 복사
        #inner_lis = lis[:] 이와 같이 얉은 복사를 할 경우 원본 lis에도 영향을 미침
        inner_ans = 0

        que = deque(start_lis[:])

        for each in combi:

            inner_lis[each[0]][each[1]] = 1

        while que:

            each_que = que.popleft()
            
            for move in [(0,1),(1,0),(-1,0),(0,-1)]:

                nx = each_que[0]+move[0]
                ny = each_que[1]+move[1]

                if 0<= nx < N and 0<= ny <M:
                    if inner_lis[nx][ny] == 0:

                        inner_ans += 1
                        inner_lis[nx][ny] = 2
                        que.append((nx,ny))

        ans = max(cnt_zero-inner_ans -3, ans)

    print(ans)

solution()