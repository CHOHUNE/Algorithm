import sys
input = sys.stdin.readline

from itertools import permutations

def solution():
    N =int(input())
    num = list(map(int,input().split()))
    spell_count = list(map(int,input().split()))

    lis =[]
    for i,value in enumerate(spell_count):
        if i ==0:
            lis += ['+'] *value
        elif i ==1:
            lis += ['-']*value
        elif i ==2:
            lis += ['*']*value
        elif i ==3:
            lis += ['//']*value

    max_result = float('-inf')
    minimum_result = float('inf')

    for per in permutations(lis):

        result = num[0] # 두 번째 항 부터 기호가 들어가서 1번째 항을 자연스럽게 result에다가

        for i in range(len(per)): #마지막 안들어가서 index error 없음 

            if per[i] =='+':
                result += num[i+1]
            elif per[i] =='-':
                result -= num[i+1]
            elif per[i] == '*':
                result *= num[i+1]
            elif per[i] == '//':
                result = int(result/num[i+1])

        max_result = max(result,max_result)
        minimum_result = min(minimum_result,result)

    print(max_result)
    print(minimum_result)

solution()