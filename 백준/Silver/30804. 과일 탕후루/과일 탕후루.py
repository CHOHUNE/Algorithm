import sys
from collections import defaultdict 

def solution():

    N = int(input())
    lis = list(map(int,input().split()))
    left = 0 
    ddict = defaultdict(int)
    ans = 0 


    for right in range(N):

        ddict[lis[right]] += 1 

        while len(ddict) > 2:

            ddict[lis[left]] -= 1

            if ddict[lis[left]]  == 0:
                del ddict[lis[left]]

            left += 1

        ans = max(ans, right-left+1)

    print(ans)

solution()