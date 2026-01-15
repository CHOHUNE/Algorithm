import sys
input = sys.stdin.readline

N = int(input())
lis = list(input().split())

def backtrack(N):

    result = []
    temp = []
    visited = [0] * 10 

    def combinations(N):

        if len(temp) == N+1:
            for i in range(N):
                if lis[i] == '<':
                    if not temp[i] < temp[i+1]:
                        return
                if lis[i] == '>':
                    if not temp[i] > temp[i+1]:
                        return


            result.append(temp[:])
            return

        for i in range(10):

            if visited[i] == 0:
                visited[i] = 1
                temp.append(i)
                combinations(N)
                temp.pop()
                visited[i] = 0

    combinations(N)
    print(''.join(map(str,result[-1])))
    print(''.join(map(str,result[0])))

backtrack(N)