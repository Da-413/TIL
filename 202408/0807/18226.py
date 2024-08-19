T = int(input())
for tc in range(1, T + 1):
    n = int(input()) // 10

    tile = [1, 3]
    for i in range(2, n):
        tile.append((2 * tile[i - 2] + tile[i - 1]))

    print(f'#{tc} {tile[n - 1]}')
