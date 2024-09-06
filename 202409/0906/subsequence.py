def sub_seq(idx, path, total):
    global cnt, size

    if total > target:
        return

    if len(path) == size:
        if total == target:
            cnt += 1
        return
    
    for i in range(idx, n):
        sub_seq(i + 1, path + [seq[i]], total + seq[i])
    

T = int(input())
for tc in range(1, T + 1):
    n, target = map(int, input().split())
    seq = list(map(int, input().split()))
                
    cnt = 0
    path = []
    total = 0
    for i in range(1, n + 1):
        size = i
        sub_seq(0, path, total)

    print(f"#{tc} {cnt}")