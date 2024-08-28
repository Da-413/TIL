def heappush(new):
    global last

    last += 1
    heap[last] = new
    c = last
    p = c // 2
    while p >= 1 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    last = 0
    heap = [0] * (n + 1)
    for num in arr:
        heappush(num)

    target = arr[-1]

    idx = last
    ans = 0
    while idx > 1:
        idx //= 2
        ans += heap[idx]

    print(f"#{tc} {ans}")