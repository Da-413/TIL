T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    total = 0

    for i in range(n):
        total += (matrix[i][i] + matrix[i][n - 1 - i])

    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]

print(f'#{tc} {total}')


