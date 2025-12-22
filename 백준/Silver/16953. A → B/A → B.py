import sys
from collections import deque
input = sys.stdin.readline


def solution():

    start, end = map(int,input().split())

    que = deque([(start,1)])

    ans = -1 

    def dfs(cur):
        nonlocal ans
        #함수 외부에 있는 변수를 변경하려면 nonlocal을 써야한다.
        #nonlocal 선언 없이 그냥 ans를 쓸 경우 또다른 지역 변수를 만들 뿐이다. 이점 주의 
        value, idx = cur

        if value == end:
            if ans == -1 or idx < ans:
                ans = idx
            return

        elif value > end :
            return 

        else:
            dfs((value*2,idx+1))
            dfs((int(str(value)+'1'),idx+1))


    dfs((start,1))
    print(ans)
    

solution()