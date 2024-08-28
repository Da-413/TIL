T = int(input())
for tc in range(1, T + 1):
    n, m, l = map(int, input().split())
    value = [0] * (n + 1)
    for _ in range(m):
        idx, val = map(int, input().split())
        value[idx] = val

    for i in range(n - m, 0, -1):
        if 2 * i < n:
            value[i] = value[2 * i] + value[2 * i + 1]
        else:
            value[i] = value[2 * i]

    print(f"#{tc} {value[l]}")