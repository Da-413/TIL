T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    profit = 0
    max_price = 0

    for i in range(len(lst)-1, -1, -1):
        if lst[i] > max_price:
            max_price = lst[i]
        else:
            profit += max_price - lst[i]

    print(f'#{test_case} {profit}')