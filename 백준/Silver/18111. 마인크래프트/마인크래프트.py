import sys 

input = sys.stdin.readline
def solution():


    N, M ,I = map(int,input().split())
    lis = [ list(map(int,input().split())) for _ in range(N)]

    max_num = max(map(max,lis))
    min_num = min(map(min,lis))
    ans = [float('INF'),0]

    for i in range(min_num, max_num+1):

        total_time = 0
        Inventory = I

        for each_line in lis:
            for each_value in each_line:

                if each_value > i :
                     
                    gap     = each_value - i
                    Inventory += each_value - i
                    total_time += gap * 2 
                
                if each_value < i :
                     
                    gap         = i - each_value
                    Inventory   -= i - each_value
                    total_time  += gap 

        if Inventory >= 0 :
            if total_time < ans[0]:
                ans[0] = total_time
                ans[1] = i
                
            if total_time == ans[0] and i > ans[1]:
                ans[0] = total_time
                ans[1] = i

    print(*ans, sep = ' ')

solution()