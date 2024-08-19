for tc in range(1, 11):
    n = int(input())
    matrix = [list(input()) for _ in range(8)]
    transpose = [[0] * 10 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            transpose[i][j] = matrix[j][i]


    def find_palin(lst):
        if lst[:] == lst[::-1]:
            return 1
        else:
            return 0


    cnt = 0
    for i in range(8):
        for j in range(9 - n):
            row_word = matrix[i][j:j + n]
            if find_palin(row_word):
                cnt += 1
            col_word = transpose[i][j:j + n]
            if find_palin(col_word):
                cnt += 1

    print(f'#{tc} {cnt}')
