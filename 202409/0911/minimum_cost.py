import heapq

def dijkstra(sx, sy):
    heap = []
    heapq.heappush(heap, (0, sx, sy))
    distance[sx][sy] = 1

    while heap:
        dist, nowx, nowy = heapq.heappop(heap)

        if distance[nowx][nowy] < dist:
            continue

        for k in range(4):
            nx = nowx + dx[k]
            ny = nowy + dy[k]
            if 0 <= nx < n and 0 <= ny < n:

                if distance[nx][ny] < dist:
                    continue

                if area[nx][ny] - area[nowx][nowy] > 0:
                    new_cost = dist + 1 + (area[nx][ny] - area[nowx][nowy])
                else:
                    new_cost = dist + 1

                if new_cost >= distance[nx][ny]:
                    continue

                distance[nx][ny] = new_cost
                heapq.heappush(heap, (new_cost, nx, ny))


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    distance = [[float('INF')] * n for _ in range(n)]

    dijkstra(0, 0)
    print(f"#{tc} {distance[n-1][n-1]}")