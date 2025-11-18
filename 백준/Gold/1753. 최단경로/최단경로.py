from queue import PriorityQueue
import sys

input = sys.stdin.readline
INF = float('INF')
def solution():

    P, L = map(int,input().split())

    S = int(input())

    adj_graph = [ [] for _ in range(P+1)]
    for _ in range(L):
        s,e,d = map(int,input().split())
        adj_graph[s].append([e,d])

    pq = PriorityQueue()
    dist = [INF] * (P+1)

    
    dist[S] = 0
    pq.put([0,S])

    while not pq.empty():
        
        cur_dist, cur_node = pq.get()
        
        if dist[cur_node] < cur_dist:
            continue

        for adj_node,adj_dist in adj_graph[cur_node]:
            if adj_dist+cur_dist < dist[adj_node]:
                dist[adj_node] = adj_dist + cur_dist
                pq.put([adj_dist+cur_dist,adj_node])

    for each in dist[1:]:
        print( each if each != INF else 'INF')

solution()

