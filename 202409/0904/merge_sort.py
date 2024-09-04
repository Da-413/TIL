def merge_sort(lst):
    global cnt 

    if len(lst) < 2:
        return lst
    
    length = len(lst)

    mid = length // 2
    left = lst[:mid]
    right = lst[mid:]

    left_ = merge_sort(left)
    right_ = merge_sort(right)

    l = length // 2; r = (length + 1) // 2
    i, j = 0, 0
    sorted_list = []

    if left_[-1] > right_[-1]:
        cnt += 1

    while i < l and j < r:
        if left_[i] <= right_[j]:
            sorted_list.append(left_[i])
            i += 1
        else:
            sorted_list.append(right_[j])
            j += 1

    while i < l:
        sorted_list.append(left_[i])
        i += 1
    
    while j < r:
        sorted_list.append(right_[j])
        j += 1
            
    return sorted_list


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    result = merge_sort(lst)

    print(f'#{tc}', result[n // 2], cnt)
