import sys

input = sys.stdin.readline

def combi(arr, m):

    result = []

    def backtrack(start,selected):

        if len(selected) == m:
            result.append(selected[:])
            return 

        for i in range(start,len(arr)):
            selected.append(arr[i])
            backtrack(i+1,selected)
            selected.pop()

    backtrack(0,[])
    return result


def solution():

    N, M = map(int,input().split())
    lis = [list(map(int,input().split())) for _ in range(N)]

    house = []
    chicken = []
    answer = float('INF')

    for x in range(N):
        for y in range(N):

            if lis[x][y] == 1:
                house.append((x,y))
            if lis[x][y] == 2:
                chicken.append((x,y))


    for selected in combi(chicken,M):
        current_dist =0

        for h_x, h_y in house :
            min_dist = float('inf')

            for c_x, c_y in selected :
                min_dist = min(min_dist,(abs(h_x-c_x)+abs(h_y-c_y)))
            current_dist += min_dist

        answer = min(answer,current_dist)

    print(answer)

solution()