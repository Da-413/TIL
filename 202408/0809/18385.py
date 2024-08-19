import sys
sys.stdin = open('input.txt')

T = int(input())


def my_round(n):
    temp = (n * 10) % 10
    if temp >= 5:
        return int(n) + 1
    else:
        return int(n)


def rcp(a, b):
    a0 = a[0]
    b0 = b[0]
    if (a0 - b0) % 3 == 0:
        return 0
    elif (a0 - b0) % 3 == 1:
        return 1
    elif (a0 - b0) % 3 == 2:
        return 2


def versus(target):
    length = len(target)

    if length <= 1:
        return target

    mid = my_round(length / 2)
    left = target[:mid]
    right = target[mid:]

    left = versus(left)
    right = versus(right)

    i = 0
    j = 0
    l = len(left)
    r = len(right)
    ranking = []

    while i < l and j < r:
        func_result = rcp(left[i], right[j])
        if func_result == 0 or func_result == 1:
            ranking.append(left[i])
            i += 1
        else:
            ranking.append(right[j])
            j += 1

    while i < l:
        ranking.append(left[i])
        i += 1
    while j < r:
        ranking.append(right[j])
        j += 1

    return ranking


for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    cards = []
    for idx, v in enumerate(lst):
        cards.append((v, idx + 1))

    result = versus(cards)
    print(f'#{tc} {result[0][1]}')
