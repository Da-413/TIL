T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    def min_index(target):
        result = 0
        for i in range(len(target)):
            if target[i] < target[result]:
                result = i
        return result

    def max_index(target):
        result = 0
        for i in range(len(target)):
            if target[i] > target[result]:
                result = i
        return result

    for i in range(0, n, 2):
        maximum = max_index(lst[i:]) + i

        temp = lst[i]
        lst[i] = lst[maximum]
        lst[maximum] = temp
        
        minimum = min_index(lst[i + 1:]) + (i + 1)

        temp = lst[i + 1]
        lst[i + 1] = lst[minimum]
        lst[minimum] = temp

    print(f'#{tc}', end=' ')
    for i in range(10):
         print(lst[i], end=' ')
    print()