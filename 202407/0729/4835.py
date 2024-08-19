T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    initial = 0
    for i in range(m):
        initial += lst[i]

    maximum = initial
    minimum = initial

    for i in range(n - m + 1):

        total = 0

        for j in range(i, i + m):
            total += lst[j]

        if total < minimum:
            minimum = total
        elif total > maximum:
            maximum = total

    print(f'#{tc} {maximum - minimum}')
