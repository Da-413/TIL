for tc in range(1, 11):
    t = int(input())
    a, b = map(int, input().split())

    def my_power(a, b):
        if b == 0:
            return 1
        else:
            return a * my_power(a, b - 1)

    print(f'#{tc} {my_power(a, b)}')