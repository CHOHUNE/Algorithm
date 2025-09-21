from collections import Counter

# def binary_search(arr,target):
    
#     left = 0 
#     right = len(arr)-1

#     cnt = 0
    
#     while left <= right:
#         mid = (left+right) // 2
#         print(arr)
#         print(arr)

#         if arr[mid] < target:
#             left = mid +1

#         elif arr[mid] > target:
#             right = mid -1
#         elif arr[mid] == target:
#             return arr.get(mid)

#     return 0

def solution():

    N = int(input())
    lis_1 = list(map(int,input().split()))
    
    lis_1.sort()
    lis_1 = Counter(lis_1)

    M = int(input())
    lis_2 = list(map(int,input().split()))
    

    for i in lis_2:
        print(lis_1[i],end = ' ')

solution()
        
