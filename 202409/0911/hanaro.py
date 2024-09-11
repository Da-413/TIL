import sys
sys.stdin = open("hanaro.txt")

import heapq
from itertools import permutations

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))

    distance = [float("INF")] * n
    distance[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = cost + dist

            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            heapq.heappush(heap, (new_cost, next_node))

    return distance

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i].append((j, E * ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)))
    
    
    path = [0] * n
    for i in range(n):
        path[i] = dijkstra(i)
    print("path: ", path)
    idxes = list(permutations(range(n), n))
    print("idxes: ", idxes)
    print("==================")
    for idx in idxes:
        for i in range(n):
            print(path[idx[i]][i], end = " ")
        print()
