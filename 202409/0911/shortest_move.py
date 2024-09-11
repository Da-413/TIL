import heapq

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
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


T = int(input())
for tc in range(1, T + 1):
    n, e = map(int, input().split())
    matrix = [tuple(map(int, input().split())) for _ in range(e)]
    graph = [[] for _ in range(n + 1)]
    for i in range(e):
        a, b, w = matrix[i]
        graph[a].append([b, w])
    distance = [float("INF")] * (n + 1)

    dijkstra(0)
    print(f"#{tc} {distance[n]}")