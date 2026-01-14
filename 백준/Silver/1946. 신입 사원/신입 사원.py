import sys

input = sys.stdin.readline

def solution():

    N = int(input())
    for i in range(N):

        IN = int(input())

        lis = []
        for i in range(IN):
            x,y = map(int,input().split())
            lis.append((x,y))

        lis.sort()
        cur_best = lis[0][1]
        cnt = 1

        for i in range(1,len(lis)):
            if cur_best > lis[i][1] :
                cur_best = lis[i][1]
                cnt+=1
        print(cnt)
solution()
