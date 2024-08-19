T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    lst = sorted(list(map(int, input().split())))

    for i in range(len(lst)):
        if (lst[i] // m) * k < (i + 1):
            print(f'#{tc} Impossible')
            break
    else:
        print(f'#{tc} Possible')