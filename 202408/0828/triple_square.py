T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    start = 1; end = n

    while end >= start:

        mid = (end + start) // 2

        if (end - start) <= 1 and (start ** 3) != n and (end ** 3) != n:
            print(f"#{tc} -1")
            break

        if (mid ** 3) == n:
            print(f"#{tc} {mid}")
            break
        
        elif (mid ** 3) > n:
            end = mid

        else:
            start = mid
