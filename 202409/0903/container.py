T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    weight.sort(reverse=True)
    truck.sort()
    total = 0
    for stuff in weight:
        if truck and stuff <= truck[-1]:
            total += stuff
            truck.pop()
    print(f"#{tc} {total}")