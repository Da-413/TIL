for tc in range(10):
    n = int(input())
    lst = list(map(int, input().split()))


    def my_min(lst):
        minimum = lst[0]
        for num in lst:
            if num < minimum:
                minimum = num
        return minimum


    total = 0

    for i in range(2, n - 2):
        view = [lst[i] - lst[i - 1], lst[i] - lst[i - 2], lst[i] - lst[i + 1], lst[i] - lst[i + 2]]
        if my_min(view) > 0:
            total += my_min(view)

    print(f'#{tc + 1} {total}')
