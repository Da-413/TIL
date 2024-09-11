import heapq

def dijkstra(start):
    global n

    heap = []
    heapq.heappush(heap, (0, start))
    distance = [float("INF")] * (n + 1)
    distance[start] = 1

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            cost, next_node = next[1], next[0]

            new_cost = cost + dist

            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            heapq.heappush(heap, (new_cost, next_node))

    return distance

T = int(input())
for tc in range(1, T + 1):
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append([b, w])

    dist = [0] * (n + 1)
    for i in range(1, n + 1):
        result = dijkstra(i)
        dist[i] = result[x]

    ans = dijkstra(x)
    for i in range(1, n + 1):
        dist[i] += ans[i]

    print(f"#{tc} {max(dist)}")
