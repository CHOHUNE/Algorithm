import sys

input = lambda : sys.stdin.readline().rstrip()

def get_idx(arr,n):
    step = len(arr)
    cur = -1 
    while step != 0:
        while step + cur < len(arr) and arr[cur+step] <= n:
            cur+= step
        step //= 2
    return cur

def solution():
    N,M = map(int,input().split())
    bot =[]
    top =[]

    minimum=int(1e12)
    howmany=0

    for i in range(N):
        num=int(input())
        if i % 2 ==0:
            bot.append(num)
        else:
            top.append(M-num+1)

    bot = sorted(bot)
    top = sorted(top)        
    for i in range(1,M+1):
        cnt_bot = N//2 - (get_idx(bot,i-1)+1)
        cnt_top = get_idx(top,i)+1
        if cnt_bot+cnt_top == minimum:
        	howmany+=1
        if minimum > cnt_bot+cnt_top:
        	minimum = cnt_bot+cnt_top
	       	howmany = 1
    print(minimum,howmany)
    
solution()
