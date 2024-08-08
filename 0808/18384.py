T = int(input())


def dfs(start, n):
    visited = [[0] * n for _ in range(n)]
    sx = start[0]; sy = start[1]
    stack = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited[sx][sy] = 1

    while True:
        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            while 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                stack.append([nx, ny])
                nx += dx[k]
                ny += dy[k]
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 3:
                return 1

        else:
            if stack:
                recent = stack.pop()
                sx = recent[0]
                sy = recent[1]
            else:
                return 0


for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(n)]

    start = []; end = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 2:
                start = [i, j]

    print(f'#{tc} {dfs(start, n)}')
