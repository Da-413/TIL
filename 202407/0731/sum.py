for i in range(1, 11):
    tc = int(input())
    matrix = []
    for i in range(100):
        matrix.append(list(map(int, input().split())))

    col = [0] * 100; row = [0] * 100; diag = [0, 0]
    for i in range(100):
        for j in range(100):
            row[i] += matrix[i][j]
            col[i] += matrix[j][i]
        diag[0] += matrix[i][i]
        diag[1] += matrix[i][99 - i]

    def my_max(lst):
        result = lst[0]
        for x in lst:
            if result < x:
                result = x
        return result
    ans = my_max([my_max(row), my_max(col), my_max(diag)])
    print(f'#{tc} {ans}')