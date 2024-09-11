import heapq

def prim(start):
    global n

    heap = []
    heapq.heappush(heap, (0, start))

    weight = 0

    while heap:
        w, node = heapq.heappop(heap)

        if MST[node]:
            continue

        MST[node] = 1
        weight += w

        for t in range(n):
            if graph[node][t] == 0:
                continue
            
            if MST[t]:
                continue

            heapq.heappush(heap, (graph[node][t], t))

    return weight


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i].append((j, E * ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)))
    
    
    MST = [0] * n
    
    result = []
    for i in range(n):
        result.append(prim(i))
    
    print(f"#{tc} {round(max(result))}")
