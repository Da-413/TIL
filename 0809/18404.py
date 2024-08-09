lst = list(map(int, input().split()))
cnt = 0


def find_subset(i, k, s, t):
    global cnt
    subset = [0] * k

    if s > t:
        return
    elif s == t:
        cnt += 1
        return
    elif i == k:
        return
    else:
        subset[i] = 1
        find_subset(i + 1, k, s + lst[i], t)
        subset[i] = 0
        find_subset(i + 1, k, s, t)


find_subset(0, len(lst), 0, 10)
print(f'#1 {cnt}')