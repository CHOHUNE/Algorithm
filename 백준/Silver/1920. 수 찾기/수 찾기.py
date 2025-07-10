import sys
input = lambda : sys.stdin.readline().rstrip()

def get_idx(arr, n):
    cur = -1
    step= len(arr)
    
    while step != 0:
        while cur + step < len(arr) and arr[cur+step] <= n:
            cur += step
        step //= 2
    return cur

def solution():
    N = int(input())
    num_list_1 = sorted(list(map(int,input().split())))
    M = int(input())
    num_list_2 = list(map(int,input().split()))
    
    for i in num_list_2:
        idx = get_idx(num_list_1,i)
        if idx >= 0 and i == num_list_1[idx]:
            print(1)
        else:
            print(0)

solution()
    
    
   