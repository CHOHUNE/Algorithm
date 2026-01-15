import sys
input = sys.stdin.readline

N = int(input())
lis = list(input().split())

def backtrack(N):

    result = []
    temp = []
    visited = [0] * 10 

    def combinations(N,NM):

        if len(result) >= 1:
            return

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
        if NM == 'MIN':
            for i in range(10):

                if visited[i] == 0:
                    visited[i] = 1
                    temp.append(i)
                    combinations(N,'MIN')
                    temp.pop()
                    visited[i] = 0
        if NM =='MAX':
            for i in range(9,-1,-1):

                if visited[i] == 0:
                    visited[i] = 1
                    temp.append(i)
                    combinations(N,'MAX')
                    temp.pop()
                    visited[i] = 0


    
    combinations(N,'MAX')
    print(''.join(map(str,result[0])))

    result=[]
    combinations(N,'MIN')
    print(''.join(map(str,result[0])))

backtrack(N)