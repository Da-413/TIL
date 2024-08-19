T = int(input())
for tc in range(1, T + 1):
    matrix = [[0] * 10 for _ in range(10)]
    n = int(input())
    cnt = 0
    for _ in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        if color == 1:
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if matrix[i][j] == 0:
                        matrix[i][j] = 1
                    elif matrix[i][j] == 2:
                        matrix[i][j] = 3
        else:
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if matrix[i][j] == 0:
                        matrix[i][j] = 2
                    elif matrix[i][j] == 1:
                        matrix[i][j] = 3

    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
