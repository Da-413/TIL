import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    t = int(input())
    queue = list(map(int, input().split()))

    while queue[-1] > 0:
        for k in range(1, 6):
            num = queue.pop(0) - k
            if num > 0:
                queue.append(num)
            elif num <= 0:
                queue.append(0)
                break

    print(f'#{tc}', end=' ')
    print(*queue)