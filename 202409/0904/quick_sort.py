def quick_sort(arr, start, end):

    if len(arr) < 2:
        return arr
    
    pivot = start
    left = []
    right = []
    for i in range(start + 1, end):
        if arr[i] <= arr[pivot]:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left, 0, len(left)) + [arr[pivot]] + quick_sort(right, 0, len(right))


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))

    sorted_lst = quick_sort(lst, 0, n)
    print(f"#{tc} {sorted_lst[n // 2]}")