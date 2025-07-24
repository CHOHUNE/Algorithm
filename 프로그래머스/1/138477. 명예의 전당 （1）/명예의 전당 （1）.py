import heapq

def solution(k, score):
    if not score:
        return []
        
    ans = []
    heap = []
    
    for i in range(len(score)):
        if i < k:
            heapq.heappush(heap, score[i])
        else:
            if score[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, score[i])
        ans.append(heap[0])
            
    return ans