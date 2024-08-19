T = int(input())
for tc in range(1, T + 1):
    p, a, b = map(int, input().split())
    book = [x + 1 for x in range(p)]

    start = 1; end = p
    mid = (start + end) // 2
    cnt_a = 0

    while mid != a:
        if a < mid:
            end = mid
        elif a > mid:
            start = mid
        cnt_a += 1
        mid = (start + end) // 2

    start = 1; end = p
    mid = (start + end) // 2
    cnt_b = 0

    while mid != b:
        if b < mid:
            end = mid
        elif b > mid:
            start = mid
        cnt_b += 1
        mid = (start + end) // 2
    print(f'#{tc}', end=' ')
    if cnt_a > cnt_b:
        print("B")
    elif cnt_a < cnt_b:
        print("A")
    else:
        print(0)
