import sys
from itertools import permutations
input = sys.stdin.readline


def solution():

    N =int(input())
    num = list(map(int,input().split()))
    spell_count = list(map(int,input().split()))
    max_result = float('-inf')
    minimum_result = float('inf')


    lis =[]

    def backtrack(idx, current_value):

        nonlocal max_result, minimum_result

        if idx == N:
            max_result  = max(max_result,current_value)
            minimum_result = min(minimum_result,current_value)
            return

        for i in range(4): #4가지 연산자 모두 시도

            if spell_count[i] > 0 : #spell이 있나 확인하기 위함 최적화

                spell_count[i] -= 1

                if i == 0:
                    new_value = current_value + num[idx]
                elif i == 1:
                    new_value = current_value - num[idx]
                elif i == 2:
                    new_value = current_value * num[idx]
                else :
                    new_value = int(current_value / num[idx]) 

                backtrack(idx+1,new_value)

                spell_count[i] += 1


    backtrack(1,num[0])


    print(max_result)
    print(minimum_result)

solution()