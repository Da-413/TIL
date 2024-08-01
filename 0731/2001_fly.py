T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    ans = []
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            kill = 0
            for k in range(m):
                for l in range(m):
                    kill += matrix[i + k][j + l]

            ans.append(kill)

    def my_max(lst):
        result = lst[0]
        for elem in lst:
            if elem > result:
                result = elem
        return result

    print(f'{tc} {my_max(ans)}')