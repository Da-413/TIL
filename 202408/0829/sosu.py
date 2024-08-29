T = int(input())
for tc in range(1, T + 1):
    x = float(input())
    ans = ''
    while int(x) != x:
        x *= 2
        ans = ans + str(int(x))
        x -= int(x)
        if len(ans) > 12:
            ans = 'overflow'
            break

    print(f"#{tc} {ans}")
