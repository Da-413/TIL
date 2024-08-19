T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [[0] * n for _ in range(n)]

    i = 0; j = 0

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    k = 0; index = 0

    while index < (n ** 2):
        index += 1
        matrix[i][j] = index
        nx = i + dx[k]
        ny = j + dy[k]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or matrix[nx][ny] != 0:
            k = (k + 1) % 4
        i += dx[k]
        j += dy[k]

    print(f'#{tc}')
    for i in range(n):
        print(*matrix[i])
    


