T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [[-1] * n for _ in range(n)]
    center = n // 2 - 1
    matrix[center][center] = 2
    matrix[center + 1][center] = 1
    matrix[center][center + 1] = 1
    matrix[center + 1][center + 1] = 2

    for i in range(m):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1

        matrix[x][y] = color

        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [1, 1, 0, -1, -1, -1, 0, 1]

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                coord = []
                while abs(matrix[nx][ny] - color) == 1:
                    coord.append([nx, ny])
                    nx = nx + dx[k]
                    ny = ny + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        break
                if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == color:
                    for coord in coord:
                        matrix[coord[0]][coord[1]] = color

        cnt1 = 0; cnt2 = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    cnt1 += 1
                elif matrix[i][j] == 2:
                    cnt2 += 1

    print(f'#{tc} {cnt1} {cnt2}')
