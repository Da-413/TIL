import heapq

def prim(start):
    global v

    heap = []
    heapq.heappush(heap, (0, start))

    weight = 0

    while heap:
        w, node = heapq.heappop(heap)

        if MST[node]:
            continue

        MST[node] = 1
        weight += w

        for t in range(v + 1):
            if graph[node][t] == 0:
                continue
            
            if MST[t]:
                continue

            heapq.heappush(heap, (graph[node][t], t))

    return weight


T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    graph = [[0] * (v + 1) for _ in range(v + 1)]
    for _ in range(e):
        a, b, w = map(int, input().split())
        graph[a][b] = w
        graph[b][a] = w
    MST = [0] * (v + 1)

    result = prim(0)
    print(f"#{tc} {result}")