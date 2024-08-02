from copy import deepcopy

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]


    def rotate(matrix):
        return_matrix = deepcopy(matrix)
        length = len(return_matrix)

        for i in range(length):
            for j in range(length):
                return_matrix[j][length - 1 - i] = matrix[i][j]

        return return_matrix


    rotate90 = rotate(matrix)
    rotate180 = rotate(rotate90)
    rotate270 = rotate(rotate180)
    ans = list(zip(rotate90, rotate180, rotate270))

    print(f'#{tc}')
    for i in range(len(ans)):
        for j in range(3):
            print(*ans[i][j], sep='', end=' ')
        print()