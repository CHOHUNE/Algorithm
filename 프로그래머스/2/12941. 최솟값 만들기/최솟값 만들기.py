import heapq

def solution(A,B):
    
    arr_A= A.copy()
    arr_B= [ -x for x in B]
    
    heapq.heapify(arr_A)
    heapq.heapify(arr_B)

    result =0
    while arr_A:
        min_a=heapq.heappop(arr_A)
        max_b=-heapq.heappop(arr_B)
        result += min_a * max_b
        
        

    return result