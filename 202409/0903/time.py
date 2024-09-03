T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    duration = [list(map(int, input().split())) for _ in range(n)]
    duration.sort(key = lambda x: (x[1], x[0]))
    
    cnt = 1
    current = duration[0][1]
    for i in range(1, n):
        if duration[i][0] >= current:
            cnt += 1
            current = duration[i][1]

    print(f"#{tc} {cnt}")