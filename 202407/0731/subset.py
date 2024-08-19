T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))

    k = len(lst)
    result = 0

    for i in range(1 << k):
        total = 0
        for j in range(k):
            if i & (1 << j):
                total += lst[j]
        if total == 0:
            result = 1

    print(f'#{tc} {result}')
