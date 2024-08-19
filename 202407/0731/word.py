T = int(input())
for tc in range(1, T + 1):     
    n, k = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    ans = 0

    def find_k(lst, k):
        temp = 0
        result = []
        for i in range(len(lst)):
            if lst[i] == 1:
                temp += 1
            else:
                result.append(temp)
                temp = 0
            if i == len(lst) - 1:
                result.append(temp)
        cnt = 0
        for element in result:
            if element == k:
                cnt += 1

        return cnt


    ans = 0
    for i in range(n):
        ans += find_k(matrix[i], k)

    for j in range(n):
        ans += find_k(list(zip(*matrix))[j], k)

    print(f'#{tc} {ans}')