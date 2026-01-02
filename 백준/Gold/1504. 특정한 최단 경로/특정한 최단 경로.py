import sys
import heapq

input = sys.stdin.readline

def daji(start,graph,N):

    heap = []
    dist = [float('INF')] * (N+1)
    dist[start] = 0
    heapq.heappush(heap,(0,start))
    #최단 거리를 구해야함 
    #start 부터 시작해서 N 까지의 거리

    while heap:

        cur_dist, cur_node = heapq.heappop(heap)

        if cur_dist > dist[cur_node]:
            #배열에 저장된 거리보다 더 길면 pass
            continue

        for  next_node, this_weight in graph[cur_node]:
            next_dist = cur_dist + this_weight

            if dist[next_node] > next_dist:
                dist[next_node] = next_dist

                heapq.heappush(heap,(next_dist,next_node))
    
    return dist



def solution():

    node, line = map(int,input().split())

    graph = [[] for _ in range(node+1)]

    for _ in range(line):

        start,end,weight = map(int,input().split())

        graph[start].append((end,weight))
        graph[end].append((start,weight))

    v1, v2 = map(int,input().split())

    
    road_1 = daji(1,graph,node)
    road_v1 = daji(v1,graph,node)
    road_v2 = daji(v2,graph,node)

    ans_candidate_1 = road_1[v1] + road_v1[v2] + road_v2[node]
    ans_candidate_2 = road_1[v2] + road_v2[v1] + road_v1[node]

    ans = min(ans_candidate_1,ans_candidate_2)
    
    if ans >= float('INF'):
        print(-1)
    else:
        print(ans)

solution()

