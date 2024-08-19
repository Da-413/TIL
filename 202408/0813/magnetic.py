import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    transpose = [[0] * 100 for _ in range(100)]

    for i in range(100):
        for j in range(100):
            transpose[i][j] = matrix[j][i]

    ans = 0
    for i in range(100):
        cnt = 0
        for j in range(100):
            left = 0
            if transpose[i][j] == 1:
                left = j
                break
        for j in range(99, -1, -1):
            right = 99
            if transpose[i][j] == 2:
                right = j
                break
        magnet = []
        for j in range(left, right + 1):
            if transpose[i][j] != 0:
                magnet.append(j)

        for k in range(len(magnet)):
            if transpose[i][magnet[k]] == 1:
                cnt += 1
                if transpose[i][magnet[k - 1]] == 1:
                    cnt -= 1

        ans += cnt

    print(f'#{tc} {ans}')