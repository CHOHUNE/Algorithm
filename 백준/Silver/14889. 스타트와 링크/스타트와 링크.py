import sys
input = sys.stdin.readline

N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]

people = list(range(N))
result = float('inf')

def combinations():
    result = []
    temp = []

    def backtrack(start):
        if len(temp) == N // 2:
            result.append(temp.copy())
            return
        for i in range(start, N):
            temp.append(i)
            backtrack(i + 1)
            temp.pop()

    backtrack(0)
    return result

teams = combinations()

for start_team in teams:
    link_team = [x for x in people if x not in start_team]

    start_score = 0
    link_score = 0

    # 스타트 팀 능력치
    for i in range(len(start_team)):
        for j in range(i + 1, len(start_team)):
            a = start_team[i]
            b = start_team[j]
            start_score += status[a][b] + status[b][a]

    # 링크 팀 능력치
    for i in range(len(link_team)):
        for j in range(i + 1, len(link_team)):
            a = link_team[i]
            b = link_team[j]
            link_score += status[a][b] + status[b][a]

    result = min(result, abs(start_score - link_score))

print(result)
