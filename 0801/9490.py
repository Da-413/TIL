T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    maximum = -1

    for i in range(n):
        for j in range(m):

            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            total = matrix[i][j]
            center = matrix[i][j]

            for k in range(4):
                for l in range(1, center + 1):
                    nx = i + dx[k] * l
                    ny = j + dy[k] * l

                    if 0 <= nx < n and 0 <= ny < m:
                        total += matrix[nx][ny]

            if total > maximum:
                maximum = total

    print(f'#{tc} {maximum}')