T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    maximum = lst[0]
    minimum = lst[0]

    for value in lst:
        if value < minimum:
            minimum = value
        elif value > maximum:
            maximum = value

    print(f'#{tc} {maximum - minimum}')