T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]
    transpose = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transpose[i][j] = matrix[j][i]

    def find_palin(word):
        if len(word) == 0 or len(word) == 1:
            return 1
        else:
            if word[0] != word[-1]:
                return 0
            else:
                word = word[1:-1]
                return find_palin(word)
    ans = ''
    for i in range(n):
        for j in range(n - m + 1):
            target_row = matrix[i][j:j + m]
            if find_palin(target_row):
                ans = target_row
                break

            target_col = transpose[i][j:j + m]
            if find_palin(target_col):
                ans = ''.join(target_col)
                break

    print(f'#{tc}', end=' ')
    print(ans)

