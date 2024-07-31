T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    lst = list(range(1, 13))

    result = 0
    subset_set = []
    for i in range(1 << 12):
        subset = []
        for j in range(12):
            if i & (1 << j):
                subset.append(lst[j])
        subset_set.append(subset)

    for sub in subset_set:
        if len(sub) == n:
            total = 0
            for element in sub:
                total += element
            if total == k:
                result = 1

    print(f'#{tc} {result}')
