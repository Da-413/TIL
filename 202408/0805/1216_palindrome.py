import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    matrix = [list(input()) for _ in range(100)]
    transpose = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            transpose[i][j] = matrix[j][i]


    def find_palin(lst):
        if lst[:] == lst[::-1]:
            return 1
        else:
            return 0

    ans = 0
    for i in range(100):
        for j in range(100):
            for k in range(100 - j, 0, -1):
                if find_palin(matrix[i][j:j + k]):
                    if k > ans:
                        ans = k
                if find_palin((transpose[i][j:j + k])):
                    if k > ans:
                        ans = k

    print(f'#{tc} {ans}')
