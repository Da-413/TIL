T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    maximum = matrix[0][0] + matrix[0][1] + matrix[1][0]        # (0,0)인덱스 기준으로 미생물이 먹은 먹이로 maximum 초기화
    for i in range(n):
        for j in range(n):

            dx = [0, 1, 0, -1, 0]
            dy = [0, 0, 1, 0, -1]
            total = 0

            for k in range(5):                                  # 델타 탐색색
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    total += matrix[nx][ny]

            if total > maximum:
                maximum = total

    print(f'#{tc} {maximum}')