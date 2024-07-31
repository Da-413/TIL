T = int(input())
for tc in range(1, T + 1):

    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    total = 0

    for i in range(5):
        for j in range(5):

            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < 5 and 0 <= ny < 5:
                    if matrix[i][j] > matrix[nx][ny]:
                        total += (matrix[i][j] - matrix[nx][ny])
                    else:
                        total += (matrix[nx][ny] - matrix[i][j])

    print(f'#{tc} {total}')