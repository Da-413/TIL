T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, list(input())))


    def my_max(arr):
        maximum = arr[0]
        for element in arr:
            if maximum < element:
                maximum = element
        return maximum


    m = my_max(lst)
    count = [0] * (m + 1)

    for i in range(len(lst)):
        count[lst[i]] += 1

    M = my_max(count)
    ans = 0
    for i in range(len(count) - 1, -1, -1):
        if count[i] == M:
            ans = i
            break

    print(f'# {ans} {M}')

# for i in range(1, m):
#     count[i] += count[i - 1]
#
# temp = [0] * len(lst)
# for i in range(len(lst) - 1, -1, -1):
#     count[lst[i] - 1] -= 1
#     temp[count[lst[i] - 1]] = lst[i]

