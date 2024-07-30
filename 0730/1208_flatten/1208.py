for tc in range(1, 11):
    n = int(input())

    def my_max(lst):
        result = lst[0]
        for e in lst:
            if e > result:
                result = e
        return result


    box = list(map(int, input().split()))
    k = len(box)
    count = [0] * my_max(box)

    for i in range(k):
        count[box[i] - 1] += 1

    cnt = 0
    diff = 0
    start = 0
    end = len(count) - 1

    while cnt < n and start + 1 < end:

        if count[start] != 0 and count[end] != 0:
            count[end - 1] += 1
            count[start + 1] += 1
            count[start] -= 1
            count[end] -= 1

        if count[start] == 0:
            start += 1

        if count[end] == 0:
            end -= 1

        cnt += 1
        diff = end - start

        # if diff == 1 and (count[end] == 0 or count[start] == 0):
        #     break
        #
        # elif diff == 0:
        #     break

    print(f'#{tc} {diff}')

