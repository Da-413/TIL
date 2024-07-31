T = int(input())
for tc in range(1, T + 1):

    n = int(input())
    lst = list(map(int, input().split()))


    def my_max(lst):
        result = lst[0]
        for i in lst:
            if i > result:
                result = i
        return result


    count = [0] * (my_max(lst) + 1)

    for i in range(len(lst)):
        count[lst[i]] += 1

    M = my_max(count)
    ans = 0
    for i in range(len(count) - 1, -1, -1):
        if count[i] == M:
            ans = i
            break

    print(f'#{tc} {ans}')