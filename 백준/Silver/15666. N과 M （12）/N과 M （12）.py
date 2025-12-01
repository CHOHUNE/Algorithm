import sys

sys.setrecursionlimit = 10* 7 


def solution():

    N, M = map(int,input().split())
    nums = sorted(list(map(int,input().split())))

    ans = []

    def dfs(start):

        if len(ans) == M :
            print(*ans, sep = ' ')
            return
        

        pre_value = -1 

        for i in range(start,N):
            
            if pre_value == nums[i]:
                continue
            
            ans.append(nums[i])
            dfs(i)
            ans.pop()
            pre_value = nums[i]

    dfs(0)

solution()