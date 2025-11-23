def solution():

    L,A = map(int,input().split())


    ans = {}
    for _ in range(L):

        x,y = map(str,input().split())
        ans[x] = y

    
    for _ in range(A):

        to_find_str = input()

        print(ans[to_find_str])    

solution()

