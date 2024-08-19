T = int(input())
for tc in range(1, 1 + T):
    n = int(input())
    pascal = [[1] * x for x in range(1, n + 1)]
    print(f'#{tc}')

    for i in range(2, n):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    for i in range(n):
        print(*pascal[i])