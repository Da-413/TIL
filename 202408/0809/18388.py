import sys
sys.stdin = open('input.txt')

T = int(input())


def func(row, s):
    global visited_col
    global target

    for i in range(n):
        if s > target:
            return
        elif row == n:
            if s <= target:
                target = s
            return
        elif visited_col[i] == 0:
            visited_col[i] = 1
            func(row + 1, s + matrix[row][i])
            visited_col[i] = 0


for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    target = 0
    for i in range(n):
        for j in range(n):
            target += matrix[i][j]
    visited_col = [0] * n
    func(0, 0)

    print(f'#{tc} {target}')
