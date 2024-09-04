def binary_search(arr, target):
    global check

    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return True
        
        if arr[mid] < target:
            if check == True:
                return False
            check = True
            start = mid + 1

        elif arr[mid] > target:
            if check == False:
                return False
            check = False
            end = mid - 1

    return False


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    target = list(map(int, input().split()))
    cnt = 0

    for num in target:
        check = 2
        if binary_search(lst, num):
            cnt += 1

    print(f"#{tc} {cnt}")