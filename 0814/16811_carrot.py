T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    carrot = list(map(int, input().split()))

    M = max(carrot)
    count = [0] * (M + 1)
    for ca in carrot:
        count[ca] += 1
    count.pop(0)

    minimum = 1000
    for left in range(1, M - 2):
        for right in range(left + 1, M - 1):
            small = sum(count[:left])
            medium = sum(count[left:right])
            large = sum(count[right:])

            result = [small, medium, large]
            print(result)
            # for i in range(3):
            #     if result[i] > n // 2:
            #         minimum = -1
            # if medium - small < minimum:
            #     minimum = medium - small
            # if large - medium < minimum:
            #     minimum = large - minimum


    print(minimum)
