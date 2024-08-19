T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    carrot = list(map(int, input().split()))

    M = max(carrot)
    count = [0] * (M + 1)
    for ca in carrot:
        count[ca] += 1
    count.pop(0)

    for i in range(1, M):
        count[i] += count[i-1]

    minimum = 1000
    for left in range(M - 2):
        for right in range(left + 1, M - 1):
            small = count[left]
            medium = count[right] - count[left]
            large = count[-1] - count[right]

            if small <= n // 2 and medium <= n // 2 and large <= n // 2:
                temp = max(abs(small - medium), abs(medium - large), abs(large - small))
                if temp < minimum:
                    minimum = temp
    
    if minimum == 1000:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {minimum}')
