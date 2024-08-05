T = int(input())
for tc in range(1, T + 1):
    a, b = input().split()
    m = len(a); n = len(b)
    cnt = 0

    i = 0
    while i < m:
        if a[i:i + n] == b:
            cnt += 1
            i = i + n
        else:
            i += 1

    ans = m - (n - 1) * cnt
    print(f'#{tc} {ans}')
