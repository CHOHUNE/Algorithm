import sys
import heapq

INF = float('INF')

input = sys.stdin.readline

def dajikstar(start_v,graph,dist):
    
    dist[start_v] = 0 
    hq = []

    heapq.heappush(hq,[0,start_v])

    while hq:
        
        now_dis, now_v = heapq.heappop(hq)

        if now_dis > dist[now_v]:
            continue
        
        for next_v in graph[now_v]:
            cost = next_v[0] + now_dis

            if cost < dist[next_v[1]]:
                dist[next_v[1]] = cost
                heapq.heappush(hq,[cost,next_v[1]])


def solution():

    
    P = int(input())
    L = int(input())

    graph = [ [] for _ in range(P+1)]

    for _ in range(L):

        s,e,w = map(int,input().split())
        graph[s].append([w,e])

    dist = [INF] * (P+1)
    start , end = map(int,input().split())
    dajikstar(start,graph,dist)

    print(dist[end])


solution()






    