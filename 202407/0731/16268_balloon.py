T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    maximum = -1

    for i in range(n):
        for j in range(m):

            dx = [0, 1, -1, 0, 0]
            dy = [0, 0, 0, 1, -1]
            total = 0

            for k in range(5):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < n and 0 <= ny < m:
                    total += matrix[nx][ny]

            if total > maximum:
                maximum = total

    print(f'#{tc} {maximum}')