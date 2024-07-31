T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    one = list(input())

    cnt = 0; maximum = 0
    for i in range(len(one)):

        if one[i] == '1':
            cnt += 1
        else:
            if cnt > maximum:
                maximum = cnt
                cnt = 0
        if i == len(one) - 1:
            if cnt > maximum:
                maximum = cnt
                cnt = 0

    print(maximum)
