import sys

input = sys.stdin.readline 

def solution():

    N = int(input())
    nums = []

    for i in range(N):
        temp = input().split()

        if temp[0] == 'push':
            nums.append(temp[1])
        elif temp[0] == 'top':
            if nums ==[]:
                print(-1)
            else:
                print(nums[-1])
        elif temp[0] == 'size':
            print(len(nums))
        elif temp[0] == 'empty':
            if nums ==[]:
                print(1)
            else:
                print(0)
        elif temp[0] == 'pop':
            if nums == []:
                print(-1)
            else:
                print(nums.pop())


            



solution()