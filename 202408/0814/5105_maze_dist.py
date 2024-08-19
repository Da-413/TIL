def bfs(s):
    ni, nj = s[0], s[1]
    queue = []
    visited[ni][nj] = 1
    queue.append(s)

    while queue:
        ti, tj = queue.pop(0)

        if maze[ti][tj] == 3:
            return visited[ti][tj] - 2

        for [di, dj] in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni = ti + di
            nj = tj + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and maze[ni][nj] != 1:
                queue.append([ni, nj])
                visited[ni][nj] = visited[ti][tj] + 1

    return 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = [i, j]

    print(f"#{tc} {bfs(start)}")