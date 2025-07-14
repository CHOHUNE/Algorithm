import heapq

def solution(A,B):
    
    heap_a = A.copy()
    heap_b = [-x for x in B]
    

    heapq.heapify(heap_a)
    heapq.heapify(heap_b)
    
    result = 0
    while heap_a:
        min_a = heapq.heappop(heap_a)
        max_b= -heapq.heappop(heap_b)
        result += min_a * max_b

    return result