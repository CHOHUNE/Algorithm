import sys

input = sys.stdin.readline

def solution():
    
    N = int(input())
    lis = list(map(int,input().split()))

    dict_ans = {}
    sorted_set = sorted(set(lis))
               
    for idx,value in enumerate(sorted_set):
        dict_ans[value] = idx
    
    for each in lis:
        print(dict_ans[each],end = ' ')
               
solution()

# 문제 포인트는 list.index() 를 활용할 때 마다 ON이 가중되어 시간초과가 난다는 점이다.
# list.index() 를 활용해 찾거나, 다시 넣게되면 안되고 dict와 원본 list를 활용해 O1 만에 풀어야한다.